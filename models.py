from dataclasses import dataclass, field, fields, is_dataclass
from datetime import datetime
from typing import Any, Dict, List, Type, TypeVar, Optional

T = TypeVar("T")

def _to_api_converter(value: Any) -> Any:
    """Converts dataclass objects to dictionaries and datetimes to ISO strings for API payload."""
    if is_dataclass(value):
        return value.to_api()
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, list):
        return [_to_api_converter(item) for item in value]
    return value

def _from_api_converter(cls, data: Any):
    """Helper to convert nested API data."""
    if hasattr(cls, 'from_api'):
        return cls.from_api(data)
    return data

@dataclass
class BaseModel:
    @classmethod
    def from_api(cls: Type[T], data: Dict[str, Any]) -> T:
        """Creates a model instance from an API dictionary response."""
        if not data:
            return None
            
        kwargs = {}
        for f in fields(cls):
            if f.name in data:
                field_value = data[f.name]
                field_type = f.type
                
                # Handle Optional[Type]
                origin = getattr(field_type, '__origin__', None)
                if origin is Optional:
                    field_type = field_type.__args__[0]

                # Handle List[Type]
                if origin is list:
                    item_type = field_type.__args__[0]
                    if field_value is not None:
                        kwargs[f.name] = [_from_api_converter(item_type, item) for item in field_value]
                # Handle datetime conversion
                elif field_type is datetime and isinstance(field_value, str):
                    try:
                        # Handles formats like '2024-01-01T12:00:00+02:00' and '2024-01-01T12:00:00.000Z'
                        if '+' in field_value:
                             # fromisoformat supports this directly
                            kwargs[f.name] = datetime.fromisoformat(field_value)
                        elif 'Z' in field_value:
                            kwargs[f.name] = datetime.fromisoformat(field_value.replace('Z', '+00:00'))
                        else: # Fallback for simpler formats if needed
                             kwargs[f.name] = datetime.fromisoformat(field_value)
                    except (ValueError, TypeError):
                        kwargs[f.name] = None # Or handle error appropriately
                # Handle nested dataclasses
                elif is_dataclass(field_type) and isinstance(field_value, dict):
                    kwargs[f.name] = field_type.from_api(field_value)
                else:
                    kwargs[f.name] = field_value
        return cls(**kwargs)

    def to_api(self) -> Dict[str, Any]:
        """Converts the model instance to a dictionary for API requests."""
        data = {}
        for f in fields(self):
            value = getattr(self, f.name)
            if value is not None:
                # Exclude read-only fields from the payload, identified by metadata
                if not f.metadata.get('readonly', False):
                    data[f.name] = _to_api_converter(value)
        return data

@dataclass
class ChangeRecord(BaseModel):
    id: int
    updated_at: datetime

@dataclass
class Field(BaseModel):
    id: int = field(metadata={'readonly': True})
    name: str
    field_group_id: int
    calculated_area: float = field(metadata={'readonly': True})
    created_at: datetime = field(metadata={'readonly': True})
    updated_at: datetime = field(metadata={'readonly': True})
    additional_info: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    field_type: Optional[str] = None
    parent_id: Optional[int] = None
    current_shape_id: Optional[int] = field(default=None, metadata={'readonly': True})
    legal_area: Optional[float] = None
    tillable_area: Optional[float] = None
    administrative_area_name: Optional[str] = None
    subadministrative_area_name: Optional[str] = None
    locality: Optional[str] = None
    public_registry_key: Optional[str] = None
    moisture_zone: Optional[str] = None
    end_time: Optional[datetime] = field(default=None, metadata={'readonly': True})


@dataclass
class Crop(BaseModel):
    id: int = field(metadata={'readonly': True})
    name: str
    short_name: Optional[str] = None
    standard_name: Optional[str] = None
    season_type: Optional[str] = None
    color: Optional[str] = field(default=None, metadata={'readonly': True})
    base_crop_id: Optional[int] = None
    productivity_estimate_crop_name: Optional[str] = None
    additional_info: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    hidden: Optional[bool] = None
    created_at: datetime = field(metadata={'readonly': True})
    updated_at: datetime = field(metadata={'readonly': True})

@dataclass
class AgroOperation(BaseModel):
    id: int = field(metadata={'readonly': True})
    field_id: int
    work_type_id: int
    status: str
    season: int
    created_at: datetime = field(metadata={'readonly': True})
    updated_at: datetime = field(metadata={'readonly': True})
    agri_work_plan_id: Optional[int] = None
    agro_recommendation_id: Optional[int] = None
    operation_number: Optional[str] = None
    planned_area: Optional[float] = None
    completed_area: Optional[float] = None
    harvested_weight: Optional[float] = None
    planned_start_date: Optional[datetime] = None
    planned_end_date: Optional[datetime] = None
    actual_start_datetime: Optional[datetime] = None
    completed_datetime: Optional[datetime] = None
    planned_water_rate: Optional[float] = None
    fact_water_rate: Optional[float] = None
    planned_rows_spacing: Optional[float] = None
    planned_depth: Optional[float] = None
    planned_speed: Optional[float] = None
    additional_info: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    locked_to_edit: Optional[bool] = None
    locked_at: Optional[datetime] = field(default=None, metadata={'readonly': True})
    responsible_user_ids: Optional[List[int]] = None
    partially_completed: Optional[bool] = field(default=None, metadata={'readonly': True})
    partially_completed_manually_defined_area: Optional[float] = field(default=None, metadata={'readonly': True})
    covered_area: Optional[float] = field(default=None, metadata={'readonly': True})
    covered_area_by_track: Optional[float] = field(default=None, metadata={'readonly': True})
    machine_work_area: Optional[float] = field(default=None, metadata={'readonly': True})
    fuel_consumption: Optional[float] = field(default=None, metadata={'readonly': True})
    fuel_consumption_per_ha: Optional[float] = field(default=None, metadata={'readonly': True})
    protein_content: Optional[float] = None
    oil_content: Optional[float] = None
    humidity: Optional[float] = None
    harmful_admixture: Optional[float] = None
    garbage_admixture: Optional[float] = None
    grain_admixture: Optional[float] = None
    oil_acid_number: Optional[float] = None
    marketable_weight: Optional[float] = None
    application_mix_items: Optional[List[int]] = field(default=None, metadata={'readonly': True})
    history_item_id: Optional[int] = None
    additional_product_type: Optional[str] = None
    additional_product_weight: Optional[float] = None
    application_by_days: Optional[bool] = None
