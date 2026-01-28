Cropwise Operations Platform API v3

Reference
Introduction
General info

You can use Cropwise Operations Platform API if you have account on Cropwise Operations Platform web site.

Cropwise Operations Platform API is HTTP JSON API. That means all requests and responses are sent via HTTP protocol (secured with SSL). All data in requests and responses present in HTTP Body in JSON format.

Cropwise Operations Platform API is based on REST principles. You have to be authenticated and call the simple HTTPs request on the URLs specified below. The following documentation covers core resources that are used to manipulate the main entities. First of all, read basic instructions to start using the API. Machine
Legacy cropio.com domain name

Cropwise Operations Platform API v3 works both from:

    https://operations.cropwise.com/api/v3 — recommended;

    https://cropio.com/api/v3 — legacy, would be redirected to https://operations.cropwise.com/api/v3 starting April 1, 2022.

We highly recommend to use https://operations.cropwise.com/api/v3.

https://cropio.com/api/v3 would be available till April 1, 2022. Then all requests to https://cropio.com/api/v3 would be automatically redirected to https://operations.cropwise.com/api/v3.
Very basics of HTTP REST concepts
Allowed HTTPs request typesemail

    GET — Get a resource or list of resources

    POST — To create or update resource

    PUT — To create or update resource

    DELETE — To delete resource

Usual HTTP response codes

    200 OK — the request was successful.

    201 Created — the request was successful and a resource was created.

    204 No Content — the request was successful but there is no representation to return (i.e. the response is empty).

    400 Bad Request — the request could not be understood or was missing required parameters.

    401 Unauthorized — authentication failed or user doesn't have permissions for requested operation.

    403 Forbidden — access denied.

    404 Not Found — resource was not found.

    422 Unprocessable Entity - the request was well-formed but was unable to be followed due to semantic errors.

    503 Service Unavailable — service is temporary unavailable (e.g. scheduled Platform Maintenance). Try again later.

Methods

    Resources collection => GET https://operations.cropwise.com/api/v3/OBJECTS — get list of objects.

    Ids => GET https://operations.cropwise.com/api/v3/OBJECTS/ids — get list of ids for all objects.

    Count => GET https://operations.cropwise.com/api/v3/OBJECTS/count — get the number of all objects.

    Single Resource => GET https://operations.cropwise.com/api/v3/OBJECT/ID — get one object by ID.

    Create Resource => POST https://operations.cropwise.com/api/v3/OBJECTS — create new object.

    Update Resource => PUT/PATCH https://operations.cropwise.com/api/v3/OBJECTS/ID — update object by ID.

    Delete Resource => DELETE https://operations.cropwise.com/api/v3/OBJECTS/ID — delete object by ID.

    Changes => GET https://operations.cropwise.com/api/v3/OBJECT/changes — get objects changed in specified period.

    Changes Ids => GET https://operations.cropwise.com/api/v3/OBJECT/changes_ids — get list of ids for objects changed in specified period.

    Mass Request => POST https://operations.cropwise.com/api/v3/OBJECT/mass_request — get the big number of objects by posting the list of ids.

Useful tools

    Postman (https://www.getpostman.com) — multi-platform REST client for API testing.

    Paw (https://paw.cloud) - beautiful (but MacOS only) REST client.

Important notice! — read before start using API

    You should add HTTP Header Content-Type: application/json for all POST and PUT requests. Else, request would be dropped.

    You could add HTTP Header Accept-Encoding: gzip. In this case server would compress responses, that dramatically reduce traffic usage (up to 5 times) and response time. Higly recommended option, especially for mobile devices.

    Cropwise Operations Platform API works only via HTTPS (SSL). Important! —inle check that you use https:// in all requests (especially in Authorization request). Request to http:// would be redirected to https:// automatically, but data in request (access token) would be unsecured and potentially could be stolen.

    If you find bugs or broken documentation — feel free to send email to info@cropio.com.

    In case of wrong request or data, API gives you response with HTTP Error Code and detailed error description (if available). Please read it carefully.

    Naming convention for OBJECT in requests: you need to use plural object name in snake_case:

    https://operations.cropwise.com/api/v3/fields

    https://operations.cropwise.com/api/v3/agro_operations

    https://operations.cropwise.com/api/v3/machine_task_field_mapping_items

Authentication

User should make Login action and obtain USER_API_TOKEN token that required for all next requests. USER_API_TOKEN is a string, that should be added for all request to Cropwise Operations Platform API.

There are 2 ways how USER_API_TOKEN could be added to request.

    Preferred way. Add X-User-Api-Token: USER_API_TOKEN HTTP Header for each request.

    Add ?user_api_token=USER_API_TOKEN parameter to URL for each request. Example: /api/v3/fields?user_api_token=USER_API_TOKEN.

These 2 ways are equal, but first way via adding HTTP Header is preferred, as it doesn't require to change request URL.
Login

Login action needs following attributes:

    email — User email (same as used for Cropwise Operations Platform web-site login).

    password — User password.

Login request
200 OK
Basic Cropwise Operations Platform API agreements
JSON format for list of resources

When you get list of resources making GET /api/v3/resource_name, it would be in next form:

    { 
        "data":
            [ 
                {...},
                {...},
                ...
            ],
        "meta": {
            "request" : {
                "server_time" : "2015-02-04T17:13:21+02:00",
                "limit" : null,
                "from_id" : 0 
            },
            "response" : {
                "limit" : 1000,
                "obtained_records" : 5,
                "last_record_id" : 5,
                "first_record_id" : 1
            }
        }
    }

Array data is the array of resources as JSON-objects. meta object describes metadata and contains two objects. request that represents user request contains the next fields:

    server_time - when server obtains request

    limit - requested number of records. All resources have default (maximal) limit (mostly 1000 records per request). You can specify limit between 0 and default limit: /api/v3/resources_name?limit=1. If no value is specified or specified limit is greater then maximal, default value will be selected. When you miss limit in url-query null will be returned in this attribute.

    from_id - specified offset in request: /api/v3/resources_name?from_id=0. If no from_id specified 0 will be returned.

Object response - represents server response:

    limit - limit selected by server: specified in request or maximal.

    obtained_records - the number of records in data.

    first_record_id - id of the first record in returned set.

    last_record_id - id of the last record in the set.

JSON format for ids list

When you make the following request GET /api/v3/resource_name/ids, it would be in next form:

    {
        "data" : [
            1,
            2,
            3,
            4,
            5
        ],
        "meta" : {
            "request" : {
                "server_time" : "2015-02-04T19:16:12+02:00"
            },
            "response" : {
                "last_record_id" : 5,
                "obtained_records" : 5,
                "first_record_id" : 1
            }
        }
    }

Array data is the list of ids for resources. meta object describes metadata and contains two objects. request that represents user request contains the next fields:

    server_time - when server obtain request

Object response - represents server response:

    obtained_records - the number of records in data.

    first_record_id - id of the first record in returned set.

    last_record_id - id of the last record in the set.

JSON format for external_ids list

This method supports only when model has external_id field. When you make the following request GET /api/v3/resource_name/external_ids, it would be in next form:

    {
        "data" : [
            1,
            2,
            3,
            4,
            5
        ],
        "meta" : {
            "request" : {
                "server_time" : "2015-02-04T19:16:12+02:00"
            },
            "response" : {
                "last_record_external_id" : 5,
                "obtained_records" : 5,
                "first_record_external_id" : 1
            }
        }
    }

Array data is the list of external_ids for resources. meta object describes metadata and contains two objects. request that represents user request contains the next fields:

    server_time - when server obtain request

Object response - represents server response:

    obtained_records - the number of records in data.

    first_record_external_id - external_id of the first record in returned set.

    last_record_external_id - external_id of the last record in the set.

JSON format for single resource

When you a single resources making GET /api/v3/resource_name/ID, it would be in next form:

    {
        "data" : {
            "attr1" : "value",
            "attr2" : "value2",
            ...
        }
    }

Response contains the list of attributes wrapped in object data. If access denied API will return HTTP code 403 Forbidden
JSON format for list of changed resources

When you get list of resources making GET /api/v3/resource_name/changes, it would be in next form:

    { 
        "data":
            [ 
                {...},
                {...},
                ...
            ],
        "meta": {
            "request" : {
                "server_time" : "2015-02-04T17:13:21+02:00",
                "limit" : null,
                "from_time" : "2015-02-03T17:22:55+02:00",
                "to_time" : "2015-02-04T17:22:55+02:00"
            },
            "response" : {
                "limit" : 1000,
                "obtained_records" : 5,
                "first_record_time" : "2015-02-04T16:23:34+02:00",
                "last_record_time" : "2015-02-04T15:45:42+02:00"
            }
        }
    }

Array data contains array of resources as JSON-objects. meta object describes metadata and contains two objects. request that represents user request contains the next fields:

    server_time - when server obtain request

    limit - requested number of records. All resources have default (maximal) limit (mostly 1000 records per request). You can specify limit between 0 and default limit: /api/v3/resources_name?limit=1. If no value is specified or specified limit is greater then maximal, default value will be selected. When you miss limit in url-query null will be returned in this attribute.

    from_time - request records changed later then specified date.

    to_time - request records changed earlier then specified date.

Object response - represents server response:

    limit - limit selected by server: specified in request or maximal.

    obtained_records - the number of records in data.

    first_record_time - time of the first record in returned set.

    last_record_time - time of the last record in the set.

JSON format for list of changed resources ids

When you get list of resources making GET /api/v3/resource_name/changes_ids, it would be in next form:

    { 
        "data":
            [ 
                {
                  "id" : 2,
                  "updated_at" : "2015-02-04T15:49:57+02:00"
                },
                {
                  "id" : 1,
                  "updated_at" : "2015-02-04T15:45:42+02:00"
                }
                ...
            ],
        "meta": {
            "request" : {
                "server_time" : "2015-02-04T17:13:21+02:00",
                "from_time" : "2015-02-03T17:22:55+02:00",
                "to_time" : "2015-02-04T17:22:55+02:00"
            },
            "response" : {
                "obtained_records" : 5,
                "first_record_time" : "2015-02-04T16:23:34+02:00",
                "last_record_time" : "2015-02-04T15:45:42+02:00"
            }
        }
    }

Array data contains araray of objects with two fields:

    id - changed object id

    updated_at - object updation date

meta object describes metadata and contains two objects. request that represents user request contains the next fields:

    server_time - when server obtain request

    from_time - request records changed later then specified date.

    to_time - request records changed earlier then specified date.

Object response - represents server response:

    obtained_records - the number of records in data.

    first_record_time - time of the first record in returned set.

    last_record_time - time of the last record in the set.

JSON format for resource creation

When you create object with POST /api/v3/resource_name with request body in JSON:

    {
        "data": {
            "attr1": "value for attr1",
            "attr2": "value for attr2",
            ...
        }
    }

API v3 returns if creation was successful:

    HTTP code 201 Created

    JSON representation of object like GET request for single resource.

If some something was wrong:

    HTTP code 403 Forbidden if object creation forbidden for current user.

    HTTP code 422 Unprocessable Entity if something was wrong with JSON-request or attributes

    JSON structure with errors description and attribute name that refers to this error.

Errors structure example:

    {
        "errors" : {
            "attr1" : [
                "error 1 description",
                "error 2 description"
            ]
        }
    }

JSON format for resource updation

When you update object with PUT /api/v3/resource_name/ID with request body in JSON:

    {
        "data": {
            "attr1": "new value for attr1",
            "attr2": "new value for attr2",
            ...
        }
    }

API v3 returns if creation was successful:

    HTTP code 200 OK

    JSON representation of object like GET request for single resource.

If some something was wrong:

    HTTP code 403 Forbidden if object exists but it's updation is not allowed for current user.

    HTTP code 404 Not Found if object does not exist.

    HTTP code 422 Unprocessable Entity if something was wrong with JSON-request or attributes

    JSON structure with errors description and attribute name that refers to this error.

Errors structure example:

    {
        "errors" : {
            "attr1" : [
                "error 1 description",
                "error 2 description"
            ]
        }
    }

JSON format for resource deletion

When you destroy object with DELETE /api/v3/resource_name/ID API v3 returns:

    HTTP code 403 Forbidden if object was destroyed

    HTTP code 302 Found if object exists but it's deletion is not allowed for current user.

    HTTP code 404 Not Found if object does not exist.

JSON format for requesting of big number of objects

This method allows to get big number of objects with submitting big list of ids with POST.

When you get a big list of objects by submitting POST /api/v3/resource_name/mass_request with:

    {
        "data": [1,2,...]
    }

Response will be the next form:

    { 
        "data":
            [ 
                {...},
                {...},
                ...
            ],
         "meta" : {
            "request" : {
                "server_time" : "2015-02-04T20:07:03+02:00",
                "from_id" : null,
                "limit" : null
            },
            "response" : {
                "limit" : null,
                "last_record_id" : 2,
                "obtained_records" : 2,
                "first_record_id" : 1
            }
        }
    }

Array data is the array of resources as JSON-objects. meta object describes metadata and contains two objects. request that represents user request contains the next fields:

    server_time - when server obtains request

    other fields are nulls

Object response - represents server response:

    limit - always null.

    obtained_records - the number of records in data.

    first_record_id - id of the first record in returned set.

    last_record_id - id of the last record in the set.

Keep your id's in Cropwise Operations Platform objects

Some objects have external_id - string field. You can store in this field id from your system. Than you can get object from Cropwise Operations Platform with yours id by request /api/v3/resource_name/external_id:your_id
Conditions in requests to filter data
Filtering with strong (equal) conditions

There is ability to filter requested data by some condition. For each object in documentation you will have a list of fields to use in request.

For example: object FieldShape can be filtered by field_id, so you can do request /api/v3/field_shapes?field_id=566
Filtering with comparison conditions

Comparison conditions are available only for some objects. If some object has comparison filters you can use comparison operators like:

    eq - it means ==

    gt_eq - it means >=

    gt - it means >

    lt_eq - it means <=

    lt - it means <

This operators should be added to parameter name as postfix.

Note:

date values should be passed in format YYYY-MM-DD

datetime values should be passed in format YYYY-MM-DDTHH:MM:SS

For example:

object MachineTask can be filtered by start_time, so you can do request /api/v3/machine_tasks?start_time_gt_eq=2016-12-09T11:00:00

object MachineTask can be filtered by season, so you can do request /api/v3/machine_tasks?season_gt=2016
Sorting

Sorting available for all objects. Base sorting attributes are id, created_at, updated_at. For additional options look for specific reference points.

Note:

Sort parameter value is combined from 2 parts:

    Attribute name

    Sort direction

Available sort directions:

    asc - From smallest to biggest.

    desc - From biggest to smallest.

Parameter name:

    sort_by

Parameter value examples:

    id_desc

    updated_at_asc

For example:

To obtain the last 10 Field objects: /api/v3/fields?limit=10&sort_by=created_at_desc or /api/v3/fields?limit=10&sort_by=id_desc
Workflow example
Resources
URI Parameterslimit	

Retrieve limit or less number of records. DefaultValue 10000
from_id (optional, number, `1`) ... Retrieve only records with id >= **from_id**	DefaultValue 1000
Get collection of Resource

Retrieve all records sorted by ID (ask)
200 OK
Resources ids
Get collection of Resources ids

Retrieve array of ids for records
200 OK
Creation of Resource
Create Resource
201 Created
Single Resource
Get single Resource

Retrieve array of ids for records
200 OK
Update Resource

Update record
200 OK
Destroy Resource

Delete record
204 No Content
Changed objects
URI Parameterslimit	

Retrieve limit or less number of records
from_time (optional, datetime, `2015-02-03T22:25:32+02:00`) ... Retrieve only records with update_at >	
to_time (optional, datetime, `2015-02-04T22:25:32+02:00`) ... Retrieve only records with update_at >	
Get changed Resource

Get all records changed between specified dates
200 OK
Changed records ids
URI Parametersfrom_time (optional, datetime, `2015-02-03T22:25:32+02:00`) ... Retrieve only records with update_at >	
to_time (optional, datetime, `2015-02-04T22:25:32+02:00`) ... Retrieve only records with update_at >	
Get changed objects ids

Get ids for all records changed between specified dates
200 OK
Mass Request
Get big amount of records by ids
200 OK
AdminRegions

operations.cropwise.com/api/v3/admin_regions
AdminRegions relations

    AdminRegion has many Fields

AdminRegions has next parameters

    (readonly) id — Cropwise Operations Platform ID of AdminRegion

    (readonly) name — name of AdminRegion

    (readonly) country_code — country_code of AdminRegion

    (readonly) region_type — region_type

    (readonly) admin_level — admin_level of AdminRegion

    (readonly) subdivision_code — subdivision_code

    (readonly) simplified_shape_json — series of attributes that contain simplified shape in different formats (see Shape Formats below)

    (readonly) created_at

    (readonly) updated_at

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Comparison filters by (for more info see)

created_at, updated_at
AutomaticAlerts

operations.cropwise.com/api/v3/automatic_alerts
AutomaticAlerts relations

    AutomaticAlert has many Alerts

    AutomaticAlert belongs to AlertType

Alert has next parameters

    (readonly) id — Cropwise Operations Platform ID of AutomaticAlert

    (readonly) alert_type_id — ID of AlertType

    (readonly) automatic_alert_type — type of automatic alert

    (readonly) automatic_alert_subtype — subtype of automatic alert

    (readonly) name — name of automatic alert

    (readonly) active - boolean, automatic alert enabled flag

    (readonly) description

    (readonly) alert_settings - JSON with automatic alert settings

    (readonly) scheduled - boolean, scheduling flag

    (readonly) schedule_start_time - the time from which the automatic alarm starts to work

    (readonly) schedule_end_time - time when the automatic alarm stops working

    (readonly) time_zone

    (readonly) created_at

    (readonly) updated_at

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

alert_type_id, automatic_alert_type, automatic_alert_subtype, active, scheduled
Comparison filters by (for more info see)

created_at, updated_at
Alerts

operations.cropwise.com/api/v3/alerts
Alert relations

    Alert belongs to AlertType

    Alert belongs to alertable objects (Machine Implement AdditionalObject Field)

    Alert belongs to AutomaticAlert

    Alert belongs to User (generated_by)

    Alert belongs to User (created_by_user)

    Alert has many protected_documents

    Alert has many spread_plant_threats

    Alert has many alert_responsible_user_assignments

Alert has next parameters

    (readonly) id — Cropwise Operations Platform ID of Alert

    (readonly) alert_type_id — ID of AlertType

    (readonly) alertable_id — ID of alertable object

    (readonly) alertable_type — type of alertable object

    (readonly) event_start_time — the time of the beginning of the event that led to the occurrence of an alarm

    (readonly) status - status of alert, could be 'open', 'closed'

    (readonly) description

    (readonly) responsible_person_id - ID of responsible User from Cropwise Operations Platform

    (readonly) created_by_user_id - ID of Cropwise Operations Platform User, whom created alert

    (readonly) event_stop_time - time when the event stopped

    (readonly) alert_closed_at - time when the event closed

    (readonly) automatic_alert_id - ID of AutomaticAlert

    (readonly) system_info - may contain different data, for example, field_ids id of fields on which was violation

    (readonly) created_at

    (readonly) updated_at

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

alert_type_id, alertable_type, alertable_id, responsible_person_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Additional info

Alert support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
AlertTypes

operations.cropwise.com/api/v3/alert_types
AlertTypes relations

    AlertType has many Alerts

    AlertType has many AutomaticAlerts

AlertType has next parameters

    (readonly) id — Cropwise Operations Platform ID of AlertType

    alert_type — name for grouping alert types

    name — name of alert type

    priority — priority of created alerts. Could be 'low', 'mid', 'high'

    description

    additional_info

    archived - boolean. The types of alarms from the archive will not be displayed in the alarm selection lists

    (readonly) created_at

    (readonly) updated_at

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

AdditionalObjects

operations.cropwise.com/api/v3/additional_objects
AdditionalObject relations

    AdditionalObject belongs to one FieldGroup. Required.

AdditionalObject has next parameters

    (readonly) id — Cropwise Operations Platform ID of AdditionalObject.

    field_group_id — FieldGroup ID (AdditionalObject belongs to). Required.

    name — Name.

    object_type — Type of object. Could be any string. Example: 'Road', 'Building', etc.

    geometry_type — Geometry type of objects. Could be one of: point, line, polygon.

    (readonly) calculated_area — Area of object (defined only for polygons). Calculated automatically.

    administrative_area_name

    subadministrative_area_name

    (readonly) geo_json — Simplified shape in GeoJSON format.

    (writeonly) shape_json - attribute for setting shape for Additional object. (in GeoJSON format)

    additional_info — Additional info.

    description — Some description.

    locality.

    (readonly) additional — JSON with visual style for geometry.

    (writeonly) icon — one of: cow, danger, default, elevator, farm, house, office. For points only.

    (writeonly) point_size — point size (diameter). For points only.

    (writeonly) point_color — point color (in HEX, eg. #00FF00). For points only.

    (writeonly) line_width— line width. For lines only.

    (writeonly) line_color — line color (in HEX, eg. #00FF00). For lines only.

    (writeonly) polygon_color — polygon color (in HEX, eg. #00FF00). For polygons only.

    (writeonly) polygon_opacity — polygon opacity (from 0.0 to 1.0). For polygons only.

    (writeonly) polygon_stroke_width — polygon stroke width. For polygons only.

    (writeonly) polygon_stroke_opacity — polygon stroke opacity (from 0.0 to 1.0). For polygons only.

    (readonly) created_at

    (readonly) updated_at

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

AdditionalInventoryUnitAssignments

operations.cropwise.com/api/v3/additional_inventory_unit_assignments
AdditionalInventoryUnitAssignment relations

    AdditionalInventoryUnitAssignment belongs to one polymorphic inventoryable entity Seed, Chemical, Fertilizer, SparePart, FuelType, WhItem.

    AdditionalInventoryUnitAssignment belongs to one additional_inventory_unit (Unit).

AdditionalInventoryUnitAssignment has next parameters

    (readonly) id — Cropwise Operations Platform ID of AdditionalInventoryUnitAssignment.

    inventoryable_type — Type of the associated inventoryable entity. One of: Seed, Chemical, Fertilizer, SparePart, FuelType, WhItem.

    inventoryable_id — ID of the associated inventoryable entity. Required.

    additional_inventory_unit_id — ID of the associated additional inventory unit (Unit).

    coefficient_to_base_unit — Coefficient for conversion to base unit.

    external_id — External identifier for the record.

    (readonly) created_at

    (readonly) updated_at

Acceptable methods

    Resources Collection — Get list of AdditionalInventoryUnitAssignments

    Ids — Get list of IDs for AdditionalInventoryUnitAssignments

    Single Resource — Get single AdditionalInventoryUnitAssignment by ID

    Create Resource — Create new AdditionalInventoryUnitAssignment

    Update Resource — Update existing AdditionalInventoryUnitAssignment

    Delete Resource — Delete existing AdditionalInventoryUnitAssignment

    Changes — Get changes of AdditionalInventoryUnitAssignments

    Changes Ids — Get changed IDs

    Mass Request — Batch operations for AdditionalInventoryUnitAssignments

Filtering

    Supports filtering by equality on fields:
    id, inventoryable_type, inventoryable_id, additional_inventory_unit_id, external_id

    Supports date comparison filtering on:
    created_at, updated_at

Sorting

    Supports sorting by:
    id, created_at, updated_at

AgriWorkPlan

operations.cropwise.com/api/v3/agri_work_plans
AgriWorkPlan relations

    AgriWorkPlan belongs to WorkType. Required.

    AgriWorkPlan belongs to AgroRecommendation. Optional.

    AgriWorkPlan belongs to Season. Optional.

    AgriWorkPlan has many AgroOperations

    AgriWorkPlan has many AgriWorkPlanApplicationMixItems

    AgriWorkPlan has many MachineWorkPlans

AgriWorkPlan object has next attrbiutes

    (readonly) id - Cropwise Operations Platform ID of AgroOperation

    status - status of work plan: 'plan', 'done'

    work_type — LEGACY! Use work_type_id instead

    work_subtype — LEGACY! Use work_type_id instead

    groupable_type - type of objects for which a plan is created ('GroupFolder','FieldGroup')

    groupable_id - Cropwise Operations Platform ID of object for which a plan is created

    season - the season (year in format "yyyy") of the plan

    planned_start_date - planned start date of agri work plan

    planned_end_date - planned end date of agri work plan

    additional_info - your system info

    description - description

    planned_water_rate - planned water rate (l/ha)

    planned_rows_spacing - planned row spacing (cm.)

    planned_depth - planned depth (cm.)

    planned_speed - planned speed (km/h)

    responsible_person_id - Cropwise Operations Platform ID of responsible User

    agro_recommendation_id - Cropwise Operations Platform ID of AgroRecommendation

    current_season_id - Cropwise Operations Platform ID of Season

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Filters by

id, groupable_id, groupable_type, work_type_id, status, season, planned_start_date, planned_end_date, created_by_user_id, additional_info, description, responsible_person_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
AgriWorkPlanApplicationMixItems

operations.cropwise.com/api/v3/agri_work_plan_application_mix_items
AgriWorkApplicationMixItem relations

    AgriWorkApplicationMixItem belongs to applicable (Seed, Fertilizer, Chemical). Required.

    AgriWorkApplicationMixItem belongs to AgriWork

AgriWorkApplicationMixItem object has next attributes

    (readonly) id - Cropwise Operations Platform ID of AgriWorkApplicationMixItem

    agri_work_plan_id - Cropwise Operations Platform ID of related AgriWorkPlan

    applicable_type - Cropwise Operations Platform type of applicable object ('Seed', 'Fertilizer', 'Chemical')

    applicable_id - Cropwise Operations Platform ID of applicable object

    amount - amount of application

    additional_info - your system information

    (readonly) rate - rate of application

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, agri_work_plan_id, applicable_id, applicable_type
AgronomistAssignments

operations.cropwise.com/api/v3/agronomist_assignments
AgronomistAssignment relations

    AgronomistAssignment belongs to User

    AgronomistAssignment belongs to FieldGroup

AgronomistAssignment object has next attributes

    (readonly) id - Cropwise Operations Platform ID of AgronomistAssignment

    user_id - Cropwise Operations Platform ID of related User

    field_group_id - Cropwise Operations Platform ID of related FieldGroup

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, user_id, field_group_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
AgronomistFields

operations.cropwise.com/api/v3/agronomist_fields
AgronomistField relations

    AgronomistFields belongs to User

    AgronomistFields belongs to Field

AgronomistFields object has next attributes

    (readonly) id - Cropwise Operations Platform ID of AgronomistAssignment

    user_id - Cropwise Operations Platform ID of related User

    field_id - Cropwise Operations Platform ID of related Field

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, user_id, field_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
AgroOperations

operations.cropwise.com/api/v3/agro_operations
AgroOperation relations

    AgroOperation belongs to Field. Required.

    AgroOperation belongs to WorkType. Required.

    AgroOperation belongs to AgroRecommendation. Optional.

    AgroOperation belongs to HistoryItem.

    AgroOperation has many ApplicationMixItems.

    AgroOperation has many MachineTasks.

AgroOperation object has next atrributes

    (readonly) id — Cropwise Operations Platform ID of AgroOperation

    field_id — Cropwise Operations Platform ID of related Field

    agri_work_plan_id — Cropwise Operations Platform ID of related AgriWorkPlan

    agro_recommendation_id - Cropwise Operations Platform ID of AgroRecommendation

    operation_type — LEGACY! Use work_type_id instead.

    operation_subtype — LEGACY! Use work_type_id instead.

    work_type_id - ID of WorkType.

    responsible_user_ids - an array of Users Cropwise Operations Platform IDs of responsible for AgroOperation

    operation_number — number of operation.

    planned_area — planned area of agro operation

    completed_area — completed area of agro operation

    harvested_weight - harvest weight for agro operation

    status - status of operation: 'planned', 'in_progress', 'done', 'canceled'

    planned_start_date - planned start date of agro operation

    planned_end_date - planned end date of agro operation

    (readonly) completed_date - actual end date of agro operation (deprecated, completed_datetime should be used)

    actual_start_datetime - actual start time of agro operation

    completed_datetime - actual end time of agro operation

    season - the season (year in format "yyyy") of work

    planned_water_rate - planned water rate (l/ha)

    fact_water_rate - fact water rate (l/ha)

    planned_rows_spacing - planned row spacing (cm.)

    planned_depth - planned depth (cm.)

    planned_speed - planned speed (km/h)

    applications_type - applications_type: 'ao_applications', 'mtfmi_applications'. When value is mtfmi_applications the ApplicationMixItem could be added to MachineTaskFieldMappingItem. Available only for companies with use_mtfmi_applications setting enabled (contact support to enable).

    (readonly) completed_percents - the percentage of completion of the agro operation

    (readonly) partially_completed - is this agro operation is partially completed (true/false)

    (readonly) partially_completed_manually_defined_area - actual complited area

    (readonly) covered_area - alias to covered_area_by_track

    (readonly) covered_area_by_track - actual covered area by machines (excluding intersections)

    (readonly) machine_work_area - area covered by machine (track length * width of implement)

    (readonly) fuel_consumption - fuel consumption (l.)

    (readonly) fuel_consumption_per_ha - fuel consumption rate (l/ha)

    additional_info - your system information

    description - description

    protein_content - protein content

    oil_content - oil content

    humidity - humidity

    harmful_admixture - harmful admixture

    garbage_admixture - garbage admixture

    grain_admixture - grain admixture

    oil_acid_number - oil acid number

    marketable_weight - marketable weight

    (readonly) application_mix_items - array of related ApplicationMixItems ids

    external_id - a string field for storing id of the element from an external system

    history_item_id - Cropwise Operations Platform ID of related HistoryItem

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

    locked_to_edit - prohibition of editing sign: 'true', 'false'

    (readonly) locked_at - the time when editing was disabled

    additional_product_type - additional product type (straw, tops, stems, other)

    additional_product_weight - additional product weight

    application_by_days - an agro operation has an application by days (true / false)

Subtypes:

    'soil': 'discing', 'plowing', 'cultivation', 'subsoiling', 'harrowing' or 'rolling'

    'application': 'spraying', 'spreading' or 'sowing'

    for 'harvesting' and 'other' leave empty or set any value.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_id, status, season, work_type_id, field_shape_id, locked_to_edit, external_id, agri_work_plan_id, applications_type, created_at, updated_at
Comparison filters by (for more info see)

planned_start_date, planned_end_date, actual_start_datetime, completed_datetime, season, created_at, updated_at, locked_at
Additional info

Agro Operations support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
AgroOperations/v3a

operations.cropwise.com/api/v3a/agro_operations
AgroOperation relations

    AgroOperation belongs to Field. Required.

    AgroOperation belongs to WorkType. Required.

    AgroOperation has many ApplicationMixItems.

    AgroOperation has many MachineTasks.

AgroOperation object has next atrributes

    (readonly) id — Cropwise Operations Platform ID of AgroOperation

    field_id — Cropwise Operations Platform ID of related Field

    field_shape_id - - ID of FieldShape

    agri_work_plan_id — Cropwise Operations Platform ID of related AgriWorkPlan

    work_type_id - ID of WorkType.

    responsible_user_ids - an array of Users Cropwise Operations Platform IDs of responsible for AgroOperation

    operation_number — number of operation.

    planned_area — planned area of agro operation

    completed_area — completed area of agro operation

    harvested_weight - harvest weight for agro operation

    status - status of operation: 'planned', 'in_progress', 'done', 'canceled'

    planned_start_date - planned start date of agro operation

    planned_end_date - planned end date of agro operation

    (readonly) completed_date - actual end date of agro operation (deprecated, completed_datetime should be used)

    actual_start_datetime - actual start time of agro operation

    completed_datetime - actual end time of agro operation

    season - the season (year in format "yyyy") of work

    custom_name - custom name of AgroOperation.

    planned_water_rate - planned water rate (l/ha)

    fact_water_rate - fact water rate (l/ha)

    planned_rows_spacing - planned row spacing (cm.)

    planned_depth - planned depth (cm.)

    planned_speed - planned speed (km/h)

    (readonly) completed_percents - the percentage of completion of the agro operation

    (readonly) partially_completed - is this agro operation is partially completed (true/false)

    (readonly) partially_completed_manually_defined_area - actual complited area

    (readonly) covered_area - alias to covered_area_by_track

    (readonly) covered_area_by_track - actual covered area by machines (excluding intersections)

    (readonly) machine_work_area - area covered by machine (track length * width of implement)

    (readonly) fuel_consumption - fuel consumption (l.)

    (readonly) fuel_consumption_per_ha - fuel consumption rate (l/ha)

    additional_info - your system information

    description - description

    (readonly) application_mix_items - array of related ApplicationMixItems ids

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Subtypes:

    'soil': 'discing', 'plowing', 'cultivation', 'subsoiling', 'harrowing' or 'rolling'

    'application': 'spraying', 'spreading' or 'sowing'

    for 'harvesting' and 'other' leave empty or set any value.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_id, status, season, work_type_id, field_shape_id, locked_to_edit, external_id, agri_work_plan_id, applications_type, created_at, updated_at
Comparison filters by (for more info see)

planned_start_date, planned_end_date, actual_start_datetime, completed_datetime, season, created_at, updated_at, locked_at
Additional info

Agro Operations support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
AgroRecommendations

operations.cropwise.com/api/v3/agro_recommendations
AgroRecommendation relations

    AgroRecommendation belongs to FieldGroup or GroupFolder as an groupable. Required

    AgroRecommendation belongs to User as an consultant. Required

    AgroRecommendation belongs to FieldScoutReport. Optional

    AgroRecommendation has many AgroOperations or has one AgriWorkPlan

AgroRecommendation object has next atrributes

    (readonly) id — Cropwise Operations Platform ID of AgroRecommendation

    groupable_type - type of objects for which a plan is created ('GroupFolder', 'FieldGroup')

    groupable_id - Cropwise Operations Platform ID of object for which a plan is created

    consultant_id - Cropwise Operations Platform ID of User

    field_scout_report_id - Cropwise Operations Platform ID of FieldScoutReport

    idempotency_key - The idempotency key transmitted during the request, if any

    external_id - ID for external system (string, must be UNIQUE)

    additional_info - some additional info from user

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Sorting by (for more info see)

id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Additional info

After creating a AgroRecommendation, you need to create AgroOperation or AgriWorkPlan with agro_recommendation_id of the created recommendation.
ApplicationMixItems

operations.cropwise.com/api/v3/application_mix_items
ApplicationMixItem relations

    ApplicationMixItem belongs to AgroOperation. Required.

    ApplicationMixItem belongs to applicable (Seed, Chemical, Fertilizer). Required.

ApplicationMixItem object has next attributes

    (readonly) id - Cropwise Operations Platform ID of ApplicationMixItem

    agro_operation_id - Cropwise Operations Platform ID of AgroOperation

    applicable_id - Cropwise Operations Platform ID applicable

    applicable_type - Cropwise Operations Platform type of applicable: "Seed", "Fertilizer", "Chemical"

    planned_amount - planned amount of application

    fact_amount - actual amount of application

    planned_rate - planned rate of application

    fact_rate - actual rate of application

    unit_id - ID of the unit of measurement. See the Unit API for available units. Must reference either the base inventory unit of the applicable (base_inventory_unit_id) or an additional unit explicitly assigned to the applicable via AdditionalInventoryUnitAssignments

    custom_fact_area - fact area for current application

    use_custom_fact_area - use custom fact area (true/false)

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Important!

planned_amount & fact_amount have priority over planned_rate & fact_rate. If you define both amount & rates — amount will be saved, but rates would be recalculated internally based on amount and area.

You can't redefine rates separately if amounts defined.

But, when creating new ApplicationMixItem you can define only rates, and right amounts would be calcluated automatically.
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, agro_operation_id, applicable_id, applicable_type, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Additional info

Application Mix Item support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
ApplicationMixItemByDays

operations.cropwise.com/api/v3/application_mix_item_by_days
ApplicationMixItemByDays relations

    ApplicationMixItemByDays belongs to AgroOperation. Required.

    ApplicationMixItemByDays belongs to applicable (Seed, Chemical, Fertilizer). Required.

ApplicationMixItemByDays object has next attributes

    (readonly) id - Cropwise Operations Platform ID of ApplicationMixItemByDays

    application_time - Application time

    agro_operation_id - Cropwise Operations Platform ID of AgroOperation

    applicable_id - Cropwise Operations Platform ID applicable

    applicable_type - Cropwise Operations Platform type of applicable: "Seed", "Fertilizer", "Chemical"

    planned_amount - planned amount of application

    fact_amount - actual amount of application

    planned_rate - planned rate of application

    fact_rate - actual rate of application

    planned_water_rate - planned water rate for this application

    fact_water_rate - fact water rate for this application

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Important!

planned_amount & fact_amount have priority over planned_rate & fact_rate. If you define both amount & rates — amount will be saved, but rates would be recalculated internally based on amount and area.

You can't redefine rates separately if amounts defined.

But, when creating new ApplicationMixItemByDays you can define only rates, and right amounts would be calcluated automatically.
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, application_time, agro_operation_id, applicable_id, applicable_type, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at

AllowedToCrops

operations.cropwise.com/api/v3/allowed_to_crops
AllowedToCrops relations

    AllowedToCrops belongs to Crop

    AllowedToCrops belongs to applicable (Chemical, WorkType). Required.

AllowedToCrops has next attributes

    (readonly) id - Cropwise Operations Platform ID of AllowedToCrops

    (immutable) crop_id - Cropwise Operations Platform ID of Crop

    (immutable) applicable_type - Cropwise Operations Platform type of applicable object ('Chemical', 'WorkType')

    (immutable) applicable_id - Cropwise Operations Platform ID of applicable object

    external_id - a string field for storing id of the element from an external system

    additional_info - your system information

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, work_type_id, applicable_id, applicable_type, external_id
Comparison filters by (for more info see)

created_at, updated_at
AutomaticScoutingTask

operations.cropwise.com/api/v3/automatic_scouting_tasks
AutomaticScoutingTasks relations

    AutomaticScoutingTasks belongs to ScoutReportTemplate

    AutomaticScoutingTasks has one AutomaticScoutingTaskDateCondition

    AutomaticScoutingTasks has one AutomaticScoutingTaskAgroOperationCondition

    AutomaticScoutingTasks has one AutomaticScoutingTaskNdviChangesCondition

    AutomaticScoutingTasks has many ScoutingTasks

    AutomaticScoutingTasks has many AutomaticScoutingTaskCropAssignments

    AutomaticScoutingTasks has many AutomaticScoutingTaskGroupFolderAssignments

    AutomaticScoutingTasks has many AutomaticScoutingTaskFieldGroupAssignments

    AutomaticScoutingTasks has many AutomaticScoutingTaskFieldAssignments

    AutomaticScoutingTasks has many Crops (through AutomaticScoutingTaskCropAssignments)

    AutomaticScoutingTasks has many GroupFolders (through AutomaticScoutingTaskGroupFolderAssignments)

    AutomaticScoutingTasks has many FieldGroups (through AutomaticScoutingTaskFieldGroupAssignments)

    AutomaticScoutingTasks has many Fields (through AutomaticScoutingTaskFieldAssignments)

AutomaticScoutingTasks has next attributes

    (readonly) id - Cropwise Operations Platform ID of AutomaticScoutingTask

    conditions_type - conditions type can be date, agro_operation, ndvi_changes

    name - name

    description - description

    (readonly) conditions - hash of conditions data parameters with values.

    scout_report_template_id - Cropwise Operations Platform ID of related ScoutReportTemplate

    season - the season (year in format "yyyy")

    active - boolean, is record is active

    description_for_scouting_task - description for scouting task

    task_duration_days - task duration in days

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Avatar

operations.cropwise.com/api/v3/avatars
Avatar relations

    Avatar has many Machines.

    Avatar has many Implements.

    Avatar has many FuelStations.

Avatar object has next attributes

    avatar_type - type of avatar: 'machine', 'implement', 'fuel_station'

    name - name of avatar

    avatar - avatar object as json

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource - for upload example see Uploading Photo

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Avatar/v3a

operations.cropwise.com/api/v3a/avatars
Avatar relations

    Avatar has many Machines.

    Avatar has many Implements.

    Avatar has many FuelStations.

Avatar object has next attributes

    (readonly) id - Cropwise Operations Platform ID of Avatar

    avatar_type - type of avatar: 'machine', 'implement', 'fuel_station'

    name - name of avatar

    avatar - avatar object as json

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource - for upload example see Uploading Photo

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Chemicals

operations.cropwise.com/api/v3/chemicals
Chemical relations

    Chemical has many ApplicationMixItems as applicable.

    Chemical has many AgriWorkApplicationMixItems as applicable.

    Chemical has many AllowedToСrops as applicable.

Chemical object has next attributes

    (readonly) id - Cropwise Operations Platform ID of Chemical

    name - name of chemical

    chemical_type - type of chemical: 'acaricide', 'adjuvant', 'attractant', 'bactericide', 'biologic_supplements', 'defoliants_desiccants', 'disinfectant', 'fumigant', 'fungicide', 'growth_regulator', 'herbicide', 'immunity_enhancer', 'insecticide', 'microbiological_agent', 'molyuscocid', 'nematicides', 'nutrients', 'repellent', 'resistance_inductor', 'rodenticide', 'seed_treatment', 'pheromones', 'defoamer', 'adhesive', 'other'

    units_of_measurement (deprecated) — use base_inventory_unit_id instead. Units of measurement: 'tn', 'g', 'kg', 'liter', 'ml', 'cubic_metre', 'pound', 'ounce', 'pint', 'quart', 'package', 'thousand_pieces', 'million_pieces'

    base_inventory_unit_id - ID of the base unit of measurement. See the Unit API for available units.

    toxicity_class - toxicity class of chemical: 1 - strong toxic, 2 - high toxic, 3 - medium toxic, 4 - low toxic

    action_term - action term of chemical

    action_term_units - action term units of chemical: 'day', 'hour'

    active_substance - chemical's active substances description

    active_substances - list of active substances associated with the chemical

    drug_form - drug form of chemical

    influence_method - influence method of chemical: 'intestinal', 'systemic', 'contact', 'fumigation'

    bees_isolating_recommended_term - in case of toxicity to bees, recommended term of bees isolating

    bees_isolating_recommended_term_units - bees isolating recommended term units: 'day', 'hour'

    additional_info - your system information

    description - description

    sale_term - date of term of sale

    term_of_use - term of use date

    archived - description

    external_id - a string field for storing id of the element from an external system

    wh_item_id - Cropwise Operations Platform ID of WhItem

    wh_item_base_unit_id (deprecated) — use base_inventory_unit_id instead. Cropwise Operations Platform ID of Unit

    manufacturer_name - name of manufacturer

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, chemical_type, description, additional_info, archived, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Additional info

Chemical support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
Chemical use for crops

You can get information about chemical use for crops by operations.cropwise.com/api/v3/chemical/chemical_ID/use_for_crops.

chemical_ID - Cropwise Operations Platform ID of Chemical
Comments

operations.cropwise.com/api/v3/comments
Crop relations

    Comment belongs to User. Required.

    Comment belongs to applicable (FieldScoutReport). Required.

Crop object has next attributes

    (readonly) id - Cropwise Operations Platform ID Crop

    content - content of comment

    user_id - Cropwise Operations Platform ID of User created this comment

    commentable_type - type of objects for which a comment is created ('FieldScoutReport')

    commentable_id - Cropwise Operations Platform ID of object for which a comment is created

    parent_id - Cropwise Operations Platform ID of comment for which a current comment is created

    active - is it comment active (boolean)

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, commentable_id, commentable_type, user_id, active
Sorting by (for more info see)

id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Company

operations.cropwise.com/api/v3/company

This API resource has one access method and returns company profile information.
Company object has next attributes

All parameters are readonly.

    id - Cropwise Operations Platform ID of Company

    name - name of company

    country - country code (ISO 2-letter)

    area_limit - limit of area, ha.

    tenant - tenant name

    logo - links to logo images

    show_seasons - if true user can create multi history items by some year

Company
Company profile request
200 OK
Counterparties

operations.cropwise.com/api/v3/counterparties
Counterparty relations

    Counterpartie has many LandDocuments

Counterparty object has next attributes

    (readonly) id - Cropwise Operations Platform ID of Counterparty

    first_name

    middle_name

    last_name

    phone_number

    passport_code

    email

    passport_issuing_date

    identification_code

    passport_issued_by

    passport_issuing_date_presence

    counterparty_type - natural_person, legal_person, state

    street

    region

    locality

    district

    house_number

    postcode

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, identification_code, counterparty_type, passport_code, external_id
Comparison filters by (for more info see)

created_at, updated_at
Crops

operations.cropwise.com/api/v3/crops
Crop relations

    Crop has many HistoryItems.

    Crop has many Seeds.

    Crop has many Fields.

    Crop has many MachineTasks.

Crop object has next attributes

    (readonly) id - Cropwise Operations Platform ID Crop

    name - name of crop

    short_name - short name of the crop

    standard_name - default names (see blow)

    season_type - type of crop ('spring' or 'winter')

    (readonly) color - color selected for crop in color scheme

    base_crop_id - id of base crop. You can view the data of base crops at http://operations.cropwise.com/api/v3/crop/base_crops_list

    productivity_estimate_crop_name - crop name for yield estimation

    additional_info - your system info

    description - description

    external_id - a string field for storing id of the element from an external system

    hidden - is it hidden (boolean)

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Default names:

    "avena_spring"

    "avena_winter"

    "barley_spring"

    "barley_winter"

    "buckwheat"

    "chickpea"

    "fallow"

    "linum"

    "maize"

    "medicago"

    "oil_seed_raps_spring"

    "oil_seed_raps_winter"

    "millet"

    "papaver"

    "pea"

    "potatoes"

    "rice"

    "rye_spring"

    "rye_winter"

    "sainfoin"

    "sorghum"

    "soya"

    "sudan_grass"

    "sugar_beet"

    "sunflower"

    "triticale_spring"

    "triticale_winter"

    "wheat_spring"

    "wheat_winter"

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, short_name, custom_name, additional_info, description, season_type, external_id, hidden, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Additional info

Crop support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
Custom Fields

operations.cropwise.com/api/v3/custom_fields
CustomField relations

At the moment, custom fields are supported by next entities:

    AgroOperation

    Alert

    ApplicationMixItem

    Chemical

    Crop

    Fertilizer

    Field

    FieldScoutReport

    GpsLogger

    HarvestWeighing

    Implement

    LandDocument

    LandParcel

    Machine

    MachineTask

    Seed

    SparePart

    SoilTest

CustomField has next attributes

    (readonly) id - Cropwise Operations Platform ID of CustomField

    related_model - related model, that will have new custom field (supported entities list)

    human_name - name of the custom field, that will be seen by user in system interface

    name - name of the custom field by which it will be available in system and API. Must start by x_custom

    field_data_type - data type of custom field (see)

    selected_list_items - array of values if field_data_type is select or multi_select

    external_id - external ID

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

CustomField support next field data types

    boolean

    date

    datetime

    float

    integer

    select

    string

    multi_select

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Additional info

In related models custom fields are available by their names which starts by x_custom.
Comparison filters by (for more info see)

created_at, updated_at
DataSourceGpsLoggers

operations.cropwise.com/api/v3/data_source_gps_loggers
DataSourceGpsLogger relations

    DataSourceGpsLogger belongs to GpsLogger

    DataSourceGpsLogger belongs to Machine

DataSourceGpsLogger has next attributes

    (readonly) id - Cropwise Operations Platform ID of DataSourceGpsLogger

    mappable_id - mappable odject id (for example machine_id)

    mappable_type - mappable odject type (for example 'Machine')

    gps_logger_id - id of gps logger

    start_time - start time when we take data from logger for machine

    end_time - end time, can be nil

    additional_info - some additional info from users

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Additional info

Start/End time need to be in range of Start/End time GpsLoggerMappingItem
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, mappable_id, mappable_type, gps_logger_id, no_date_end, start_time, end_time, created_at, updated_at
Comparison filters by (for more info see)

start_time, end_time, created_at, updated_at
DataSourceParameters

operations.cropwise.com/api/v3/data_source_parameters
DataSourceParameters relations

    DataSourceParameters belongs to DataSourceGpsLogger

DataSourceParameters has next attributes

    (readonly) id - Cropwise Operations Platform ID of DataSourceParameters

    (readonly) data_source_gps_logger_id - Cropwise Operations Platform ID of related DataSourceGpsLogger

    (readonly) name - name

    (readonly) name_human - visible name

    (readonly) units_of_measurement - units of measurement for parameter data

    (readonly) value_type - value type

    (readonly) calc_type - calculation type

    (readonly) gps_sensor_name - gps sensor name

    (readonly) calc_formula - calculation formula

    (readonly) key_values_table - key value table for parameter data calculation

    (readonly) description - parameter description

    (readonly) hidden - shows if parameter hidden

    (readonly) presentation_mode - presentation mode

    (readonly) type - parameter type

    (readonly) fuel_consumption_accounting - flag shows if fuel consumption is used for accounting

    (readonly) fuel_flow_sensor_type - type of sensor for fuel flow parameters

    (readonly) settings - parameter settings

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Comparison filters by (for more info see)

created_at, updated_at
DirectionLines

operations.cropwise.com/api/v3/direction_lines
DirectionLine relations

    DirectionLine belongs to FieldShape.

DirectionLine has next attributes

    (readonly) id — Cropwise Operations Platform ID of the DirectionLine.

    field_shape_id — ID of the related FieldShape.

    name — Human-readable name of the direction line.

    point_a — Starting coordinate point [longitude, latitude].

    point_b — Ending coordinate point [longitude, latitude].

    external_id — External system identifier (optional).

    (readonly) created_at — Time when the object was created on the server.

    (readonly) updated_at — Time when the object was last updated on the server.

Filtering and sorting

    field_shape_id — filter by specific FieldShape

    external_id — filter by external identifier

    sort_by — available: id, name, created_at, updated_at

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Examples

    DirectionLine object

      {
          "id": 5,
          "field_shape_id": 119798,
          "name": "Test line",
          "point_a": [30.023204894690707, 48.89267376175872],
          "point_b": [30.027121195836685, 48.896638357324086],
          "external_id": null,
          "created_at": "2023-10-02T11:01:22Z",
          "updated_at": "2023-10-02T11:01:22Z"
      }

    List example (GET /api/v3/direction_lines)

      {
          "data": [
              {
                  "id": 5,
                  "field_shape_id": 119798,
                  "name": "Test line",
                  "point_a": [30.023204894690707, 48.89267376175872],
                  "point_b": [30.027121195836685, 48.896638357324086],
                  "external_id": null,
                  "created_at": "2023-10-02T11:01:22Z",
                  "updated_at": "2023-10-02T11:01:22Z"
              }
          ],
          "meta": {
              "request": { "server_time": "2025-01-01T12:00:00Z" },
              "response": { "obtained_records": 1, "first_record_id": 5, "last_record_id": 5 }
          }
      }

EquipmentAssignments

operations.cropwise.com/api/v3/equipment_assignments
EquipmentAssignments relations

    EquipmentAssignments belongs to Equippable

    EquipmentAssignments belongs to Equipment holder

EquipmentAssignments has next attributes

    (readonly) id - Cropwise Operations Platform ID of EquipmentAssignments

    equippable_id - ID of Equippable object

    equippable_type - type of Equippable object

    equipment_holder_id - ID of Equipment holder object

    equipment_holder_type - type of Equipment holder object

    start_time - start time of assignment

    end_time - end time of assignment

    no_end_time - boolean, true if there no end time of assignment

    external_id - external ID

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Additional info

external_id is optional field.

Allowed equippable objects are: PersonalIdentifier.

Allowed equipment holders are: Machine, User or Implement.
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Fertilizers

operations.cropwise.com/api/v3/fertilizers
Fertilizer relations

    Fertilizer has many ApplicationMixItems as applicable.

    Fertilizer has many AgriWorkApplicationMixItems as applicable.

Fertilizer object has next attributes

    (readonly) id - Cropwise Operations Platform ID of fertilizer

    name - name of fertilizer

    manufacturer_name - name of manufacturer

    fertilizer_type - type of fertilizer: 'granular', 'liquid', 'organic'

    source_type - type of source: 'inorganic', 'organic', 'other'

    nutrient_type - type of nutrient: 'nitrogen', 'phosphate', 'potassium', 'multinutrient', 'micronutrient', 'other'

    additional_info - your system info

    description - description

    element_N - concentration of N element in the fertilizer

    element_P2O5 - concentration of P205 element in the fertilizer

    element_K2O - concentration of K20 element in the fertilizer

    element_Ca - concentration of Ca element in the fertilizer

    element_Mg - concentration of Mg element in the fertilizer

    element_S - concentration of S element in the fertilizer

    element_B - concentration of B element in the fertilizer

    element_Cl - concentration of Cl element in the fertilizer

    element_Cu - concentration of Cu element in the fertilizer

    element_Fe - concentration of Fe element in the fertilizer

    element_Mn - concentration of Mn element in the fertilizer

    element_Mo - concentration of Mo element in the fertilizer

    element_Ni - concentration of Ni element in the fertilizer

    element_Zn - concentration of Zn element in the fertilizer

    element_Co - concentration of Co element in the fertilizer

    element_Se - concentration of Se element in the fertilizer

    units_of_measurement (deprecated) — use base_inventory_unit_id instead. Units of measurement: 'liter', 'kg'

    base_inventory_unit_id - ID of the base unit of measurement. See the Unit API for available units.

    wh_item_id - Cropwise Operations Platform ID of WhItem

    wh_item_base_unit_id (deprecated) — use base_inventory_unit_id instead. Cropwise Operations Platform ID of Unit

    external_id - a string field for storing id of the element from an external system

    archived - hide item from lists

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, fertilizer_type, description, additional_info, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Additional info

Fertilizer support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
FieldGroup

operations.cropwise.com/api/v3/field_groups
FieldGroup relations

    FieldGroup belongs to GroupFolder.

    FieldGroup has many Fields.

    FieldGroup has many MachineTasks.

    FieldGroup has many Notifications.

    FieldGroup has many AadditionalObjects.

FieldGroup object has next attributes

    (readonly) id - Cropwise Operations Platform ID of field group

    group_folder_id - Cropwise Operations Platform ID of group folder

    name - name of field group

    description - description of field group

    administrative_area_name - name of administrative area (region)

    subadministrative_area_name - name of subadministrative area (subregion, district)

    locality - name of location (city, town, village)

    external_id - a string field for storing id of the element from an external system

    legal_entity - a string field for storing legal entity of a separate structure

    machine_task_default_duration - default duration for machine tasks in field group

    machine_task_default_start_time - default start time for machine task in field group

    accounting_period_closing_date - closing date of the accounting period

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, group_folder_id, name, description, administrative_area_name, subadministrative_area_name, locality, external_id
FieldScoutReportThreatMappingItem

operations.cropwise.com/api/v3/field_scout_report_threat_mapping_items
FieldScoutReportThreatMappingItem

    FieldScoutReportThreatMappingItem belongs to FieldScoutReport.

    FieldScoutReportThreatMappingItem belongs to PlantThreat.

FieldScoutReportThreatMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of field scout report threat mapping item

    field_scout_report_id - Cropwise Operations Platform ID of related field scout report

    plant_threat_id - Cropwise Operations Platform ID of related plant threat

    comment - comment about threat

    (writeonly) photo - you can submit this image through multipart-form POST query

    (readonly) image - object describing image

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Multipart-form POST request with photo

To upload photo for field scout report threat mapping item we propouse the next workflow:

    Create FieldScoutReportThreatMappingItem through JSON API

    Update it with POST query equal to this HTML-form submitting:

HTML form example:

<form action="/api/v3/field_scout_report_threat_mapping_items/ID" enctype="multipart/form-data" method="PUT">
    <input type="file" name="photo">
</form>

Image structure

API returns uploaded photo as structure with different preview and original image.

{
    "data": {
        "id": 62,
        "field_scout_report_id": 44,
        "plant_threat_id": 1,
        "comment": "",
        "image": {
            "url": "/system/uploads/field_scout_report_threat_mapping_item/photo/62/photo.jpg",
            "preview_200": "/system/uploads/field_scout_report_threat_mapping_item/photo/62/preview_200_photo.jpg",
            "preview_400": "/system/uploads/field_scout_report_threat_mapping_item/photo/62/preview_400_photo.jpg",
            "preview_1000": "/system/uploads/field_scout_report_threat_mapping_item/photo/62/preview_1000_photo.jpg",
            "md5": "aa972d78daf7df64eb8b838eb837a103"
        },
        "created_at": "2014-04-14T14:37:30.568+03:00",
        "updated_at": "2014-06-24T14:45:28.712+03:00"
    }
}

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

FieldScoutReport

operations.cropwise.com/api/v3/field_scout_reports
FieldScoutReport relations

    FieldScoutReport belongs to User.

    FieldScoutReport belongs to Field.

    FieldScoutReport belongs to GrowthStage.

    FieldScoutReport belongs to ScoutingTask.

    FieldScoutReport belongs to HistoryItem.

    FieldScoutReport has many Photos.

    FieldScoutReport has many FieldScoutReportThreatMappingItems.

    FieldScoutReport has many PlantThreats.

    FieldScoutReport has many ScoutReportPoints

    FieldScoutReport has many ScoutReportPointIssues

    FieldScoutReport has many ScoutReportPointMeasurements

    FieldScoutReport has many AgroRecommendations

FieldScoutReport has next attributes

    (readonly) id - Cropwise Operations Platform ID of FieldScoutReport.

    field_id - Cropwise Operations Platform ID of Field.

    (readonly) user_id - Cropwise Operations Platform ID of User created this report.

    report_time - time when user create report (e.g. from mobile device without network access).

    season - Season

    growth_stage_id — Cropwise Operations Platform ID of GrowthStage.

    (readonly) growth_scale - growth scale for plant (for example "zadoks"). Deprecated, use growth_stage_id instead.

    (readonly) growth_stage - stage on growth scale (for example '00'). Deprecated, use growth_stage_id instead.

    additional_info - your system info.

    (readonly) image1 - First Photo (URLs for photo in different resolutions). Deprecated, use Photo relation instead.

    (readonly) image2 - Second Photo (URLs for photo in different resolutions). Deprecated, use Photo relation instead.

    (readonly) image3 - Third Photo (URLs for photo in different resolutions). Deprecated, use Photo relation instead.

    created_by_user_at - time of report object created on user's device.

    updated_by_user_at - time of last update on user's device.

    scouting_task_id - Cropwise Operations Platform ID of scouting task

    scout_report_template_id - Cropwise Operations Platform ID of scouting report template

    history_item_id - Cropwise Operations Platform ID of related HistoryItem

    field_condition - field condition, one of ['bad', 'satisfactory', 'good', 'excellent']

    (readonly) created_at - time when object created on server.

    (readonly) updated_at - time when object was updated on server.

Uploading Photos

You could upload any number of Photos to FieldScoutReport. Photos for FieldScoutReport stored in Photos relation.

    Create FieldScoutReport. From server response you should get ID of created FieldScoutReport.

    Upload Photos one by one (as described in Photo relation section). Set Photo photoable_type attribute to "FieldScoutReport" and photoable_id attribute to ID of FieldScoutReport.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, user_id, field_id, external_id, season, scouting_task_id, scout_report_template_id, created_at, updated_at
Comparison filters by (for more info see)

created_by_user_at, report_time, created_at, updated_at
Sorting by (for more info see)

report_time, created_by_user_at
Additional info

Field scout report support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
FieldScoutReport/v3a

operations.cropwise.com/api/v3a/field_scout_reports
FieldScoutReport relations

    FieldScoutReport belongs to User.

    FieldScoutReport belongs to Field.

    FieldScoutReport belongs to GrowthStage.

    FieldScoutReport belongs to ScoutingTask.

    FieldScoutReport has many Photos.

    FieldScoutReport has many PlantThreats.

    FieldScoutReport has many ScoutReportPoints

    FieldScoutReport has many AgroRecommendations

    FieldScoutReport has many ScoutReportPointIssues

    FieldScoutReport has many ScoutReportPointMeasurements

    FieldScoutReport has many FieldScoutReportThreatMappingItems.

FieldScoutReport has next attributes

    (readonly) id - Cropwise Operations Platform ID of FieldScoutReport.

    (readonly) user_id - Cropwise Operations Platform ID of User created this report.

    field_id - Cropwise Operations Platform ID of Field.

    report_time - time when user create report (e.g. from mobile device without network access).

    season - Season

    growth_stage_id — Cropwise Operations Platform ID of GrowthStage.

    additional_info - your system info.

    created_by_user_at - time of report object created on user's device.

    updated_by_user_at - time of last update on user's device.

    external_id - a string field for storing id of the element from an external system

    field_condition - field condition, one of ['bad', 'satisfactory', 'good', 'excellent']

    ears_count - a number with double precision field for record ears count

    plants_count - a number with double precision field for record plants count

    ground_cover - a number with double precision field for record ground cover

    scouting_task_id - Cropwise Operations Platform ID of scouting task

    scout_report_template_id - Cropwise Operations Platform ID of scouting report template

    (readonly) created_at - time when object created on server.

    (readonly) updated_at - time when object was updated on server.

Uploading Photos

You could upload any number of Photos to FieldScoutReport. Photos for FieldScoutReport stored in Photos relation.

    Create FieldScoutReport. From server response you should get ID of created FieldScoutReport.

    Upload Photos one by one (as described in Photo relation section). Set Photo photoable_type attribute to "FieldScoutReport" and photoable_id attribute to ID of FieldScoutReport.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Additional info

Field scount report support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
FieldScoutReport/v3b

operations.cropwise.com/api/v3b/field_scout_reports
FieldScoutReport relations

    FieldScoutReport belongs to User.

    FieldScoutReport belongs to Field.

    FieldScoutReport belongs to GrowthStage.

    FieldScoutReport belongs to ScoutingTask.

    FieldScoutReport has many Photos.

    FieldScoutReport has many PlantThreats.

    FieldScoutReport has many ScoutReportPoints

    FieldScoutReport has many AgroRecommendations

    FieldScoutReport has many ScoutReportPointIssues

    FieldScoutReport has many ScoutReportPointMeasurements

    FieldScoutReport has many FieldScoutReportThreatMappingItems.

FieldScoutReport has next attributes

    (readonly) id - Cropwise Operations Platform ID of FieldScoutReport.

    (readonly) user_id - Cropwise Operations Platform ID of User created this report.

    field_id - Cropwise Operations Platform ID of Field.

    report_time - time when user create report (e.g. from mobile device without network access).

    season - Season

    additional_info - your system info.

    created_by_user_at - time of report object created on user's device.

    updated_by_user_at - time of last update on user's device.

    external_id - a string field for storing id of the element from an external system

    field_condition - field condition, one of ['bad', 'satisfactory', 'good', 'excellent']

    (readonly) idempotency_key - used into mobile applications for safely retrying requests without accidentally performing the same operation twice

    risk_yield_decreasing - risk of yield decreasing

    scouting_task_id - Cropwise Operations Platform ID of scouting task

    scout_report_template_id - Cropwise Operations Platform ID of scouting report template

    (readonly) created_at - time when object created on server.

    (readonly) updated_at - time when object was updated on server.

Uploading Photos

You could upload any number of Photos to FieldScoutReport. Photos for FieldScoutReport stored in Photos relation.

    Create FieldScoutReport. From server response you should get ID of created FieldScoutReport.

    Upload Photos one by one (as described in Photo relation section). Set Photo photoable_type attribute to "FieldScoutReport" and photoable_id attribute to ID of FieldScoutReport.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

FieldScoutReportsAggregated

operations.cropwise.com/api/v3/field_scout_reports_aggregated
FieldScoutReportAggregated relations

    FieldScoutReport belongs to User.

    FieldScoutReport belongs to Field.

    FieldScoutReport belongs to GrowthStage.

    FieldScoutReport belongs to ScoutingTask.

    FieldScoutReport has many Photos.

    FieldScoutReport has many FieldScoutReportThreatMappingItems.

    FieldScoutReport has many PlantThreats.

    FieldScoutReport has many ScoutReportPoints

    FieldScoutReport has many ScoutReportPointIssues

    FieldScoutReport has many ScoutReportPointMeasurements

    FieldScoutReport has many AgroRecommendations

FieldScoutReport has next attributes

    (readonly) id - Cropwise Operations Platform ID of FieldScoutReport.

    (readonly) field_id - Cropwise Operations Platform ID of Field.

    (readonly) user_id - Cropwise Operations Platform ID of User created this report.

    (readonly) report_time - time when user create report (e.g. from mobile device without network access).

    (readonly) season - Season

    (readonly) growth_stage_id — Cropwise Operations Platform ID of GrowthStage.

    (readonly) growth_scale - growth scale for plant (for example "zadoks"). Deprecated, use growth_stage_id instead.

    (readonly) growth_stage - stage on growth scale (for example '00'). Deprecated, use growth_stage_id instead.

    (readonly) additional_info - your system info.

    (readonly) image1 - First Photo (URLs for photo in different resolutions). Deprecated, use Photo relation instead.

    (readonly) image2 - Second Photo (URLs for photo in different resolutions). Deprecated, use Photo relation instead.

    (readonly) image3 - Third Photo (URLs for photo in different resolutions). Deprecated, use Photo relation instead.

    (readonly) created_by_user_at - time of report object created on user's device.

    (readonly) updated_by_user_at - time of last update on user's device.

    (readonly) scouting_task_id - Cropwise Operations Platform ID of scouting task

    (readonly) scout_report_template_id - Cropwise Operations Platform ID of scouting report template

    (readonly) created_at - time when object created on server.

    (readonly) updated_at - time when object was updated on server.

    (readonly) risk_yield_decreasing - reported risk of yield decreasing

    (readonly) ears_count - reported ears count

    (readonly) plants_count - reported plants count

    (readonly) ground_cover - reported ground cover

    (readonly) threats - Plant threat values

    (readonly) measurements - Scout report point measurements

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    External ids

    Mass Request

Filters by

id, user_id, field_id, external_id, season, scouting_task_id, scout_report_template_id
Comparison filters by (for more info see)

season, created_by_user_at, report_time, created_at, updated_at
Sorting by (for more info see)

report_time, created_by_user_at
FieldWorkResults

operations.cropwise.com/api/v3/field_work_results
FieldWorkResult relations

    FieldWorkResult belongs to Crop. Optional.

    FieldWorkResult belongs to AgroOperation. Optional.

    FieldWorkResult belongs to YieldFile. Required.

    FieldWorkResult belongs to Field. Required.

    FieldWorkResult has many YieldMaps.

FieldWorkResult has next attributes

    (readonly) id - Cropwise Operations Platform ID of FieldWorkResult

    field_id - Cropwise Operations Platform ID of Field

    crop_id - Cropwise Operations Platform ID of Crop

    agro_operation_id - Cropwise Operations Platform ID of AgroOperation (optional)

    applicable_id - Cropwise Operations Platform ID of applicable object

    applicable_type - Cropwise Operations Platform type of applicable: 'Seed', 'Fertilizer', 'Chemical'

    work_date - date when the work was done

    work_type - work type: 'as_applied', 'yield'

    work_subtype - work subtype: 'fertilizing', 'seeding', 'pesticiding', 'subsoiling'

    name - custom name

    additional_info - your system information

    external_id - a string field for storing id of the element from an external system

    description - description

    measurement_units - measurement units

    totals - totals into json format

    (readonly) created_at - time when object was created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Count

    Single Resource

    Changes

    Changes Ids

    External ids

Filters by

field_id, crop_id, measurement_units, external_id
Comparison filters by (for more info see)

work_date, created_at, updated_at
Sorting by (for more info see)

id, created_at, updated_at
FuelHourlyDataItem

operations.cropwise.com/api/v3/fuel_hourly_data_items
FuelHourlyDataItems relations

    FuelHourlyDataItem belongs to Machine, FuelStation

    FuelHourlyDataItem belongs to DataSourceParameter(optional)

FuelHourlyDataItems object has next attributes

    id - Cropwise Operations Platform ID of MachineObjectIntersection

    object_type - Type of object for which fuel data

    object_id - ID of object for wich fuel data

    hour_start - Rounded down hour

    fuel_consumption - fuel consumption of object for hour

    fuel_drain - fuel drain of object for hour

    refuel - refuel of object

    data_source_parameter_id - ID of DataSourceParameter, fuel sensor by which data was calculated

    external_id - a string field for storing id of the element from an external system

    created_at - time when object created

    updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, object_type, object_id, hour_start, data_source_parameter_id, fuel_consumption, fuel_drain, refuel, created_at, updated_at
Comparison filters by (for more info see)

hour_start, created_at, updated_at
ScoutReportPoint

operations.cropwise.com/api/v3/scout_report_points
ScoutReportPoint relations

    ScoutReportPoint belongs to FieldScoutReport

    ScoutReportPoint belongs to GrowthStage(optional)

    ScoutReportPoint belongs to ScoutTaskPoint(optional)

    ScoutReportPoint has many Photos

    ScoutReportPoint has many ScoutReportPointIssue

    ScoutReportPoint has many ScoutReportPointMeasurement

ScoutReportPoint has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportPoint

    field_scout_report_id - Cropwise Operations Platform ID of related FieldScoutReport

    growth_stage_id - Cropwise Operations Platform ID of related GrowthStage

    latitude - latitude of this scout point

    longitude - longitude of this scout point

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - some description

    scouting_task_point_id - Cropwise Operations Platform ID of related ScoutTaskPoint

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

ScoutReportPointIssue

operations.cropwise.com/api/v3/scout_report_point_issues
ScoutReportPointIssue relations

    ScoutReportPoint belongs to ScoutReportPoint

    ScoutReportPoint belongs to PlantThreat

    ScoutReportPoint has many Photos

    ScoutReportPoint has many ScoutReportPointIssuePlantPart

ScoutReportPointIssue has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportPointIssue

    scout_report_point_id - Cropwise Operations Platform ID of related ScoutReportPoint

    plant_threat_id - Cropwise Operations Platform ID of related PlantThreat

    latitude - latitude of this scout point issue

    longitude - longitude of this scout point issue

    threat_level - can be low, mid, high

    threat_stage - can be egg, larva, pupa, imago

    amount

    damaged_area

    economic_damage_threshold_exceeded

    number_pests_in_trap - Number of pests in the trap

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - some description

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

ScoutReportPointIssuePlantPart

operations.cropwise.com/api/v3/scout_report_point_issue_plant_parts
ScoutReportPointIssuePlantPart relations

    ScoutReportPointIssuePlantPart belongs to ScoutReportPointIssue

ScoutReportPointIssuePlantPart has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportPointIssuePlantPart

    scout_report_point_issue_id - Cropwise Operations Platform ID of related ScoutReportPointIssue

    plant_part

    progress

    spread

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - some description

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

ScoutReportPointMeasurement

operations.cropwise.com/api/v3/scout_report_point_measurements
ScoutReportPointMeasurement relations

    ScoutReportPointMeasurement belongs to ScoutReportPoint

    ScoutReportPoint has many Photos

ScoutReportPointMeasurement has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportPointMeasurement

    scout_report_point_id - Cropwise Operations Platform ID of related ScoutReportPoint

    latitude - latitude of this measurement point

    longitude - longitude of this measurement point

    measurement_type - can be density_of_planting_square, density_of_planting_linear, stems_density, productive_stems_density, rate_of_tillers, rate_of_productive_tillers, plant_height, yield_forecast, ears_count, ground_cover, plants_density_estimate

    calculated_value

    density_of_planting_linear_row_width

    density_of_planting_linear_length_of_row

    density_of_planting_linear_rows_count

    density_of_planting_linear_plants_in_rows

    rate_of_productive_tillers_number_of_heads

    rate_of_productive_tillers_number_of_plants

    yield_forecast_head_number

    yield_forecast_kernels_per_head

    yield_forecast_thousand_grain_weight

    density_of_planting_square

    stems_density

    productive_stems_density

    plant_height

    ground_cover

    ears_count

    plants_density_estimate

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - some description

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

ScoutReportPointMeasurement/v3b

operations.cropwise.com/api/v3b/scout_report_point_measurements
Relations

    Belongs to ScoutReportPoint

    Belongs to ScoutReportMeasurementType

    Has many Photos

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportPointMeasurement

    scout_report_point_id - Cropwise Operations Platform ID of related ScoutReportPoint

    latitude - latitude of this measurement point

    longitude - longitude of this measurement point

    scout_report_measurement_type_id - Cropwise Operations Platform ID of ScoutReportMeasurementType

    measurement_values - Json. Measurement values field. Depends on the selected ScoutReportMeasurementType. ScoutReportMeasurementType has ScoutReportMeasurementValueType each value type has a system_name which must be specified as keys for the measurement values. Example: For ScoutReportMeasurementType with the system name density_of_planting_linear_millions_per_ha, measurement_values will be { "row_width": 10, "length_of_row": 10, "rows_count": 10, "plants_in_row": 10 }

    description - some description

    calculated_value - calculated value according to the calculate_value_expression in ScoutReportMeasurementType. Example: For ScoutReportMeasurementType with the system name density_of_planting_linear_millions_per_ha calculate_value_expression will be plants_in_rows / (row_width / 100.0 * length_of_row * rows_count) * 10000 / 1000000

    additional_info - your system info

    external_id - a string field for storing id of the element from an external system

    idempotency_key - The idempotency key transmitted during the request, if any

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, scout_report_point_id, scout_report_measurement_type_id, external_id
ScoutReportPointGrowthStageStructure

operations.cropwise.com/api/v3/scout_report_point_growth_stage_structures
ScoutReportPointGrowthStageStructure relations

    ScoutReportPointGrowthStageStructure has many growth_stages

    ScoutReportPointGrowthStageStructure has many growth_stage_structure_mapping_items

    ScoutReportPointGrowthStageStructure has many photos

ScoutReportPointGrowthStageStructure has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportPointGrowthStageStructure

    scout_report_point_id - Cropwise Operations Platform ID of related ScoutReportPoint

    idempotency_key - The idempotency key transmitted during the request, if any

    external_id - a string field for storing id of the element from an external system

    additional_info - some additional info

    description - some description

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

GrowthStageStructureMappingItem attributes

Param name: growth_stage_structure_mapping_items_attributes.

    (readonly)id - Cropwise Operations Platform ID of GrowthStageStructureMappingItem

    (readonly)scout_report_point_growth_stage_structure_id - Cropwise Operations Platform ID of ScoutReportPointGrowthStageStructure

    (readonly)growth_scale_name - Name of growth scale

    (readonly)growth_stage_group_name - Name of growth stage group

    (readonly)growth_stage_name - Name of growth stage

    growth_stage_id- Cropwise Operations Platform ID of GrowthStage

    growth_stage_fraction - Fraction of plants in some growth stage

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Uploading Photos

You could upload any number of Photos to ScoutReportPointGrowthStageStructure. Photos for ScoutReportPointGrowthStageStructure stored in Photos relation.

    Create ScoutReportPointGrowthStageStructure. From server response you should get ID of created ScoutReportPointGrowthStageStructure.

    Upload Photos one by one (as described in Photo relation section). Set Photo photoable_type attribute to "ScoutReportPointGrowthStageStructure" and photoable_id attribute to ID of ScoutReportPointGrowthStageStructure.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, scout_report_point_id, external_id, additional_info, description
Comparison filters by (for more info see)

created_at, updated_at, scout_report_point_id
Sorting by (for more info see)

id, created_at, updated_at
FieldShapes

operations.cropwise.com/api/v3/field_shapes
FieldShape relations

    FieldShape belongs to Field.

FieldShape has next attributes

    (readonly) id - Cropwise Operations Platform ID of FieldShape

    field_id - Cropwise Operations Platform ID of Field

    field_external_id - you can specify external_id for field and Cropwise Operations Platform will find field by external_id

    start_time - time when shape become actual

    (readonly) calculated_area - area calculated from shape

    legal_area - legal area

    tillable_area - tillable area

    (readonly) shape_simplified_[format] - series of attributes that contain simplified shape in different formats (see Shape Formats below)

    shape_[format] - series of attributes that contain or allow to set original shape in different formats (see Shape Formats below)

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_id, external_id, created_at, updated_at

active=true - request active fields in current time, this operator should be added to parameter name
Filter by dates

Filtering shapes from start_time,end_time equivalent to this logical expression: start_time <= specified date && end_time => specified date || end_time == null

    Request https://operations.cropwise.com/api/v3/field_shapes?start_time=2021-12-31T00:00&end_time=2021-12-31T00:00 - get all active shapes for specified date

Additional filters

You could find all FieldShapes that intersects specified GeoJSON geometry. Pass GeoJSON geometry as intersects_geometry URL query parameter.

api/v3/field_shapes?intersects_geometry={"type":"Point","coordinates":[30,40]}
Comparison filters by (for more info see)

created_at, updated_at
Filtering by dates

Filtering shapes from start_time,end_time equivalent to this logical expression: start_time <= specified date && end_time => specified date || end_time == null

    Request https://operations.cropwise.com/api/v3/field_shapes?start_time=2021-12-31&end_time=2021-12-31 - returned all active shapes for specified date

Shape formats

Cropwise Operations Platform API v3 now supports 4 formats of shapes:

    wkt - WKT (Well-Known Text)

    geojson - GeoJSON

    kml - KML (Keyhole Markup Language)

    shp_zip - Shapefile with additional files (we assepts up to 4 files - shp, shx, prj and dbf) packed into Zip archive and encode to Base64

Api response with two types of shapes - original and simplified. All list for shape attributes:

    shape_simplified_wkt - simplified WKT shape

    shape_wkt - original WKT shape

    shape_simplified_geojson - simplified GeoJSON shape

    shape_geojson - original GeoJSON shape

    shape_simplified_kml - simplified KML shape

    shape_kml - original KML shape

    shape_simplified_shp_zip - simplified SHP Zip-packed shape

    shape_shp_zip - original SHP Zip-packed shape

Multiformat request are supported only on single resource. By-default we respond with shape_simplified_geojson.
Query example

    Request https://operations.cropwise.com/api/v3/field_shapes/ID?shape_formats=simplified_wkt,wkt,simplified_geojson,geojson,kml_simplified_kml,shp_zip,simplified_shp_zip

Get shapes in multiple formats [GET]

    Response 200 (application/json)

      {
          "data": {
              "id": 71621,
              "field_id": 17323,
              "start_date": "2000-01-01",
              "calculated_area": 26.2,
              "legal_area": 26.2,
              "tillable_area": 26.2,
              
              "shape_simplified_wkt": "MULTIPOLYGON (((39.12398233381195 49.064546943309004, 39.12589011106124 49.06389879525872, 39.120555400604935 49.05975507759761, 39.12083803427151 49.059477274112254, 39.12631406156106 49.06378305364588, 39.127691900685555 49.06334323305861, 39.12172126447948 49.058759607921516, 39.11871828177232 49.056398181507106, 39.115326677773595 49.057740967149066, 39.12189791052109 49.062787664647594, 39.122463177854215 49.063042300940296, 39.12263982389582 49.063366381607615, 39.12398233381195 49.064546943309004)))",

              "shape_wkt": "MULTIPOLYGON (((39.12398233381195 49.064546943309004, 39.12589011106124 49.06389879525872, 39.120555400604935 49.05975507759761, 39.12083803427151 49.059477274112254, 39.12631406156106 49.06378305364588, 39.127691900685555 49.06334323305861, 39.12172126447948 49.058759607921516, 39.11871828177232 49.056398181507106, 39.115326677773595 49.057740967149066, 39.12189791052109 49.062787664647594, 39.122463177854215 49.063042300940296, 39.12263982389582 49.063366381607615, 39.12398233381195 49.064546943309004)))",
      
              "shape_simplified_geojson": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[39.123982,49.064547],[39.12589,49.063899],[39.120555,49.059755],[39.120838,49.059477],[39.126314,49.063783],[39.127692,49.063343],[39.121721,49.05876],[39.118718,49.056398],[39.115327,49.057741],[39.121898,49.062788],[39.122463,49.063042],[39.12264,49.063366],[39.123982,49.064547]]]]}",
              
              "shape_geojson": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[39.12398233381195,49.064546943309004],[39.12589011106124,49.06389879525872],[39.120555400604935,49.05975507759761],[39.12083803427151,49.059477274112254],[39.12631406156106,49.06378305364588],[39.127691900685555,49.06334323305861],[39.12172126447948,49.058759607921516],[39.11871828177232,49.056398181507106],[39.115326677773595,49.057740967149066],[39.12189791052109,49.062787664647594],[39.122463177854215,49.063042300940296],[39.12263982389582,49.063366381607615],[39.12398233381195,49.064546943309004]]]]}",
              
              "shape_simplified_shp_zip": "UEsDBBQAAAAIAHdzb0aTaL8a1wAAAGwBAAAKAAAAc2hhcGVzLnNocGNgUOdi\nwA62vWBmYGAFMpzX/OM43OfssOL4Nh6Ldg+Hv78UzSImODuws1cLO3d4OODQ\njwwYgbiBGLNACnmhmsqWpi6514+Qiym6oykLVLtw/srrukC+q/7iiDyg/MMk\nV95lQLNm8s2dVw7kz3tn83EOkF/cvJBPG6jeonUql1YHwi6Z7TPmSwP5znIH\ne6cA1fNrzC5qBarX2HlYzagf4TaYW7cGzuVLAfKDdnZGzQLKp3m9zucE6tf+\nI3lvDZCvqLzgkCCQbzn90apNQP6Vax0JMkA+uvsBUEsDBBQAAAAIAHdzb0b4\nQlwJOQAAAGwAAAAKAAAAc2hhcGVzLnNoeGNgUOdiwA7MXjAzMLACGc5r/nEc\n7nN2WHF8G49Fu4fD31+KZhETnB3Y2auFnTs8HHDoRwZGQNwAAFBLAwQUAAAA\nCAB3c29G48FRankAAACPAAAACgAAAHNoYXBlcy5wcmpzd/V3dw6OVgIS8eHu\nwfGGlhYmSjoujiGhvtFKLkhCwQEerkH+ni7RSggxM2NzC0Njcx0jSws9I1Nz\nIyNjUzPj2FidgCBPX1egfvei1NS88szkDCUdg1idUD/PEKCZqelAUaCAnoGh\nuYmpsZGlkamhpaUJkGEaGwsAUEsDBBQAAAAIAHdzb0afggQ6HgAAAE0AAAAK\nAAAAc2hhcGVzLmRiZmOOZ5diZGBgcGTgYcAG3DxdYEw/EMGNJs+rgAAGAFBL\nAwQUAAAACAB3c29GUDyBDgcAAAAFAAAACgAAAHNoYXBlcy5jcGcLDXHTtQAA\nUEsBAjQDFAAAAAgAd3NvRpNovxrXAAAAbAEAAAoAAAAAAAAAAQAAAKSBAAAA\nAHNoYXBlcy5zaHBQSwECNAMUAAAACAB3c29G+EJcCTkAAABsAAAACgAAAAAA\nAAABAAAApIH/AAAAc2hhcGVzLnNoeFBLAQI0AxQAAAAIAHdzb0bjwVFqeQAA\nAI8AAAAKAAAAAAAAAAEAAACkgWABAABzaGFwZXMucHJqUEsBAjQDFAAAAAgA\nd3NvRp+CBDoeAAAATQAAAAoAAAAAAAAAAQAAAKSBAQIAAHNoYXBlcy5kYmZQ\nSwECNAMUAAAACAB3c29GUDyBDgcAAAAFAAAACgAAAAAAAAABAAAApIFHAgAA\nc2hhcGVzLmNwZ1BLBQYAAAAABQAFABgBAAB2AgAAAAA=\n",
              
              "shape_shp_zip": "UEsDBBQAAAAIAHdzb0al8KS31wAAAGwBAAAKAAAAc2hhcGVzLnNocGNgUOdi\nwA62vWBmYGAFMnI2ebEd7nN2sJtgw2fR7uHgvcXHNGKCs8NlD0Zh5w4PBxz6\nkQEjEDcQYxZIIS9UU1uD0fJ7/Qi5N59OackC1b75+PGqLpCvWfU/Og8oP5ft\nDe8yoFn9y5/NKwfyc6Z2fp4D5DNsV+XXBqqP2snBrdWBsCvfpHehNJCfKvqz\nfwpQ/SKdwPxWoHqFywqaRv0It8Hcuv1oGF8KkH904snIWUD5cgXpXE6g/r43\n0++vAfLPpakdFQTy32ZkrNwE5F8N3ZMsA+Sjux8AUEsDBBQAAAAIAHdzb0bU\n56f8OAAAAGwAAAAKAAAAc2hhcGVzLnNoeGNgUOdiwA7MXjAzMLACGTmbvNgO\n9zk72E2w4bNo93Dw3uJjGjHB2eGyB6Owc4eHAw79yMAIiBsAUEsDBBQAAAAI\nAHdzb0bjwVFqeQAAAI8AAAAKAAAAc2hhcGVzLnByanN39Xd3Do5WAhLx4e7B\n8YaWFiZKOi6OIaG+0UouSELBAR6uQf6eLtFKCDEzY3MLQ2NzHSNLCz0jU3Mj\nI2NTM+PYWJ2AIE9fV6B+96LU1LzyzOQMJR2DWJ1QP88QoJmp6UBRoICegaG5\niamxkaWRqaGlpQmQYRobCwBQSwMEFAAAAAgAd3NvRp+CBDoeAAAATQAAAAoA\nAABzaGFwZXMuZGJmY45nl2JkYGBwZOBhwAbcPF1gTD8QwY0mz6uAAAYAUEsD\nBBQAAAAIAHdzb0ZQPIEOBwAAAAUAAAAKAAAAc2hhcGVzLmNwZwsNcdO1AABQ\nSwECNAMUAAAACAB3c29GpfCkt9cAAABsAQAACgAAAAAAAAABAAAApIEAAAAA\nc2hhcGVzLnNocFBLAQI0AxQAAAAIAHdzb0bU56f8OAAAAGwAAAAKAAAAAAAA\nAAEAAACkgf8AAABzaGFwZXMuc2h4UEsBAjQDFAAAAAgAd3NvRuPBUWp5AAAA\njwAAAAoAAAAAAAAAAQAAAKSBXwEAAHNoYXBlcy5wcmpQSwECNAMUAAAACAB3\nc29Gn4IEOh4AAABNAAAACgAAAAAAAAABAAAApIEAAgAAc2hhcGVzLmRiZlBL\nAQI0AxQAAAAIAHdzb0ZQPIEOBwAAAAUAAAAKAAAAAAAAAAEAAACkgUYCAABz\naGFwZXMuY3BnUEsFBgAAAAAFAAUAGAEAAHUCAAAAAA==\n",
              
              "created_at": "2013-09-27T10:11:38.205+03:00",
              "updated_at": "2015-03-11T18:46:19.486+02:00"
          }
      }

FieldShapeLandParcelMappingItems

operations.cropwise.com/api/v3/field_shape_land_parcel_mapping_items
FieldShapeLandParcelMappingItem relations

    FieldShapeLandParcelMappingItem belongs to FieldShape

    FieldShapeLandParcelMappingItem belongs to LandParcel

FieldShapeLandParcelMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of FieldShapeLandParcelMappingItem

    field_shape_id - id of FieldShape

    land_parcel_id - id of LandParcel

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_shape_id, land_parcel_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Fields

operations.cropwise.com/api/v3/fields
Field relations

    Field belongs to FieldGroup.

    Field has many FieldShapes.

    Field has many HistoryItems.

    Field has many Notes.

    Field has many FieldScoutReports.

    Field has many HarvestWeighings.

    Field has many MachineTaskFieldMappingItems.

    Field has many MachineTasks.

    Field has many AgroOperations.

    Field has many AgriWorks.

    Field has many AgriWorkApplicationMixItems.

    Field has many SatelliteImages

Field has next attributes

    (readonly) id - Cropwise Operations Platform ID of Field

    field_group_id - Cropwise Operations Platform ID of FieldGroup

    name - Name of field

    additional_info - your system info

    description - description

    field_type - type of field. Can be standard for a simple field and plot for a plot of field

    parent_id - Cropwise Operations Platform ID of Field for plot of field

    (readonly) shape_simplified_[format] - series of attributes that contain simplified shape in different formats (see FieldShapes/Shape Formats above)

    shape_[format] - series of attributes that contain or allow to set original shape in different formats (see FieldShapes/Shape Formats above)

    (readonly) current_shape_id - Cropwise Operations Platform ID of current FieldShape for this field

    (readonly) calculated_area - area calculated from shape

    legal_area - legal area

    (readonly) end_time - time when shape end become actual

    tillable_area - tillable area

    administrative_area_name - Administrative area (e.g. country, state, district, etc.)

    subadministrative_area_name - Subadministrative area (e.g. region, etc.)

    locality - Locality (town, villege, etc.)

    external_id - a string field for storing id of the element from an external system

    public_registry_key - a string field for storing the key of the field from an external system

    moisture_zone - moisture zone (one of: arid, low_hydrated, humidified)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, description, field_group_id, additional_info, current_shape_id, external_id, created_at, updated_at, field_type, parent_id

active=true - request active fields in current time, this operator should be added to parameter name

season_year=year - request active fields in current time for season, this operator should be added to parameter name. year - it is number of season year, for exemple 2024
Comparison filters by (for more info see)

created_at, updated_at
Important! Deprecated feature!

Shape attributes shape_[format], shape_simplified_[format], tillable_area, legal_area, are proxing from current FieldShape for legacy reasons. We strongly recommend to use FieldShapes resource for operations with shapes. Fields are currently creating with only with this attributes because we currently can not create field without related FieldShape object. We are planning to change this feature in future.
Field creation

Example with GeoJSON:

{
    "data": {
        "name": "test api field 2",
        "description": "the biggest field",
        "field_group_id": "77",
        "shape_geojson": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[36.9636726379395,50.2249156874147],[36.9618701934815,50.2186552658086],[36.974573135376,50.2172273352869],[36.974573135376,50.2179413058903],[36.9734573364258,50.2190946204475],[36.9731140136719,50.2200282356199],[36.972599029541,50.2211265830181],[36.9720840454102,50.2222798205684],[36.9716548919678,50.2229937155558],[36.9711399078369,50.2238723408725],[36.9636726379395,50.2249156874147]]]]}",
        "tillable_area": "51",
        "legal_area": "51",
        "administrative_area_name": "Zone 1",
        "subadministrative_area_name": "Subzone 1",
        "locality": "Town name",
        "additional_info": "12333"
    }
}

You can replace "shape_geojson" attribute with "shape_wkt", "shape_kml" or "shape_shp_zip".
Additional info

Field support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
Fields/v3a

operations.cropwise.com/api/v3a/fields
Field relations

    Field belongs to FieldGroup.

    Field belongs to AdminRegion.

    Field belongs to Company.

    Field has many FieldShapes.

    Field has many HistoryItems.

    Field has many HistoricalValues.

    Field has many Notes.

    Field has many Notifications.

    Field has many ApplicationTasks.

    Field has many SoilTests.

    Field has many SoilTestTasks.

    Field has many SoilTextureMaps.

    Field has many ProductivityEstimates.

    Field has many PlanThreatItemFieldMappingItems.

    Field has many PlanThreatItems.

    Field has many Alerts.

    Field has many YieldMaps.

    Field has many FieldWorkResults.

    Field has many FieldScoutReports.

    Field has many HarvestWeighings.

    Field has many MachineTaskFieldMappingItems.

    Field has many MachineTasks.

    Field has many AgroOperations.

    Field has many AgriWorks.

    Field has many AgriWorkApplicationMixItems.

    Field has many SatelliteImages

Field has next attributes

    (readonly) id - Cropwise Operations Platform ID of Field

    field_group_id - Cropwise Operations Platform ID of FieldGroup

    name - Name of field

    additional_info - your system info

    description - description

    field_type - type of field. Can be standard for a simple field and plot for a plot of field

    parent_id - Cropwise Operations Platform ID of Field for plot of field

    administrative_area_name - Administrative area (e.g. country, state, district, etc.)

    subadministrative_area_name - Subadministrative area (e.g. region, etc.)

    (readonly) region_id - Cropwise Operations Platform ID of AdminRegion

    (readonly) country_id - Cropwise Operations Platform ID of AdminRegion

    (readonly) district_id - Cropwise Operations Platform ID of AdminRegion

    locality - Locality (town, villege, etc.)

    external_id - a string field for storing id of the element from an external system

    public_registry_key - a string field for storing the key of the field from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

additional_info, (point) - [lat, long], field_type, parent_id
Important! Deprecated feature!

Shape attributes shape_[format], shape_simplified_[format], tillable_area, legal_area, are proxing from current FieldShape for legacy reasons. We strongly recommend to use FieldShapes resource for operations with shapes. Fields are currently creating with only with this attributes because we currently can not create field without related FieldShape object. We are planning to change this feature in future.
Field creation

Example with GeoJSON:

{
    "data": {
        "name": "test api field 2",
        "description": "the biggest field",
        "field_group_id": "77",
        "shape_geojson": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[36.9636726379395,50.2249156874147],[36.9618701934815,50.2186552658086],[36.974573135376,50.2172273352869],[36.974573135376,50.2179413058903],[36.9734573364258,50.2190946204475],[36.9731140136719,50.2200282356199],[36.972599029541,50.2211265830181],[36.9720840454102,50.2222798205684],[36.9716548919678,50.2229937155558],[36.9711399078369,50.2238723408725],[36.9636726379395,50.2249156874147]]]]}",
        "tillable_area": "51",
        "legal_area": "51",
        "administrative_area_name": "Zone 1",
        "subadministrative_area_name": "Subzone 1",
        "locality": "Town name",
        "additional_info": "12333"
    }
}

You can replace "shape_geojson" attribute with "shape_wkt", "shape_kml" or "shape_shp_zip".
Additional info

Field support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
FuelMovements

operations.cropwise.com/api/v3/fuel_movements
FuelMovements relations

    FuelMovements belongs to Object from

    FuelMovements belongs to Object to

    FuelMovements belongs to FuelTank

    FuelMovements belongs to FuelPump

FuelMovements has next attributes

    (readonly) id - Cropwise Operations Platform ID of FuelMovements

    object_from_id - object fuel was transfered from id (for example fuel_station_id)

    object_from_type - object fuel was transfered from type (for example 'FuelStation')

    object_to_id - object fuel was transfered to id (for example machine_id)

    object_to_type - object fuel was transfered to type (for example 'Machine')

    fuel_tank_id - id of fuel tank

    fuel_pump_id - id of fuel pump

    time_start - time when fuel transfering started

    time_end - time when fuel transfering ended

    amount - amount of fuel transfered

    rfid - RFID

    external_id - External ID

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Filters by

id, rfid, fuel_tank_id, fuel_pump_id, object_from_id, object_from_type, object_to_id, object_to_type, external_id
Additional info

object_from_id/object_from_type are optional fields. The same is for time_end field.
Request examples
Refueling machine

Replenishes Machine #38 on FuelStation #1 for 50.2 litres via FuelPump #2 from FuelTank #2

  {
    "data": {
      "time_start": "2019-08-08T10:00:00+02:00",
      "time_end": "2019-08-08T10:07:13+02:00",
      "amount": 50.2,
      "rfid": "test-rfid99",
      "fuel_tank_id": 2,
      "fuel_pump_id": 2,
      "object_from_id": 1,
      "object_from_type": "FuelStation",
      "object_to_id": 38,
      "object_to_type": "Machine"
      "external_id": "ABCDEFG"
    }
  }

FuelTank replenishment without gasoline tanker

Replenishes FuelTank #2 on FuelStation #1 for 20 000 litres

  {
    "data": {
      "time_start": "2019-08-08T10:00:00+02:00",
      "amount": 20000,
      "fuel_tank_id": 2,
      "object_to_id": 1,
      "object_to_type": "FuelStation"
    }
  }

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

FuelStations

operations.cropwise.com/api/v3/fuel_stations

    (readonly) id - Cropwise Operations Platform ID of FuelStation

    name - name of FuelStation

    description - some text description of object

    geo_gson - simplified shape in GeoJSON format

    geometry_type - type of geometry

    additional - - additional settings for polygon

    avatar_id — Cropwise Operations Platform ID of Avatar

    external_id - External ID

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

FuelStationMachineRegionMappingItems

operations.cropwise.com/api/v3/fuel_station_machine_region_mapping_items
FuelStationMachineRegionMappingItem relations

    FuelStationMachineRegionMappingItem belongs to FuelStation

    FuelStationMachineRegionMappingItem belongs to MachineRegion

FuelStationMachineRegionMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of FuelStationMachineRegionMappingItem

    fuel_station_id - ID of FuelStation

    machine_region_id - ID of MachineRegion

    date_start - start date of mapping

    date_end - end date of mapping

    no_date_end - boolean, true if there is no end date of mapping

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

FuelStationMachineRegionMappingItem methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, fuel_station_id, machine_region_id, external_id
Comparison filters by (for more info see)

created_at, updated_at
FuelTanks

operations.cropwise.com/api/v3/fuel_tanks

    (readonly) id - Cropwise Operations Platform ID of FuelTank

    fuelable_object_type - name of object from which was fueling

    fuelable_object_id - Cropwise Operations Platform ID of object from which was fueling

    fuel_type_id - Cropwise Operations Platform ID of fuel type

    fuel_pump_id - Cropwise Operations Platform ID of linked fuel pump

    tank_size - size of fuel tank

    external_id - External ID

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

FuelTypes

operations.cropwise.com/api/v3/fuel_types

    (readonly) id - Cropwise Operations Platform ID of FuelType

    name - name for FuelType

    short_name - short name for FuelType

    standard_name - standard name for FuelType

    category - category of FuelType (either one of 'gas', 'diesel', 'natural_gas', 'other')

    external_id - External ID

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

FuelPumps

operations.cropwise.com/api/v3/fuel_pumps

    (readonly) id - Cropwise Operations Platform ID of FuelPump

    fuelable_object_type - name of object from which was fueling

    fuelable_object_id - Cropwise Operations Platform ID of object from which was fueling

    fuel_type_id - Cropwise Operations Platform ID of fuel type

    external_id - External ID

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

GpsLoggers

operations.cropwise.com/api/v3/gps_loggers

GpsLogger appears automatically in system when Cropwise Operations Platform start receiving data from device
GpsLogger relations

    GpsLogger has many GpsLoggerMappingItems

    GpsLogger has many DataSourceGpsLoggers

GpsLogger attributes

    (readonly) id - Cropwise Operations Platform ID of GpsLogger

    (readonly) logger_type - gps logger type

    (readonly) imei - device imei or unique id

    (readonly) phone_number - sim phone number in device

    (readonly) serial_number - device serial number

    (readonly) description - some description

    external_id - External ID

    gps_filter_formula - GPS filter formula

    auto_fill_coordinates - Auto fill coordinates (true/false)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

    Update Resource

Filters by

id, logger_type, imei, phone_number, serial_number, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Additional info

Gps Logger support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
GpsLoggerMappingItems

operations.cropwise.com/api/v3/gps_logger_mapping_items
GpsLoggerMappingItem relations

    GpsLoggerMappingItem belongs to Machine

    GpsLoggerMappingItem belongs to GpsLogger

GpsLoggerMappingItem attributes

    (readonly) id - Cropwise Operations Platform ID of GpsLoggerMappingItem

    gps_logger_id - id of gps_logger

    mappable_id - id of mappable object (for example machine_id)

    mappable_type - type of mappable object (for example "Machine")

    start_time - start time when logger was installed on mappable object

    end_time - expiration date for installed logger (can be nil)

    external_id - External ID

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

    Update Resource

Filters by

id, logger_type, mappable_id, mappable_type, external_id, start_time, end_time, created_at, updated_at
Comparison filters by (for more info see)

start_time, end_time, created_at, updated_at
GpsLoggerDataItems ⚠️

⚠️⚠️⚠️ Testing stage, may be changed !!! ⚠️⚠️⚠️

operations.cropwise.com/api/v3/gps_logger_data_items
Filters by

date_at, machine_ids

Note: parameter date_at is required!
it returns records with next attributes

    id - internal record id

    machine_id - internal id of Machine

    gps_logger_id - internal id of GpsLogger

    time - time

    speed - speed

    lat - latitude

    long - longitude

GpsAggregatedData ⚠️

⚠️⚠️⚠️ Testing stage, may be changed !!! ⚠️⚠️⚠️

operations.cropwise.com/api/v3/gps_aggregated_data
Filters by

date_at, machine_ids

Note: parameter date_at is required!
it returns records aggregated by each hour with next attributes

    id - internal record id

    machine_id - internal id of Machine

    gps_logger_id - internal id of GpsLogger

    hour_start - beginning of hour for each grouped record

    last_time - time of last GPS data for this hour

    last_lat - last known latitude for this hour

    last_long - last known longitude for this hour

    last_alt - last known altitude for this hour

    avg_speed - average speed for this hour

    max_speed - maximum speed for this hour

    distance - distance passed for this hour

GpsLoggerEventDataItems ⚠️

⚠️⚠️⚠️ Testing stage, may be changed !!! ⚠️⚠️⚠️

operations.cropwise.com/api/v3/gps_logger_event_data_items
Filters by

date_at, from_time, to_time, machine_ids
it returns records with next attributes

    id - internal record id

    machine_id - internal id of Machine

    gps_logger_id - internal id of GpsLogger

    time - record time

    data - hash with custom attributes from GpsLogger (see example below)

data attribute example

{
    "time": 1620162010, 
    "satellites": 18, 
    "adc_1": 12345, 
    "adc_2": 987654321
}

GroupFolders

operations.cropwise.com/api/v3/group_folders
GroupFolder relations

    GroupFolder has many FieldGroups.

GroupFolder attributes

    (readonly) id - Cropwise Operations Platform ID of GroupFolder

    parent_id - Cropwise Operations Platform ID of parent GroupFolder

    name - name of GroupFolder

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated on server

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
GrowthScales

operations.cropwise.com/api/v3/growth_scales
GrowthScales relations

    GrowthScales has many GrowthStageGroups

    GrowthScales has many GrowthStages

    GrowthScales has many GrowthScaleCropAssignments

    GrowthScales has many Crops

GrowthScales attributes

    (readonly) crop_to_growth_scales - crop and related growth scales

    (readonly) growth_scales - growth scales and related stages

Acceptable methods

    Mass Request

GrowthScales/v3a

operations.cropwise.com/api/v3a/growth_scales
GrowthScales relations

    GrowthScales has many GrowthStageGroups

    GrowthScales has many GrowthStages

    GrowthScales has many GrowthScaleCropAssignments

    GrowthScales has many Crops

GrowthScales attributes

    (readonly) id - Cropwise Operations Platform ID of GrowthScales

    name - name of GrowthScales

    standard_name - standard name of GrowthScales

    (readonly) localized_name - name of GrowthScales in locale

    hidden - boolean, hide object in reports and views

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - description

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

GrowthScalesCropAssignments
GrowthScalesCropAssignments###

    (readonly) id - Cropwise Operations Platform ID of GrowthScalesCropAssignments

    crop_id - Cropwise Operations Platform ID of Crops

    growth_scale_id - Cropwise Operations Plantform ID of GrowthScales

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

GrowthStages

operations.cropwise.com/api/v3/growth_stages
GrowthStages relations

    GrowthScales belons to GrowthScale

    GrowthScales belons to GrowthStageGroup

GrowthStages attributes

    (readonly) id - Cropwise Operations Platform ID of GrowthScale

    growth_scale_id - Cropwise Operations Platform ID of GrowthScale

    growth_stage_group_id - Cropwise Operations Platform ID of GrowthStageGroup

    code - code of GrowthScale

    name - name of GrowthScale

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - description

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

Filters by

code, growth_scale_id
GrowthStageGroup

operations.cropwise.com/api/v3/growth_stage_groups
GrowthStageGroup relations

    GrowthScales belons to GrowthScale

GrowthStageGroup attributes

    (readonly) id - Cropwise Operations Platform ID of GrowthScale

    growth_scale_id - Cropwise Operations Platform ID of GrowthScale

    standard_name - standard_name of GrowthStageGroup

    name - name of GrowthStageGroup

    localized_name - localized name of GrowthStageGroup

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

GrowthStagesPredictions

operations.cropwise.com/api/v3/growth_stages_predictions
GrowthStagesPredictions relations

    GrowthStagesPredictions belons to HistoryItem

    GrowthStagesPredictions belons to GrowthScale

GrowthStagesPredictions attributes

    (readonly) id - Cropwise Operations Platform ID of GrowthStagesPredictions

    (readonly) history_item_id - Cropwise Operations Platform ID of HistoryItem

    (readonly) growth_scale_id - Cropwise Operations Platform ID of GrowthScale

    (readonly) year - year of GrowthStagesPredictions

    (readonly) prediction_data - information about growth stages. This is a hash where the key is the growth stage code and the value is the date until which this growth stage is actual

    (readonly) fact_data - fact data

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Changes

    Changes Ids

    Mass Request

Filters by

history_item_id, growth_scale_id, year
HarvestIndicators

operations.cropwise.com/api/v3/harvest_indicators
HarvestIndicator relations

    HarvestIndicator belongs to Season.

    HarvestIndicator belongs to HistoryItem.

    HarvestIndicator belongs to AgroOperation.

    HarvestIndicator belongs to HarvestWeighing.

HarvestIndicator has next attributes

    (readonly) id - Cropwise Operations Platform ID of HarvestIndicator

    custom_name - user custom name of HarvestIndicator

    made_at - time when harvest indicators were made

    season_id - Cropwise Operations Platform ID of Season

    history_item_id - Cropwise Operations Platform ID of HistoryItem

    agro_operation_id - Cropwise Operations Platform ID of AgroOperation

    harvest_weighing_id - Cropwise Operations Platform ID of HarvestWeighing

    grain_humidity - grain humidity parameter of harvest indicators

    protein_content - protein content parameter of harvest indicators

    oil_content - oil content parameter of harvest indicators

    grain_nature - grain nature parameter of harvest indicators

    harmful_admixture - harmful admixture parameter of harvest indicators

    garbage_admixture - garbage admixture parameter of harvest indicators

    grain_admixture - grain admixtureparameter of harvest indicators

    oil_acid_number - oil acid number parameter of harvest indicators

    gluten_quality - gluten quality parameter of harvest indicators

    gluten_amount - gluten amount parameter of harvest indicators

    grain_class - grain class parameter of harvest indicators

    grain_type - grain type parameter of harvest indicators

    falling_number - falling number parameter of harvest indicators

    oil_by_dry_matter - mass fraction of oil in terms of dry matter parameter of harvest indicators

    core - core parameter of harvest indicators

    oil_on_dry_basis_content - mass fraction of oil in rapeseed from the field at actual humidity

    oil_on_wet_basis_content - mass fraction of oil in rapeseed, when dried to standard moisture content

    erucic_acid_content - erucic acid content

    glucosinolates_content - glucosinolates content

    starch_content - starch content

    green_index - green index

    vitreousness - vitreousness

    admixtures - admixtures

    gmo - gmo

    ambrosia_weight - ambrosia weight

    ambrosia_quantity - ambrosia quantity

    aegilops_weight - aegilops weight

    aegilops_quantity - aegilops quantity

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - your description

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

    (readonly) photos - photos of harvest indicators

    (readonly) plant_threats - plant threats of harvest indicators

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

Filters by

custom_name, made_at, season_id, history_item_id, agro_operation_id, harvest_weighing_id, grain_humidity, protein_content, oil_content, grain_nature, harmful_admixture, garbage_admixture, grain_admixture, oil_acid_number, gluten_quality, gluten_amount, grain_class, grain_type, falling_number, oil_by_dry_matter, core
Comparison filters by (for more info see)

made_at, created_at, updated_at
HarvestIndicatorPlantThreatAssignment

operations.cropwise.com/api/v3/harvest_indicator_plant_threat_assignments
HarvestIndicatorPlantThreatAssignment

    HarvestIndicatorPlantThreatAssignment belongs to HarvestIndicator.

    HarvestIndicatorPlantThreatAssignment belongs to PlantThreat.

HarvestIndicatorPlantThreatAssignment has next attributes

    (readonly) id - Cropwise Operations Platform ID of harvest indicator plant threat assignments

    harvest_indicator_id - Cropwise Operations Platform ID of related harvest indicator

    plant_threat_id - Cropwise Operations Platform ID of related plant threat

    plant_threat_harmful_admixture - harmful admixture of plant threat

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

HarvestTransportations

operations.cropwise.com/api/v3/harvest_transportations
HarvestTransportation has next attributes

    (readonly) id - Cropwise Operations Platform ID of Harvest Transportation

    machine_id - Cropwise Operations Platform ID of Machine

    loading_time - time of loading

    loader_id - Cropwise Operations Platform ID of Machine or User who make load

    loader_type - type of loader (Machine/User)

    reloading_time - time of reloading

    reloader_id - Cropwise Operations Platform ID of Machine or User who make reload

    reloader_type - type of reloader (Machine/User)

    unloading_time - time of unloading

    unloader_id - Cropwise Operations Platform ID of Machine or User who make reload

    unloader_type - type of unloader (Machine/User)

    distance - distance, km

    weight - weight, kg

    loaded_duration - loaded duration interval, seconds

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_id, loading_time, loader_id, loader_type, reloading_time, reloader_id, reloader_type, unloading_time, unloader_id, unloader_type, distance, weight, loaded_duration, external_id, created_at, updated_at
Comparison filters by (for more info see)

loading_time, reloading_time, unloading_time, created_at, updated_at
HarvestWeighings

operations.cropwise.com/api/v3/harvest_weighings
HarvestWeighing relations

    HarvestWeighing belongs to Machine.

    HarvestWeighing belongs to Field.

    HarvestWeighing belongs to AdditionalObject as weighing_place.

    HarvestWeighing belongs to User as created_by_user.

    HarvestWeighing belongs to HistoryItem.

HarvestWeighing has next attributes

    (readonly) id - Cropwise Operations Platform ID of HarvestWeighing

    machine_id - Cropwise Operations Platform ID of Machine

    field_id - Cropwise Operations Platform ID of Field

    weighing_place_id - Cropwise Operations Platform ID of AdditionalObject

    season — Season

    departure_from_field_time - time of departure from field

    weight - weight

    brutto_weigh - brutto weigth

    seed_moisture - seed moisure

    seed_admixture - seed admixture

    weighing_time - time of weighing

    last_truck - is this track last? (true/false)

    (readonly) track_length - calculated track length

    manually_set_track_length - true if car was without logger or track was not recorded

    additional_info - your system info

    description - description

    external_id - a string field for storing id of the element from an external system

    waybill_number - waybill number

    waybill_date - date when waybill was created

    (readonly) created_by_user_id - Cropwise Operations Platform ID of User created this object (from API-token)

    (readonly) unloaded_machines - array with Cropwise Operations Platform ID of unloaded Machines

    history_item_id - Cropwise Operations Platform ID of related HistoryItem. When you change 'field_id' or 'season' this attribute is required. If you want this attribute to be automatically determined by the system, you must set it to null

    marketable_weight - marketable weight

    loaded_trailer_weight - loaded trailer weight

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_id, weighing_place_id, field_id, season, type_of_route, external_id
Comparison filters by (for more info see)

weighing_time, departure_from_field_time, created_at, updated_at
Additional info

Harvest Weighing support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
HistoricalValues

operations.cropwise.com/api/v3/historical_values
HistoricalValues relations

    HistoricalValue belongs to field.

HistoricalValues has next attributes:

    last_value - last measured value

    last_value_date - date of last value measure

Temperature value:

    date - date of measured value

    temperature - value of temperature

NDVI value:

    date - date of measured value

    ndvi - NDVI value

Soil moisture value:

    date - date of measured value

    soil_moisture - soil moisture

Acceptable methods

    Resources Collection

Query params and meta

You can pass next params to this resource:

    field_id - Cropwise Operations Platform ID of field. Required!

    type - type of value: 'temperature', 'ndvi', 'soil_moisture'. Required!

    from_time - begining of time range. Default is 24 hours ago.

    to_time - end of time range. Default is current time.

Example:

https://operations.cropwise.com/api/v3/historical_values?field_id=17323&type=ndvi&from_time=2012-01-01&to_time=2012-12-31

The 'meta' block in this resource deffers from typical 'meta' in other resources.

{
    "request": {
        "field_id": "17323",
        "type": "ndvi",
        "from_time": "2012-01-01T00:00:00.000+00:00",
        "to_time": "2012-12-31T00:00:00.000+00:00",
        "server_time": "2015-04-24T10:59:21.171+03:00"
    },
    "response": {
        "from_time": "2012-01-01T00:00:00.000+00:00",
        "to_time": "2012-12-31T00:00:00.000+00:00",
        "obtained_records": 0
    }
}

HistoricalValues/v3a

operations.cropwise.com/api/v3a/historical_values
HistoricalValues relations

    HistoricalValue belongs to field.

HistoricalValues has next attributes:

    last_value - last measured value

    last_value_date - date of last value measure

Temperature value:

    date - date of measured value

    temperature - value of temperature

NDVI value:

    date - date of measured value

    ndvi - NDVI value

Soil moisture value:

    date - date of measured value

    soil_moisture - soil moisture

Acceptable methods

    Resources Collection

Query params and meta

You can pass next params to this resource:

    field_id - Cropwise Operations Platform ID of field. Required!

    type - type of value: 'temperature', 'ndvi', 'soil_measure'. Required!

    from_time - begining of time range. Default is 24 hours ago.

    to_time - end of time range. Default is current time.

Example:

https://operations.cropwise.com/api/v3a/historical_values?field_id=17323&type=ndvi&from_time=2012-01-01&to_time=2012-12-31

The 'meta' block in this resource deffers from typical 'meta' in other resources.

{
    "request": {
        "field_id": "17323",
        "type": "ndvi",
        "from_time": "2012-01-01T00:00:00.000+00:00",
        "to_time": "2012-12-31T00:00:00.000+00:00",
        "server_time": "2015-04-24T10:59:21.171+03:00"
    },
    "response": {
        "from_time": "2012-01-01T00:00:00.000+00:00",
        "to_time": "2012-12-31T00:00:00.000+00:00",
        "obtained_records": 0
    }
}

HistoricalValues/v3b

operations.cropwise.com/api/v3b/historical_values
HistoricalValues relations

    HistoricalValue belongs to field.

HistoricalValues has next attributes:

    last_value - last measured value

    last_value_date - date of last value measure

Query params

HistoricalValues/v3b has some extra params

    skip_value - skip value array, it change value to nil

HistoryItems

operations.cropwise.com/api/v3/history_items
HistoryItem relations

    HistoryItem belongs to Field

    HistoryItem belongs to Crop

    HistoryItem belongs to ProductionCycle

    HistoryItem belongs to FieldShape

HistoryItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of HistoryItem

    field_id - Cropwise Operations Platform ID of related Field

    year - year

    active - is this item active (deprecated, InventoryHistoryItem should be used)

    crop_id - Cropwise Operations Platform ID of the Crop

    variety - variety

    till_type - till type (one of: standard, strip_till, mini_till, no_till, stubble_ploughing, deep_cultivation, discing, chisel_plowing, plowing, non_inversion_tillage, direct_seeding, other)

    productivity - productivity

    (readonly) productivity_estimate - productivity estimate

    sowing_date - date of the sowing

    harvesting_date - date of the harvesting

    description - description

    additional_info - some additional info from user

    external_id - a string field for storing id of the element from an external system

    harvested_weight - weight of harvest, fill it only if you productivity accounting source is manual

    expected_yield - expected yield volume, fill it only if you productivity accounting source is manual

    yield_density - yield density

    productivity_zone - productivity zone (one of: highly_productive, medium_productive, low_productivity)

    grain_class - grain class (one of: class_1, class_2, class_3, class_4, class_5)

    irrigation_type - irrigation type (one of: surface_irrigation, localized_irrigation, drip_irrigation, sprinkler_irrigation, center_pivot_irrigation, lateral_move_irrigation, sub_irrigation, manual_irrigation, dryland, bogara)

    grain_humidity - grain humidity

    grain_garbage_admixture - grain garbage admixture

    production_cycle_id - Cropwise Operations Platform ID of related ProductionCycle

    auto_shape_detect - if this element has the value true, the system automatically determines the shape of the field, if false, the user must set the shape of the field himself

    field_shape_id - Cropwise Operations Platform ID of related FieldShape

    marketable_weight - marketable weight

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_id, year, active, crop_id, variety, sowing_date, harvesting_date, description, additional_info, external_id, harvested_weight, yield_density, production_cycle_id, field_shape_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
HistoryRelations

operations.cropwise.com/api/v3/history_relations
HistoryRelation relations

    HistoryRelation belongs to InventoryHistoryItem as parental_inventory_history_item_id

    HistoryRelation belongs to InventoryHistoryItem as inventory_history_item_id

HistoryRelation has next attributes

    (readonly) id - Cropwise Operations Platform ID of HistoryRelation

    (immutable) inventory_history_item_id - Cropwise Operations Platform ID of related InventoryHistoryItem which act as a child refference

    (immutable) parental_inventory_history_item_id - Cropwise Operations Platform ID of related InventoryHistoryItem which act as a parent refference

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Destroy Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, inventory_history_item_id, parental_inventory_history_item_id
Comparison filters by (for more info see)

created_at, updated_at
Implement

operations.cropwise.com/api/v3/implements
Implement relations

    Implement has many MachineTasks.

    Implement has many Notes.

    Implement has many Machines as :default_machines.

Implement has next attributes

    (readonly) id - Cropwise Operations Platform ID of Implement

    (readonly) name - name

    custom_name - custom name of Implement. If custom name not set, then name of implement in Cropwise Operations Platform will be 'manufacturer' + 'model'

    model - model

    manufacturer - manufactor

    year - year of production

    registration_number - registration number

    inventory_number - inventory number

    implement_type - implement type: 'subsoiler', 'cultivator', 'planter', 'sprayer', 'spreader', 'lifter', 'bunker', 'cart', 'harrow', 'graider', 'trailer', 'roller', 'ripper', 'reaper', 'compactor', 'baler', 'grass_handling', 'plow', 'brush_cutter', 'mower', 'disk', 'hindcarriage', 'barrel', 'sprinkling_machine', 'shredders', 'saw', 'feeder_wagon', 'grubber', 'blade', 'coupler', 'applicator', 'rakes_rollformers', 'fodder_mixer', 'hiller', 'bags_extractor', 'bag_packer', 'unloader', 'other'

    width - width in meters

    official_width - official width in meters

    (readonly) avatarr - avatar (see below)

    chassis_serial_number - serial number

    legal_company - legal company

    description - description

    (readonly) additional - serialized attributes

    additional_info - your system info

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Additional info

Implement support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
Avatar

{ data: { ... "avatar": { "avatar": { "url": "/system/uploads/implement/avatar/1658/avatar.png", "menu_thumb": { "url": "/system/uploads/implement/avatar/1658/menu_thumb_avatar.png" }, "thumb": { "url": "/system/uploads/implement/avatar/1658/thumb_avatar.png" }, "small": { "url": "/system/uploads/implement/avatar/1658/small_avatar.png" }, "tiny": { "url": "/system/uploads/implement/avatar/1658/tiny_avatar.png" }, "small_rounded": { "url": "/system/uploads/implement/avatar/1658/small_rounded_avatar.png" }, "tiny_rounded": { "url": "/system/uploads/implement/avatar/1658/tiny_rounded_avatar.png" } } } ... } }
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, implement_type, inventory_number, manufacturer, model, registration_number, year, chassis_serial_number, external_id, virtual, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
ImplementRegionMappingItems

operations.cropwise.com/api/v3/implement_region_mapping_items
ImplementRegionMappingItem relations

    ImplementRegionMappingItem belongs to Implement

    ImplementRegionMappingItem belongs to MachineRegion

ImplementRegionMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of ImplementRegionMappingItem

    implement_id - ID of Implement

    machine_region_id - ID of MachineRegion

    date_start - start date of mapping

    date_end - end date of mapping

    no_date_end - boolean, true if there is no end date of mapping

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

ImplementRegionMappingItem methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, implement_id, machine_region_id, date_start, date_end, no_date_end
Comparison filters by (for more info see)

date_start, date_end, created_at, updated_at
ImplementWorkTypeMappingItems

operations.cropwise.com/api/v3/implement_work_type_mapping_items
ImplementWorkTypeMappingItem relations

    ImplementWorkTypeMappingItem belongs to Implement

    ImplementWorkTypeMappingItem belongs to WorkType

ImplementWorkTypeMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of ImplementWorkTypeMappingItem

    implement_id - ID of Implement

    work_type_id - ID of WorkType

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

ImplementWorkTypeMappingItem methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, implement_id, work_type_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
InventoryHistoryItems

operations.cropwise.com/api/v3/inventory_history_items
InventoryHistoryItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of InventoryHistoryItem

    historyable_id - id of historyable object (machine_id, field_id, etc.)

    historyable_type - type of record: 'Machine', 'Implement', 'Field'

    event_start_at - date when record comes into effect

    reason - reason (see below)

    description - description

    available - boolean, is record is active

    hidden - boolean, hide object in reports and views

    external_id - a string field for storing id of the element from an external system

    (readonly)event_end_at - end date for record, calculates automatically by Cropwise Operations Platform if there are new records for historyable object

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Reasons subtypes

    if object is available: 'bought', 'taken_on_lease_start', 'granted_on_lease_end', 'temporaly_unavailable_end', 'other_available_reason'

    if object is unavailable: 'sold', 'taken_on_lease_end', 'granted_on_lease_start', 'temporaly_unavailable_start', 'other_unavailable_reason'

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, historyable_id, historyable_type, reason, description, available, hidden, external_id, created_at, updated_at
Filter by dates

Filtering from event_start_at,event_end_at equivalent to this logical expression: event_start_at <= specified date && event_end_at => specified date || event_end_at == null

    Request https://operations.cropwise.com/api/v3/inventory_history_items?event_start_at=2021-12-31T00:00&end_time=2021-12-31T00:00 - get all active objects for specified date

Comparison filters by (for more info see)

created_at, updated_at
LandDocuments

operations.cropwise.com/api/v3/land_documents
LandDocument relations

    LandDocument has many Counterparties

    LandDocument has many LandParcels

    LandDocument has many LandDocumentLandParcelMappingItems

    LandDocument has many LandDocumentCounterpartyMappingItems

LandDocument has next attributes

    (readonly) id - Cropwise Operations Platform ID of LandDocument

    document_date - date of document

    document_type - document type (see below)

    document_subtype - document subtype, can be: empty (see below)

    agent - agent name

    start_date - document start date

    end_date - document end date

    actual_end_date - date when document becomes inactive

    additional_info - some additional info

    auto_prolongation - auto prolongation (true/false)

    prolongation_months - the number of months of contract prolongation

    description - some description

    document_number - document number

    document_version - document version

    document_status - can be: empty, signed, registered

    normative_monetary_value - normative monetary value

    year_of_nmv - year of normative monetary value

    nmv_currency - normative monetary value currency (see available currencies below)

    price_per_year - price per year

    price_per_year_currency - price per year currency (see available currencies below)

    price - document price

    currency - document price currency (see available currencies below)

    share_of_land - share of land in percents (from 0 to 100)

    ownership_of_land_type - can be: empty, certificate, state_act, certificate_of_ownership

    location - location of document

    external_id - a string field for storing id of the element from an external system

    counterparty_ids - array ids of counterparties

    own_land_parcel_ids - array ids of own land parcels, for exchange document type

    counterparty_land_parcel_ids - array ids of counterparties land parcels, for exchange document type

    (readonly) protected_documents - array of protected documents (some photo, pdf, etc.). See below

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Land document types

    sold

    rented

    subrented

    rented_out

    subrented_out

    purchased

    exchange

Land document subtypes

Subtypes can only be assigned when the document type is rented.

    fixed_in_currency

    natural

    in_dollars

    fixed_in_percents_to_nmv

Available currencies

Complete list of available currency: ISO 4217. Most common:

    USD

    EUR

    RUB

    UAH

LandDocumentLandParcelMappingItem attributes

Param name: land_document_land_parcel_mapping_items_attributes.

    (readonly)id - Cropwise Operations Platform ID of LandDocumentLandParcelMappingItem

    land_document_id - Cropwise Operations Platform ID of LandDocument

    land_parcel_id- Cropwise Operations Platform ID of LandParcel

    shared_area - Area of land parcel shared within the document

    land_type - Ownership type of the land parcel

Land types: own, counterparty for exchange document type. Leave it empty for other document types.
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, document_date, document_type, agent, start_date, end_date, document_number, document_status, external_id, created_at, updated_at, price, currency, share_of_land, document_subtype, ownership_of_land_type, normative_monetary_value, year_of_nmv, nmv_currency, price_per_year, price_per_year_currency, document_version, location
Comparison filters by (for more info see)

created_at, updated_at, price, normative_monetary_value, year_of_nmv, price_per_year, document_date, start_date, end_date
Additional info

Land Document support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
LandDocumentCounterpartyMappingItem

operations.cropwise.com/api/v3/land_document_counterparty_mapping_items
LandDocumentCounterpartyMappingItem relations

    LandDocumentCounterpartyMappingItem belongs to LandDocument

    LandDocumentCounterpartyMappingItem belongs to Counterparty

LandDocumentCounterpartyMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of LandDocumentCounterpartyMappingItem

    land_document_id - id of LandDocument

    counterparty_id - id of Counterparty

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, land_document_id, counterparty_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
LandDocumentLandParcelMappingItem

operations.cropwise.com/api/v3/land_document_land_parcel_mapping_items
LandDocumentLandParcelMappingItem relations

    LandDocumentLandParcelMappingItem belongs to LandDocument

    LandDocumentLandParcelMappingItem belongs to LandParcel

LandDocumentLandParcelMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of LandDocumentLandParcelMappingItem

    land_document_id - id of LandDocument

    land_parcel_id - id of LandParcel

    land_type - land type (see below)

    shared_area - part of the area of the land parcel which was declared in the land document

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

LandDocumentLandParcelMappingItem types

    nil

    own

    counterparty

If LandDocument type is exchange there will be 2 records in LandDocumentLandParcelMappingItem One record will be with type own, another one with counterparty.

In any other case land_type will be nil
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, land_document_id, land_parcel_id, land_type, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
LandParcels

operations.cropwise.com/api/v3/land_parcels
LandParcel relations

    LandParcel belongs to FieldGroup.

LandParcel has next attributes

    (readonly) id - Cropwise Operations Platform ID of LandParcel

    field_group_id - Cropwise Operations Platform ID of FieldGroup

    cadastral_number - cadastral number

    cadastral_area - cadastral area

    cadastral_price - cadastral price

    permitted_use - permitted use

    address - address

    region - region

    country_code - country code

    (writeonly)shape_json - attribute for setting shape for LandParcel object, in GeoJSON format

    additional_info - your system info

    description - description

    planned_action - planned action type, see below

    registration_number - registration_number

    subadministrative_area_name - subadministrative area name

    village_council - village_council

    in_archive - invisible on maps if true

    external_id - a string field for storing id of the element from an external system

    (readonly) shape - series of attributes that contain original shape in different formats

    (readonly) geo_json - simplified shape in GeoJSON format

    (readonly) calculated_area

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Land parcel planned action subtypes

    'purchase' or empty

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_group_id, cadastral_number, country_code, additional_info, description, created_at, updated_at, planned_action, registration_number, subadministrative_area_name, village_council', in_archive, external_id, `document_status'
Comparison filters by (for more info see)

created_at, updated_at, cadastral_area, calculated_area, cadastral_price
Additional info

Land Parcel support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
LandParcel creation

Example:

{
    "data" : {
        "cadastral_number" : "31100",
         "country_code": "UA",
        "field_group_id": 1745,
        "shape_json": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[38.26704181,50.78766348],[38.27019573,50.7896044],[38.28013502,50.78556909],[38.27921892,50.78519345],[38.27751554,50.78404576],[38.27693223,50.78425975],[38.27649897,50.7839538],[38.27273009,50.78576243],[38.26704181,50.78766348]]]]}"
    }
}

LandParcelOwnership

operations.cropwise.com/api/v3/land_parcel_ownerships
LandParcelOwnership relations

    LandParcelOwnership belongs to LandParcel

    LandParcelOwnership belongs to Counterparty

LandParcelOwnership has next attributes

    (readonly) id - Cropwise Operations Platform ID of LandParcelOwnership

    land_parcel_id - id of LandParcel

    counterparty_id - id of Counterparty

    area

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, land_parcel_id, counterparty_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
LeafTests

operations.cropwise.com/api/v3/leaf_tests
LeafTest relations

    LeafTest belongs to Field.

LeafTest has next attributes

    (readonly) id - Cropwise Operations Platform ID of LeafTest

    field_id - Cropwise Operations Platform ID of Field

    made_at - Date when soil test has been made

    elements - Hash of elements (see Available elements below). Every element is a hash of parameters ("K": {"value": 127 }

    description - Description for the LeafTest

    attached_file - Attached file

    laboratory_name - Laboratory name

    external_id - External ID of LeafTest

    plant_part_sampled - Part of Plant that used to the LeafTest, could be one of (leaf, petiole, stem, sap, fruit, seed, other)

    crop_growth_stage - Growth stage

    lat - Latitude

    lon - Longitude

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Available elements and their measurement units

    N - Nitrogen (%)

    P - Phosphorus (%)

    K - Potassium (%)

    Ca- Calcium (%)

    Mg - Magnesium (%)

    S - Sulfur (%)

    Na - Natrium (ppm)

    Cu - Copper (ppm)

    Zn - Zinc (ppm)

    Mn - Manganese (ppm)

    B - Boron (ppm)

    Fe - Iron (ppm)

    Al - Aluminium (ppm)

    Mo - Molybdenum (ppm)

    brix - Brix (°Bx)

LeafTest creation

Example:

{
    "data" : {
        "field_id" : "123",
        "made_at": "2024-10-11",
         "plant_part_sampled": "leaf",
         "lat": 50,
         "lon": 30,
        "elements": { "K": { "value": "56" }, "Ca": { "value": "150" } }
    }
}

MachineDowntimes

operations.cropwise.com/api/v3/machine_downtimes
MachineDowntime relations

    MachineDowntime belongs to Machine

    MachineDowntime belongs to MachineDowntimeType

    MachineDowntime has many MachineDowntimeStoppingPoint

MachineDowntime has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineDowntime

    (readonly) start_time - start time for machine downtime

    (readonly) end_time - end time for machine downtime

    (readonly) duration_in_seconds - duration of downtime in seconds

    machine_downtime_type_id - ID of MachineDowntimeType

    (readonly) machine_id - ID of Machine

    status - one of type: 'unknown', 'planned', 'unplanned', 'confirmed', 'hidden'

    additional_info - some additional info

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

MachineDowntime methods

    Resources Collection

    Ids

    Single Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_id, machine_downtime_type_id, status
Comparison filters by (for more info see)

start_time, end_time, created_at, updated_at
MachineDowntimeTypes

operations.cropwise.com/api/v3/machine_downtime_types
MachineDowntimeType relations

    MachineDowntimeType has many MachineDowntime

    MachineDowntimeType belongs to MachineDowntimeTypeGroup

MachineDowntimeType has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineDowntimeType

    (readonly) standard_name - standard name of MachineDowntimeType

    custom_name - custom name of MachineDowntimeType

    machine_downtime_type_group_id - ID of MachineDowntimeTypeGroup

    additional_info - some additional info

    hidden - is it hidden (boolean)

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

MachineDowntimeType methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, hidden, machine_downtime_type_group_id, status
Comparison filters by (for more info see)

created_at, updated_at
MachineDowntimeTypeGroups

operations.cropwise.com/api/v3/machine_downtime_type_groups
MachineDowntimeTypeGroup relations

    MachineDowntimeTypeGroup has many MachineDowntimeType

MachineDowntimeTypeGroup has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineDowntimeTypeGroup

    (readonly) standard_name - standard name of MachineDowntimeTypeGroup

    custom_name - custom name of MachineDowntimeTypeGroup

    additional_info - some additional info

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

MachineDowntimeTypeGroup methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Comparison filters by (for more info see)

created_at, updated_at
MachineRegions

operations.cropwise.com/api/v3/machine_regions
MachineRegion relations

    MachineRegion has many MachineRegionMappingItem

    MachineRegion has many ImplementRegionMappingItem

MachineRegion has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineRegion

    name - name of machine region

    ancestry - ancestry for current record

    description - description

    additional_info - additional info for region

    external_id - a string field for storing id of the element from an external system

    hidden - is it hidden (boolean)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, ancestry, hidden, external_id
MachineRegionMappingItems

operations.cropwise.com/api/v3/machine_region_mapping_items
MachineRegionMappingItem relations

    MachineRegionMappingItem belongs to Machine

    MachineRegionMappingItem belongs to MachineRegion

MachineRegionMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineRegionMappingItem

    machine_id - ID of Machine

    machine_region_id - ID of MachineRegion

    date_start - start date of mapping

    date_end - end date of mapping

    no_date_end - boolean, true if there is no end date of mapping

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

MachineRegionMappingItem methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_id, machine_region_id, date_start, date_end, no_date_end
Comparison filters by (for more info see)

date_start, date_end, created_at, updated_at
MachineGroups

operations.cropwise.com/api/v3/machine_groups
MachineGroup relations

    MachineGroup has many Machines.

MachineGroup has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineGroup

    name - name

    additional_info - your system info

    description - description

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

MachineObjectIntersections

operations.cropwise.com/api/v3/machine_object_intersections
MachineObjectIntersections relations

    MachineObjectIntersections belongs to Object (Field or AdditionalObject)

    MachineObjectIntersections belongs to Machine

MachineObjectIntersections object has next attributes

    id - Cropwise Operations Platform ID of MachineObjectIntersection

    machine_id - ID of Machine that intersected some Object

    object_type - Type of object that was intersected by machine

    object_id - ID of object that was intersected by machine

    hour_start - Rounded down hour when intersection occured

    start_intersection - Exact time when intersection started

    end_intersection - Exact time when intersection ended

    created_at - time when object created

    updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

machine_id, object_type, object_id, hour_start, created_at, updated_at
Comparison filters by (for more info see)

start_intersection, end_intersection, hour_start, created_at, updated_at
MachineTaskAgriWorkPlanMappingItem

operations.cropwise.com/api/v3/machine_task_agri_work_plan_mapping_items
MachineTaskAgriWorkPlanMappingItem relations

    MachineTaskAgriWorkPlanMappingItem belongs to MachineTask.

    MachineTaskAgriWorkPlanMappingItem belongs to AgriWorkPlan.

MachineTaskAgriWorkPlanMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineTaskAgriWorkPlanMappingItem

    machine_task_id - Cropwise Operations Platform ID of MachineTask

    agri_work_plan_id - Cropwise Operations Platform ID of AgriWorkPlan

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Create Resource

    Delete Resource

    Changes

    Changes Ids

Filters by

id, machine_task_id, agri_work_plan_id
Comparison filters by (for more info see)

created_at, updated_at
MachineTaskAgroOperationMappingItem

operations.cropwise.com/api/v3/machine_task_agro_operation_mapping_items
MachineTaskAgroOperationMappingItem relations

    MachineTaskAgroOperationMappingItem belongs to MachineTask.

    MachineTaskAgroOperationMappingItem belongs to AgroOperation.

MachineTaskAgroOperationMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineTaskAgroOperationMappingItem

    machine_task_id - Cropwise Operations Platform ID of MachineTask

    agro_operation_id - Cropwise Operations Platform ID of AgroOperation

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Create Resource

    Delete Resource

    Changes

    Changes Ids

Filters by

id, machine_task_id, agro_operation_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
MachineTaskFieldMappingItem

operations.cropwise.com/api/v3/machine_task_field_mapping_items
MachineTaskFieldMappingItem relations

    MachineTaskFieldMappingItem belongs to MachineTask

    MachineTaskFieldMappingItem belongs to Field

    MachineTaskFieldMappingItem belongs to HistoryItem

MachineTaskFieldMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineTaskAgroOperationMappingItem

    machine_task_id - Cropwise Operations Platform ID of MachineTask

    field_id - Cropwise Operations Platform ID of Field

    history_item_id - Cropwise Operations Platform ID of related HistoryItem

    covered_area - covered area

    (readonly) fuel_consumption - fuel consumption

    (readonly) work_area - machine work area

    (readonly) covered_area_hourly - hourly covered area

    (readonly) work_area_hourly - hourly machine work area

    (readonly) work_distance - machine distance inside a field

    (readonly) work_distance_hourly - hourly machine distance inside a field

    (readonly) work_duration - machine work duration inside a field (seconds)

    (readonly) work_duration_hourly - hourly machine work duration inside a field (seconds)

    (readonly) work_timetable - array of time intervals, when machine was on the field

    manually_defined_covered_area - boolean, true if covered area was settled manually

    manually_defined_fuel_consumption - boolean, true if fuel consumption was settled manually

    (readonly) covered_area_by_track - covered area calculated with "first track rule"

    (readonly) covered_area_by_track_hourly - hourly covered area calculated with "first track rule"

    (readonly) stops_duration - machine stop duration inside a field (seconds)

    (readonly) stops_duration_hourly - hourly machine stop duration inside a field (seconds)

    (readonly) stops_timetable - array of time intervals, when machine stop on the field

    (readonly) sensors_data - array of data from machines sensors (see description below)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

    from_warehouse_id - Cropwise Operations Platform ID of Warehouse

    locked_to_edit - prohibition of editing sign: 'true', 'false'

    locked_at - the time when editing was disabled

Sensors data

    id - id of DataSourceParameter

    name - sensor's human readable name

    units - unit of measurement

    value - value, calculated by sensors data

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

    Update Resource. You can update external_id, covered_area and fuel_consumption considering that the relevant parameters (manually_defined_covered_area, manually_defined_fuel_consumption) are setted as true in request

Filters by

id, field_id, machine_task_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
MachineTask

operations.cropwise.com/api/v3/machine_tasks
MachineTask relations

    MachineTask belongs to WorkType. Required.

    MachineTask belongs to Machine. Required.

    MachineTask belongs to Implement.

    MachineTask belongs to User as driver.

    MachineTask has_many Fields.

MachineTask has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineTask

    machine_id - Cropwise Operations Platform ID of Machine

    start_time - start date

    end_time - end date

    action_type — LEGACY! Use work_type_id instead.

    action_subtype — LEGACY! Use work_type_id instead.

    work_type_id - ID of WorkType.

    driver_id - Cropwise Operations Platform ID of User

    implement_id - Cropwise Operations Platform ID of Implement

    work_for_contractors - is this work for contractors (true/false)

    work_for_land_owners - is this work for owners (true/false)

    season - the season (year in format "yyyy")

    real_implement_width - real Implement width (required for Implements with variable width)

    total_distance - total distance

    related_agri_task_ids - related agri machine task ids (array of ids)

    related_transportation_task_ids - related transportation machine task ids (array of ids)

    (readonly) total_distance_hourly - total distance hourly

    (readonly) work_distance - work distance

    (readonly) work_distance_hourly - work distance hourly

    work_area - work area

    (readonly) work_area_hourly - work area hourly

    (readonly) covered_area - covered area

    (readonly) covered_area_hourly - covered area hourly

    (readonly) work_duration - work duration

    (readonly) work_duration_hourly - work duration hourly

    (readonly) work_timetable - work timetable

    additional_info - your system info

    description - description

    (readonly) engine_work_duration_on_fields - engine work duration on fields (in seconds)

    (readonly) engine_work_duration_on_road - engine work duration on road (in seconds)

    (readonly) locked_at - time when task was locked

    (readonly) locked_to_edit - locked to edit

    (readonly) sensors_data - array of aggregated data from machines sensors (see description below)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

    (readonly) plan_speed_min - minimum planned speed

    (readonly) plan_speed_max - maximum planned speed

    (readonly) start_fuel_level - fuel level at start of machine task

    (readonly) end_fuel_level - fuel level at the end of the machine task

    (readonly) refuel - refueled during machine task

Action subtypes

    'agri': 'spraying', 'discing', 'plowing', 'cultivation', 'subsoiling', 'sowing', 'over_sowing', 'spreading', 'harrowing', 'rolling', 'harvesting', 'other'

    'transport': 'grain', 'seeds', 'water', 'fertilizers', 'chemicals', 'machinery', 'spare_parts', 'people', 'other'

    'service': 'field_works', 'field_monitoring', 'service_works', 'admin_works', 'service_patrol', 'other'

    'other': 'garbage_works', 'road_works', 'loading_works', 'fuel_tanking', 'works_in_territory', 'transfer', 'snow_removal', 'other'

Sensors data

    id - id of DataSourceParameter

    name - sensor's human readable name

    units - unit of measurement

    value - value, calculated by sensors data

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_id, driver_id, implement_id, season, work_type_id, status, external_id, locked_to_edit
Comparison filters by (for more info see)

start_time, end_time, created_at, updated_at, locked_at
MachineTask/v3a

operations.cropwise.com/api/v3a/machine_tasks
MachineTask relations

    MachineTask belongs to WorkType. Required.

    MachineTask belongs to Machine. Required.

    MachineTask belongs to Implement.

    MachineTask belongs to User as driver.

    MachineTask has_many Fields.

MachineTask has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineTask

    machine_id - Cropwise Operations Platform ID of Machine

    start_time - start date

    end_time - end date

    action_type — LEGACY! Use work_type_id instead.

    action_subtype — LEGACY! Use work_type_id instead.

    work_type_id - ID of WorkType.

    driver_id - Cropwise Operations Platform ID of User

    implement_id - Cropwise Operations Platform ID of Implement

    work_for_contractors - is this work for contractors (true/false)

    work_for_land_owners - is this work for owners (true/false)

    season - the season (year in format "yyyy")

    real_implement_width - real Implement width (required for Implements with variable width)

    total_distance - total distance

    (readonly) work_distance - work distance

    work_area - work area

    (readonly) covered_area - covered area

    (readonly) work_duration - work duration

    (readonly) work_timetable - work timetable

    additional_info - your system info

    description - description

    (readonly) engine_work_duration_on_fields - engine work duration on fields (in seconds)

    (readonly) engine_work_duration_on_road - engine work duration on road (in seconds)

    (readonly) locked_at - time when task was locked

    (readonly) locked_to_edit - locked to edit

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

    (readonly) plan_speed_min - minimum planned speed

    (readonly) plan_speed_max - maximum planned speed

    (readonly) start_fuel_level - fuel level at start of machine task

    (readonly) end_fuel_level - fuel level at the end of the machine task

    (readonly) refuel - refueled during machine task

Action subtypes

    'agri': 'spraying', 'discing', 'plowing', 'cultivation', 'subsoiling', 'sowing', 'over_sowing', 'spreading', 'harrowing', 'rolling', 'harvesting', 'other'

    'transport': 'grain', 'seeds', 'water', 'fertilizers', 'chemicals', 'machinery', 'spare_parts', 'people', 'other'

    'service': 'field_works', 'field_monitoring', 'service_works', 'admin_works', 'service_patrol', 'other'

    'other': 'garbage_works', 'road_works', 'loading_works', 'fuel_tanking', 'works_in_territory', 'transfer', 'snow_removal', 'other'

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_id, driver_id, implement_id, season, work_type_id, status, external_id, created_at, updated_at
Comparison filters by (for more info see)

start_time, end_time, season, created_at, updated_at
Additional info

Machine Task support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)

MachineTaskResponsibleUserAssignments

operations.cropwise.com/api/v3/machine_task_responsible_user_assignments
MachineTaskResponsibleUserAssignments relations

    MachineTaskResponsibleUserAssignments belongs to MachineTask

    MachineTaskResponsibleUserAssignments belongs to User as a responsible

MachineTaskResponsibleUserAssignments has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineTaskResponsibleUserAssignments

    (immutable) machine_task_id - Cropwise Operations Platform ID of MachineTask

    (immutable) responsible_user_id - Cropwise Operations Platform ID of responsible User

    external_id - a string field for storing id of the element from an external system

    idempotency_key - The idempotency key transmitted during the request, if any.

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_task_id, responsible_user_id, external_id, idempotency_key
Comparison filters by (for more info see)

created_at, updated_at

MachineTaskGroupFolderMappingItems

operations.cropwise.com/api/v3/machine_task_group_folder_mapping_items
MachineTaskGroupFolderMappingItems relations

    MachineTaskGroupFolderMappingItems belongs to MachineTask

    MachineTaskGroupFolderMappingItems belongs to GroupFolder as a work region

MachineTaskGroupFolderMappingItems has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineTaskGroupFolderMappingItems

    (immutable) machine_task_id - Cropwise Operations Platform ID of MachineTask

    (immutable) group_folder_id - Cropwise Operations Platform ID of GroupFolder as a work region

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_task_id, group_folder_id, external_id
Comparison filters by (for more info see)

created_at, updated_at
Machine

operations.cropwise.com/api/v3/machines
Machine relations

    Machine belongs to MachineGroup

    Machine belongs to Implement as default_implement.

    Machine belongs to Avatar.

    Machine belongs to MachineryManufacturer

    Machine belongs to MachineryModel

    Machine has many MachineTasks.

    Machine has many HarvestWeighings.

    Machine has many Notes.

    Machine has many GpsLoggerMappingItems.

    Machine has many DataSourceGpsLoggers.

Machine has next attributes

    (readonly) id - Cropwise Operations Platform ID of Machine

    (readonly) name - name of Machine

    custom_name - custom name of Machine. If custom name not set, then name of machine in Cropwise Operations Platform will be 'manufacturer ' + 'model'

    model - model (still supported, requaried, 'machinery_model_id' has priority)

    manufacturer - manufacturer (outdated but still supported, prefere 'machinery_manufacturer_id')

    machinery_model_id - Cropwise Operations Platform ID of MachineryModel

    year - year of production

    registration_number - registration number

    inventory_number - inventory number

    machine_group_id - Cropwise Operations Platform ID of MachineGroup

    machine_type - machine type: 'agri', 'transport'

    machine_subtype - machine subtype: 'lorrie', 'tipper', 'car', 'fuel_bowser', 'harvester', 'sprayer', 'tractor', 'buldozer', 'telehandler', 'maintenance', 'minibus', 'truck_crane', 'other'

    avatar_id — Cropwise Operations Platform ID of Avatar

    (readonly) avatar - legacy

    chassis_serial_number - chassis serial number

    engine_serial_number - engine serial number

    engine_power - engine power

    weight - machine weight

    height - machine height

    width - machine width

    length - machine length

    engine_capacity - machine engine capacity

    fuel_type - fuel type: 'gas', 'diesel', 'natural_gas', 'other'. (Backward compatibility. For new custom fuel types will return only its category)

    fuel_type_id - Cropwise Operations Platform ID of fuel type

    fuel_tank_size - fuel tank size

    fuel_consumption_norm - fuel consumption norm

    legal_company - legal company

    description - description

    default_implement_id - Cropwise Operations Platform ID of Implement

    additional_1 - serialized attributes

    additional_2 - serialized attributes

    additional_info - your system info

    external_id - a string field for storing id of the element from an external system

    machinery_manufacturer_id - Cropwise Operations Platform ID of Machinery Manufacturer

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, chassis_serial_number, engine_serial_number, inventory_number, machine_subtype machine_type, model, manufacturer, registration_number, year, machine_group_id, default_implement_id, default_driver_id, external_id, phone_number, fuel_type_id
Comparison filters by (for more info see)

created_at, updated_at
Additional info

Machine support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
FetchAvailableMachinesForWorkAtCoordinates

GET operations.cropwise.com/api/v3/machines/available_for_work_at_coordinates

Return all active machines within search radius from centerpoint. To default machine attributes in responce added next ones:

    lat - latitude of point where machine was last seen active

    long - longitude of point where machine was last seen active

    last_time - last time when machine was seen active

Required parameters

You need to pass next body param to this request:

    lat - latitude of centerpoint for search

    long - longitude of centerpoint for search

Optional parameters

    at_time - timestamp when to search available machines

    search_radius - search radius in metres around centerpoint (default: 50 000m)

Example request get list of items:

https://operations.cropwise.com/api/v3/machines/available_for_work_at_coordinates?lat=0&long=0&at_time=2000-01-01+12%3A30%3A30%2B00%3A00&search_radius=10000
Example success response:

{
    "data": 
    {
        "available_machines":
        [
            {
                "lat": 51.21087333,
                "long": 31.34297833,
                "last_time": "2025-06-04T13:47:32.000+03:00",
                "id": 1,
                "name": "Machine",
                ... other machine attributes
            },
        ]
    },
}

FetchAvailableMachineIdsForWorkAtCoordinates

GET operations.cropwise.com/api/v3/machines/available_for_work_at_coordinates_ids

Return only active machines IDs within search radius from centerpoint
Required parameters

You need to pass next body param to this request:

    lat - latitude of centerpoint for search

    long - longitude of centerpoint for search

Optional parameters

    at_time - timestamp when to search available machines

    search_radius - search radius in metres around centerpoint (default: 50 000m)

Example request get list of items:

https://operations.cropwise.com/api/v3/machines/available_for_work_at_coordinates?lat=0&long=0&at_time=2000-01-01+12%3A30%3A30%2B00%3A00&search_radius=10000
Example success response:

{
    "data": 
    {
        "available_machine_ids":
        [
            1,
            2,
            ...
        ]
    },
}

Machine GpsAggregatedData ⚠️

⚠️⚠️⚠️ Testing stage, may be changed !!! ⚠️⚠️⚠️

operations.cropwise.com/api/v3/machine_gps_aggregated_data
Filters by

from_time, to_time, machine_id

Note: all filter parameters are required!
it returns records aggregated by each hour with next attributes

    id - internal record id

    hour_start - beginning of hour for each grouped record

    last_time - time of last GPS data for this hour

    last_lat - last known latitude for this hour

    last_long - last known longitude for this hour

    last_alt - last known altitude for this hour

    avg_speed - average speed for this hour

    max_speed - maximum speed for this hour

    distance - distance passed for this hour

    first_move_time - time of first move for this hour

    last_move_time - time of last move for this hour

MachineWorkPlan

operations.cropwise.com/api/v3/machine_work_plans
MachineWorkPlan relations

    MachineWorkPlan belongs to AgriWorkPlan

    MachineWorkPlan has many MachineWorkPlanRows

MachineWorkPlan has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineWorkPlan

    agri_work_plan_id - Cropwise Operations Platform ID of AgriWorkPlan

    color - color of MachineWorkPlan

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

MachineWorkPlanRow

operations.cropwise.com/api/v3/machine_work_plan_rows
MachineWorkPlanRow relations

    MachineWorkPlanRow belongs to MachineWorkPlan

    MachineWorkPlanRow belongs to Machine

    MachineWorkPlanRow belongs to Implement

    MachineWorkPlanRow has many MachineWorkPlanItems

MachineWorkPlanRow has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineWorkPlanRow

    machine_work_plan_id - Cropwise Operations Platform ID of MachineWorkPlan

    machine_id - Cropwise Operations Platform ID of agri work plan

    implement_id - Cropwise Operations Platform ID of agri work plan

    ind - MachineWorkPlanRow index in MachineWorkPlan

    rate - rate

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

MachineWorkPlanItem

operations.cropwise.com/api/v3/machine_work_plan_items
MachineWorkPlanItem relations

    MachineWorkPlanItem belongs to MachineWorkPlanRow

MachineWorkPlanItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineWorkPlanItem

    machine_work_plan_row_id - Cropwise Operations Platform ID of agri work plan

    date - date MachineWorkPlanItem assigned to

    rate - rate

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

MachineryManufacturer

operations.cropwise.com/api/v3/machinery_manufacturers
MachineryManufacturer relations

    MachineryManufacturer has many Machines

    MachineryManufacturer has many MachineryModels

MachineryManufacturer has next attributes

    (readonly) id - Cropwise Operations Platform ID of MachineryManufacturer

    machine_manufacturer - Machine manufacturer sign (boolean)

    implement_manufacturer - Implement manufacturer sign (boolean)

    standard_name - Machine manufacturer standard name

    custom_name - Machine manufacturer custom name

    description - some text description for Machine manufacturer

    hidden - is it hidden (boolean)

    external_id - a string field for storing id of the element from an external system

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

MachineryModel

operations.cropwise.com/api/v3/machinery_models
MachineryModel relations

    MachineryModel has many Machines

    MachineryModel belongs to MachineryManufacturer

MachineryModel has next attributes

    id - Cropwise Operations Platform ID of MachineryModel

    machinery_manufacturer_id - Cropwise Operations Platform ID of MachineryManufacturer

    machinery_type - the sign sign of belonging to Machines or Implements

    additional_info - Additional info

    hidden - is it hidden (boolean)

    external_id - a string field for storing id of the element from an external system

    name - name

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

MaintenanceType

operations.cropwise.com/api/v3/maintenance_types
MaintenanceType relations

    MaintenanceType belongs to MaintenanceTypeGroup

MaintenanceType has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenanceType

    maintenance_type_group_id - Cropwise Operations Platform ID of object for which this record

    name - name of group

    description - some text description for MaintenanceTypeGroup

    external_id - a string field for storing id of the element from an external system

    hidden - is it hidden (boolean)

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

MaintenanceTypeGroup

operations.cropwise.com/api/v3/maintenance_type_groups
MaintenanceTypeGroup relations

    MaintenanceTypeGroup has many MaintenanceTypes

MaintenanceTypeGroup has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenanceRecord

    name - name of group

    description - some text description for MaintenanceTypeGroup

    external_id - a string field for storing id of the element from an external system

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

MaintenanceRecord

operations.cropwise.com/api/v3/maintenance_records
MaintenanceRecord relations

    MaintenanceRecord belongs to Machine

    MaintenanceRecord belongs to Implement

    MaintenanceRecord belongs to MaintenancePlan (optional)

    MaintenanceRecord has many MaintenanceRecordRows

    MaintenanceRecord has many MaintenanceRecordResponsibleUserAssignments

MaintenanceRecord has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenanceRecord

    maintainable_type - type of object for which this record: Machine,Implement

    maintainable_id - Cropwise Operations Platform ID of object for which this record

    maintenance_plan_id - Cropwise Operations Platform ID of object for which this record

    start_time - start time for maintenance

    end_time - end time for maintenance

    mileage - technic's current mileage value, km

    motohours - technic's current motohours value, seconds

    status - type: 'planned', 'in_progress', 'done', 'canceled'

    description - some text description for record

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, status, maintainable_id, maintainable_type, maintenance_plan_id
Comparison filters by (for more info see)

start_time, end_time, created_at, updated_at
MaintenanceRecordRow

operations.cropwise.com/api/v3/maintenance_record_rows
MaintenanceRecordRow relations

    MaintenanceRecordRow belongs to MaintenanceRecord

    MaintenanceRecordRow belongs to MaintenanceType

    MaintenanceRecordRow has many SpareParts

MaintenanceRecordRow has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenanceRecordRow

    maintenance_record_id - Cropwise Operations Platform ID of object for which this record

    maintenance_type_id - Cropwise Operations Platform ID of object for which this record (see MaintenanceType)

    repair_stage - repair stage (see below)

    description - some text description for row

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Repair stages

    problem_identifying

    waiting_spareparts

    waitiing_for_dealer_service

    repair_works

    testing

    postpone

    other

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, maintenance_record_id, maintenance_type_id, repair_stage
MaintenanceRecordRowSparePartMappingItem

operations.cropwise.com/api/v3/maintenance_record_row_spare_part_mapping_items
MaintenanceRecordRowSparePartMappingItem relations

    MaintenanceRecordRow belongs to MaintenanceRecordRow

    MaintenanceRecordRow belongs to SparePart

MaintenanceRecordRowSparePartMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenanceRecordRowSparePartMappingItem

    maintenance_record_row_id - Cropwise Operations Platform ID of MaintenanceRecordRow

    spare_part - Cropwise Operations Platform ID of SparePart

    quantity - quantity

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, maintenance_record_row_id, spare_part_id
MaintenanceRecordResponsibleUserAssignment

operations.cropwise.com/api/v3/maintenance_record_responsible_user_assignments
MaintenanceRecordResponsibleUserAssignment relations

    MaintenanceRecordResponsibleUserAssignment belongs to MaintenanceRecord

    MaintenanceRecordResponsibleUserAssignment belongs to User

MaintenanceRecordResponsibleUserAssignment has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenanceRecordResponsibleUserAssignment

    maintenance_record_id - Cropwise Operations Platform ID of MaintenanceRecord

    responsible_user_id - Cropwise Operations Platform ID of User

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource (deprecated, please use /api/v3/responsible_user_mapping_items)

    Update Resource (deprecated, please use /api/v3/responsible_user_mapping_items)

    Delete Resource (deprecated, please use /api/v3/responsible_user_mapping_items)

    Changes

    Changes Ids

    Mass Request

Filters by

id, maintenance_record_id, responsible_user_id
MaintenancePlan

operations.cropwise.com/api/v3/maintenance_plans
MaintenancePlan relations

    MaintenancePlan belongs to responsible user

    MaintenancePlan has many MaintenancePlanRows

MaintenancePlan has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenancePlan

    responsible_user_ids - an array of Users Cropwise Operations Platform IDs of responsible for MaintenancePlan implementation

    plan_type - type: 'implement', 'machine'

    name - name of MaintenancePlan

    settings - jsonb field, contain plan's machines/implement conditions (see example below)

    description - some text description for record

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, external_id
MaintenancePlan settings example

for machines: {"machine_group_ids"=>["1"], "excluded_machine_ids"=>["11"], "included_machine_ids"=>["373", "4702"]}

for implements: {"implement_type_ids"=>["planter"], "excluded_implement_ids"=>["4289"], "included_implement_ids"=>["210"]}
MaintenancePlanRow

operations.cropwise.com/api/v3/maintenance_plan_rows
MaintenancePlanRow relations

    MaintenancePlanRow belongs to MaintenancePlan

    MaintenancePlanRow belongs to MaintenanceType

    MaintenancePlanRow has many SpareParts

MaintenancePlanRow has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenancePlanRow

    maintenance_plan_id - Cropwise Operations Platform ID of object for which this record (see MaintenancePlan)

    maintenance_type_id - Cropwise Operations Platform ID of object for which this record (see MaintenanceType)

    mileage - mileage periodic condition, km

    motohours - motohours periodic condition, hours

    interval - time interval periodic condition, seconds

    external_id - a string field xfor storing id of the element from an external system

    description - some text description for MaintenancePlanRow

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, maintenance_plan_id, maintenance_type_id, external_id
MaintenancePlanRowSparePartMappingItem

operations.cropwise.com/api/v3/maintenance_plan_row_spare_part_mapping_items
MaintenanceRecordRowSparePartMappingItem relations

    MaintenancePlanRow belongs to MaintenancePlanRow

    MaintenancePlanRow belongs to SparePart

MaintenanceRecordRowSparePartMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of MaintenancePlanRowSparePartMappingItem

    maintenance_plan_row_id - Cropwise Operations Platform ID of MaintenancePlanRow

    spare_part - Cropwise Operations Platform ID of SparePart

    quantity - quantity

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, maintenance_plan_row_id, spare_part_id
ManualTask

operations.cropwise.com/api/v3/manual_tasks
ManualTask relations

    ManualTask belongs to WorkType. Required.

    ManualTask belongs to User as supervisor. Required.

    ManualTask has many ManualTaskFieldMappingItems.

    ManualTask has many ManualTaskAssignments.

ManualTask has next attributes

    (readonly) id - Cropwise Operations Platform ID of ManualTask

    supervisor_id - Cropwise Operations Platform ID of User

    work_type_id - Cropwise Operations Platform ID of WorkType

    season - the season (year in format "yyyy") of manual task

    start_time - start date of manual task

    end_time - end date of manual task

    status - status of manual task: planned, in_progress, confirmed, done

    description - description of manual task

    additional_info - some additional info

    (readonly) created_at - time when object was created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, supervisor_id, work_type_id, season, status
Comparison filters by (for more info see)

start_time, end_time, created_at, updated_at, season
Sorting by (for more info see)

id, start_time, end_time, created_at, updated_at
Request body example

{
    "data": {
        "supervisor_id": 280287,
        "work_type_id": 1,
        "season": 2024,
        "start_time": "2024-08-27T02:00:00+02:00",
        "end_time": "2024-08-28T01:59:00+02:00",
        "status": "planned",
        "description": "",
        "additional_info": "",
        "manual_task_field_mapping_items_attributes": [
            {
                "field_id": 587,
                "history_item_id": 14087
            }
        ],
        "manual_task_assignments_attributes": [
            {
                "field_id": 1915,
                "worker_id": 264589,
                "work_result": 1337
            }
        ]
    }
}

ManualTaskFieldMappingItem

operations.cropwise.com/api/v3/manual_task_field_mapping_items
ManualTaskFieldMappingItem relations

    ManualTaskFieldMappingItem belongs to ManualTask. Required.

    ManualTaskFieldMappingItem belongs to Field. Required.

    ManualTaskFieldMappingItem belongs to HistoryItem.

ManualTaskFieldMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of ManualTaskFieldMappingItem

    manual_task_id - Cropwise Operations Platform ID of ManualTask

    field_id - Cropwise Operations Platform ID of Field

    history_item_id - Cropwise Operations Platform ID of HistoryItem

    (readonly) created_at - time when object was created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, manual_task_id, field_id, history_item_id
Comparison filters by (for more info see)

created_at, updated_at
Sorting by (for more info see)

id, created_at, updated_at
ManualTaskAssignment

operations.cropwise.com/api/v3/manual_task_assignments
ManualTaskAssignment relations

    ManualTaskAssignment belongs to ManualTask. Required.

    ManualTaskAssignment belongs to Field. Required.

    ManualTaskAssignment belongs to User as worker. Required.

ManualTaskAssignment has next attributes

    (readonly) id - Cropwise Operations Platform ID of ManualTaskAssignment

    manual_task_id - Cropwise Operations Platform ID of ManualTask

    field_id - Cropwise Operations Platform ID of Field

    worker_id - Cropwise Operations Platform ID of User

    work_result - work result of worker

    (readonly) created_at - time when object was created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, manual_task_id, field_id, worker_id
Comparison filters by (for more info see)

work_result, created_at, updated_at
Sorting by (for more info see)

id, work_result, created_at, updated_at
MtfmiApplicationMixItem

⚠ ️This endpoint only available if MachineTask applications is enabled to company account. Contact support to enable it.

operations.cropwise.com/api/v3/mtfmi_application_mix_items
MtfmiApplicationMixItem relations

    MtfmiApplicationMixItem belongs to MachineTask.

    MtfmiApplicationMixItem belongs to Field.

    MtfmiApplicationMixItem belongs MachineTaskFieldMappingItem (optional and set automatically through Field)

MachineTaskFieldMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of MtfmiApplicationMixItem

    machine_task_id - Cropwise Operations Platform ID of MachineTask

    field_id - Cropwise Operations Platform ID of Field

    date_at - application date, should be in MachineTask start_time and end_time range

    applicable_type - Cropwise Operations Platform type of applicable: "Seed", "Fertilizer", "Chemical"

    applicable_id - Cropwise Operations Platform ID of Applicable

    fact_amount - actual amount, integer value in range 0..100_000_000

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

    Update Resource

Filters by

id, applicable_id, applicable_type, external_id
Comparison filters by (for more info see)

created_at, updated_at
Notes

operations.cropwise.com/api/v3/notes
Note relations

    Note belongs to User.

    Note belongs to notable (Field, Machine, Implement, AdditionalObject).

Note has next attributes

    (readonly) id - Cropwise Operations Platform ID of Note

    notable_id - Cropwise Operations Platform ID of notable (Field, Machine or Implement)

    notable_type - type: 'Field', 'Machine', 'Implement'

    (readonly) user_id - Cropwise Operations Platform ID of User

    title - title

    description - description, note

    (readonly) photo1 - photo 1, see below

    (readonly) photo2 - photo 2, see below

    (readonly) photo3 - photo 3, see below

    (readonly) photo1_md5 - photo1 md5 digest

    (readonly) photo2_md5 - photo2 md5 digest

    (readonly) photo3_md5 - photo3 md5 digest

    created_by_user_at - time when object created on user system/device

    updated_by_user_at - last time when object was updated on user system/device

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Photo

{ "data": { ... "photo1": { "photo1": { "url": "/system/uploads/note/photo1/1495/photo.jpg", "preview_200": { "url": "/system/uploads/note/photo1/1495/preview_200_photo.jpg" }, "preview_400": { "url": "/system/uploads/note/photo1/1495/preview_400_photo.jpg" }, "preview_1000": { "url": "/system/uploads/note/photo1/1495/preview_1000_photo.jpg" } } }, ... "photo1_md5": "ff272eff6ef234862a4239b6e4717dd6", ... } }
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Notes/v3a

operations.cropwise.com/api/v3a/notes
Note relations

    Note belongs to User.

    Note belongs to notable (Field, Machine, Implement, AdditionalObject).

Note has next attributes

    (readonly) id - Cropwise Operations Platform ID of Note

    notable_id - Cropwise Operations Platform ID of notable (Field, Machine or Implement)

    notable_type - type: 'Field', 'Machine', 'Implement'

    (readonly) user_id - Cropwise Operations Platform ID of User

    title - title

    description - description, note

    (readonly) photo1 - photo 1, see below

    (readonly) photo2 - photo 2, see below

    (readonly) photo3 - photo 3, see below

    (readonly) photo1_md5 - photo1 md5 digest

    (readonly) photo2_md5 - photo2 md5 digest

    (readonly) photo3_md5 - photo3 md5 digest

    created_by_user_at - time when object created on user system/device

    updated_by_user_at - last time when object was updated on user system/device

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Photo

{ "data": { ... "photo1": { "photo1": { "url": "/system/uploads/note/photo1/1495/photo.jpg", "preview_200": { "url": "/system/uploads/note/photo1/1495/preview_200_photo.jpg" }, "preview_400": { "url": "/system/uploads/note/photo1/1495/preview_400_photo.jpg" }, "preview_1000": { "url": "/system/uploads/note/photo1/1495/preview_1000_photo.jpg" } } }, ... "photo1_md5": "ff272eff6ef234862a4239b6e4717dd6", ... } }
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

NutritionPlans

operations.cropwise.com/api/v3/nutrition_plans
NutritionPlan relations

    NutritionPlan belongs to Field.

NutritionPlan has next attributes

    (readonly) id - Cropwise Operations Platform ID of NutritionPlan

    field_id - Cropwise Operations Platform ID of Field

    source_type - one of type: 'yara', 'phos_agro'

    (readonly) plan_type - one of type: 'manual', 'auto'

    season - NutritionPlan season, integer (only 1 NutritionPlan per season on Field)

    (readonly) status - one of type: 'pending', 'enabled'

    manual_yield - planned yield, centner

    (readonly) target_yield - auto yield value will be used if manual_yield blank, centner

    calculate_params - calculate params only for 'phos_agro', see below

    soil_test_id - ID of SoilTest from this Field, all supported SoilTest values (like kalium, phosphorus, nitrogenium) will be applyed to NutritionPlan params.

    external_id - external ID, max 255 chars

    (readonly) demand_data - calculated demand data, see below

    (readonly) external_products - calculated external products, see below

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

calculate_params

example when source_type='phos_agro'

    {
        "humus": 4.4,
        "acidity": 6.2,
        "density": 1.2,
        "weedinessId": "middle",
        "soilTextureId": "light-loamy",
        "topsoilThickness": 20,
        "soilNutrients": {
            "kalium": 11,
            "phosphorus": 22,
            "nitrogenium": 33
        }
    }

demand_data

example when source_type='phos_agro'

    {
        "K": 78.36,
        "N": 77.3,
        "P": 42.97,
        "units": "kg_per_ha",
        "KTotal": 7702.79,
        "NTotal": 7598.59,
        "PTotal": 4223.95
    }

external_products

example when source_type='phos_agro'

    [
      {
        id: "11-111111-22222",
        name: "Жидкое удобрение",
        KTotal: nil,
        NTotal: 11.0,
        PTotal: 37.0,
        amount: 1.17,
        image_url: "https://shop.phosagro.com/Test2x.png",
        amount_unit: "Т",
        description: "Жидкое азотно‑фосфорное удобрение",
        growth_stage_id: "spring"
      },
      {
        id: "22-222222-22222",
        name: "Жидкое удобрение 2",
        KTotal: 11,
        NTotal: 22.0,
        PTotal: 33.0,
        amount: 2.05,
        image_url: "https://shop.phosagro.com/Test2_2x.png",
        amount_unit: "Т",
        description: "Жидкое азотно‑фосфорное удобрение",
        growth_stage_id: "autumn"
      }
    ]

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_id, source_type, plan_type, season, status, external_id
Comparison filters by (for more info see)

created_at, updated_at
OdometerStates

operations.cropwise.com/api/v3/odometer_states
OdometerState relations

    OdometerState belongs to Machine.

OdometerState has next attributes

    (readonly) id - Cropwise Operations Platform ID of OdometerState

    machine_id - Cropwise Operations Platform ID of Machine

    manual_distance - manual distance, km

    manual_engine_work_duration - manual engine work duration, seconds

    measuring_time - time when measured

    (readonly) calculated_distance - calculated distance, km

    (readonly) calculated_engine_work_duration - calculated engine work duration, seconds

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, machine_id, created_at, updated_at
Comparison filters by (for more info see)

manual_distance, calculated_distance, manual_engine_work_duration, calculated_engine_work_duration, measuring_time, created_at, updated_at
PersonalIdentifiers

operations.cropwise.com/api/v3/personal_identifiers
PersonalIdentifiers relations

    PersonalIdentifiers has many Equipment assignments

PersonalIdentifiers has next attributes

    (readonly) id - Cropwise Operations Platform ID of PersonalIdentifiers

    uid - unique identifier for object (RFiD, iButton etc.)

    description - identifier description

    external_id - external ID

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Additional info

description and external_id are optional fields.
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

PlanetSubscription

operations.cropwise.com/api/v3/planet_subscriptions
PlanetSubscription relations

    PlanetSubscription belongs to Field

    PlanetSubscription belongs to FieldShape

PlanetSubscription has next attributes

    (readonly) id - Cropwise Operations Platform ID of PlanetSubscription

    field_id - Cropwise Operations Platform ID of related Field

    field_shape_id - Cropwise Operations Platform ID of related FieldShape

    (readonly) planet_uuid - Unique ID of the subscription on Planet platform

    start_date - Date when subscription starts

    end_date - Date when subscription ends

    (readonly) billing_year - Billing year (Current year)

    (readonly) uniq_area - area of the geometry affected by subscription

    (readonly) geometry - WKT representation of subscribed geometry

    (readonly) status - activity status

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Status types

    (active) pending

    (active) processed

    (inactive) failed

    (inactive) canceled

Additional info

field_id is optional while field_shape_id is present and vice versa.
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Cancel

    Changes

    Changes Ids

    Mass Request

Filters by

id, planet_uuid, field_shape_id, status, billing_year, field_id
Comparison filters by (for more info see)

created_at, updated_at, start_date, end_date
PlantThreat

operations.cropwise.com/api/v3/plant_threats
PlantThreat relations

    PlantThreat has many FieldScoutReportThreatMappingItems.

    PlantThreat has many FieldScoutReports

    PlantThreat has many PlantThreatVulnerableCropAssignments

    PlantThreat has many VulnerableCrops

Plant threat has next attributes

    (readonly) id - Cropwise Operations Platform ID of PlantThreat

    (readonly) name - name

    custom_name - custom name of PlantThreat

    (readonly) standard_name - standard name of PlantThreat

    code - code of threat

    threat_type - type: 'weed', 'insect', 'disease', 'other', ...

    threat_subtype - subtype

    external_id - a string field xfor storing id of the element from an external system

    additional_info - your system info

    description - some description

    visible - is it visible (boolean)

    range - infection transfer distance

    latin_name - latin name of PlantThreat

    (readonly) economic_threshold_damage - economic threshold damage (string)

    (readonly) image1 - image 1, see below

    (readonly) image2 - image 2, see below

    (readonly) image3 - image 3, see below

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

PlantTreat types

    Weed

    Insect

    Disease

    Nematodes

    Nutrition_problem

    Damaged_area

    Technological_mistake

    Other

Images

{ "data": { ... "image1": { "image1": { "url": "/system/uploads/plant_threat/image1/1/avatar.png", "thumb_400": { "url": "/system/uploads/plant_threat/image1/1/thumb_400_avatar.png" }, "thumb_200": { "url": "/system/uploads/plant_threat/image1/1/thumb_200_avatar.png" }, "thumb": { "url": "/system/uploads/plant_threat/image1/1/thumb_avatar.png" }, "small": { "url": "/system/uploads/plant_threat/image1/1/small_avatar.png" }, "tiny": { "url": "/system/uploads/plant_threat/image1/1/tiny_avatar.png" }, "small_rounded": { "url": "/system/uploads/plant_threat/image1/1/small_rounded_avatar.png" }, "tiny_rounded": { "url": "/system/uploads/plant_threat/image1/1/tiny_rounded_avatar.png" } } }, ... } }
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

PlantThreat/v3a

operations.cropwise.com/api/v3a/plant_threats
PlantThreat relations

    PlantThreat has many FieldScoutReportThreatMappingItems.

    PlantThreat has many FieldScoutReports

    PlantThreat has many PlantThreatVulnerableCropAssignments

    PlantThreat has many VulnerableCrops

Plant threat has next attributes

    (readonly) id - Cropwise Operations Platform ID of PlantThreat

    name - name

    custom_name - custom name of PlantThreat

    standard_name - standard name of PlantThreat

    code - code of threat

    threat_type - type: 'weed', 'insect', 'disease', 'other', ...

    threat_subtype - subtype

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - some description

    visible - is it visible (boolean)

    range - infection transfer distance

    latin_name - latin name of PlantThreat

    (readonly) economic_threshold_damage - economic threshold damage (string)

    (readonly) image1 - image 1, see below

    (readonly) image2 - image 2, see below

    (readonly) image3 - image 3, see below

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

PlantTreat types

    Weed

    Insect

    Disease

    Nematodes

    Nutrition_problem

    Damaged_area

    Technological_mistake

    Other

Images

{ "data": { ... "image1": { "url": "/system/uploads/plant_threat/image1/1/avatar.png", "thumb_400": { "url": "/system/uploads/plant_threat/image1/1/thumb_400_avatar.png" }, "thumb_200": { "url": "/system/uploads/plant_threat/image1/1/thumb_200_avatar.png" }, "thumb": { "url": "/system/uploads/plant_threat/image1/1/thumb_avatar.png" }, "small": { "url": "/system/uploads/plant_threat/image1/1/small_avatar.png" }, "tiny": { "url": "/system/uploads/plant_threat/image1/1/tiny_avatar.png" } }, ... } }
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

PlantThreat/v3b

operations.cropwise.com/api/v3b/plant_threats
PlantThreat relations

    PlantThreat has many FieldScoutReportThreatMappingItems.

    PlantThreat has many FieldScoutReports

    PlantThreat has many PlantThreatVulnerableCropAssignments

    PlantThreat has many VulnerableCrops

Plant threat has next attributes

    (readonly) id - Cropwise Operations Platform ID of PlantThreat

    name - name

    custom_name - custom name of PlantThreat

    standard_name - standard name of PlantThreat

    code - code of threat

    threat_type - type: 'weed', 'insect', 'disease', 'nematodes', 'nutrition_problem', 'damaged_area', 'technological_mistake', 'not_defined', 'other'

    threat_subtype - subtype

    external_id - a string field for storing id of the element from an external system

    additional_info - your system info

    description - some description

    visible - is it visible (boolean)

    range - infection transfer distance

    latin_name - latin name of PlantThreat

    (readonly) economic_threshold_damage - economic threshold damage (string)

    (readonly) image1 - image 1, see below

    (readonly) image2 - image 2, see below

    (readonly) image3 - image 3, see below

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

PlantTreat types

    Weed

    Insect

    Disease

    Nematodes

    Nutrition_problem

    Damaged_area

    Technological_mistake

    Other

Images

{ "data": { ... "image1": { "url": "/system/uploads/plant_threat/image1/1/avatar.png", "thumb_400": { "url": "/system/uploads/plant_threat/image1/1/thumb_400_avatar.png" }, "thumb_200": { "url": "/system/uploads/plant_threat/image1/1/thumb_200_avatar.png" }, "thumb": { "url": "/system/uploads/plant_threat/image1/1/thumb_avatar.png" }, "small": { "url": "/system/uploads/plant_threat/image1/1/small_avatar.png" }, "tiny": { "url": "/system/uploads/plant_threat/image1/1/tiny_avatar.png" } }, ... } }
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

PlantThreatItem

operations.cropwise.com/api/v3/plant_threat_items
PlantThreatItem relations

    PlantThreatItem belongs to Crop. Required.

    PlantThreatItem belongs to PlantThreat.

    PlantThreatItem belongs to plant_threatable.

    PlantThreatItem has many PlantThreatItemFieldMappingItems.

PlantThreatItem has next attributes (all read-only)

    (readonly) id - Cropwise Operations Platform ID of PlantThreatItem.

    (readonly) crop_id - Cropwise Operations Platform ID of Crop.

    (readonly) plant_threat_id - Cropwise Operations Platform ID of PlantThreat.

    (readonly) plant_threatable_type - Cropwise Operations Platform type of plant_threatable: "WeatherStation", "SharedWeatherStation" or "VirtualWeatherStation".

    (readonly) plant_threatable_id - Cropwise Operations Platform ID of plant_threatable (WeatherStation, SharedWeatherStation or VirtualWeatherStation).

    (readonly) point_lon - longitude of plant_threatable object geoposition.

    (readonly) point_lat - latitude of plant_threatable object geoposition.

    (readonly) custom_name - custom name.

    (readonly) current_data - hash of current data parameters with values.

    (readonly) created_at - time when object created on server.

    (readonly) updated_at - last time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

PlantThreatItemFieldMappingItem

operations.cropwise.com/api/v3/plant_threat_item_field_mapping_items

PlantThreatItem on Field.
PlantThreatItemFieldMappingItem relations

    PlantThreatItemFieldMappingItem belongs to PlantThreatItem. Required.

    PlantThreatItemFieldMappingItem belongs to Field. Required.

PlantThreatItemFieldMappingItem has next attributes (all read-only)

    (readonly) id - Cropwise Operations Platform ID of PlantThreatItemFieldMappingItem.

    (readonly) plant_threat_item_id - Cropwise Operations Platform ID of PlantThreatItem.

    (readonly) field_id - Cropwise Operations Platform ID of Field.

    (readonly) created_at - time when object created on server.

    (readonly) updated_at - last time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Photo

operations.cropwise.com/api/v3/photos
Photo relations

    Photo belongs to photoable (one of Machine, Implement, AdditionalObject, FieldScoutReport, FieldScoutReportThreatMappingItem, ScoutReportPoint, ScoutReportPointIssue, ScoutReportPointMeasurement).

Photo has next attributes

    id (readonly) - Cropwise Operations Platform ID of Photo.

    photoable_type - Cropwise Operations Platform type of photoable: "Machine", "Implement", "AdditionalObject", "FieldScoutReport", "ScoutReportPoint".

    photoable_id - Cropwise Operations Platform ID of photoable (Machine, Implement, AdditionalObject, FieldScoutReport).

    name - Photo name.

    photo - URLs for photo in different resolutions.

    additional_info - Additional info.

    description - Description.

    md5 (readonly) - md5 digest for photo.

    file_size(readonly) - Photo file size.

    longitude (readonly) - Longtitude of this photo.

    latitude (readonly) - Latitude of this photo.

    altitude (readonly) - Altitude of this photo.

    image_direction (readonly) - Image direction of this photo.

    created_by_user_at- Time of Photo created on user's device.

    external_id - a string field to store id of the element from an external system.

    created_at (readonly) - Time when object created on server.

    updated_at (readonly) - Last time when object was updated.

Photoable types

    Machine

    Implement

    AdditionalObject

    FieldScoutReport

    FieldScoutReportThreatMappingItem

    ScoutReportPoint

    ScoutReportPointIssue

    ScoutReportPointMeasurement

Uploading Photo

IMPORTANT: Photo file can't be uploaded via plain-text JSON HTTP request.

To create Photo record you should send request through multipart-form POST query.

    Content-Type HTTP header should be multipart/form-data. Most of HTTP libs set this header automatically when sending form data via POST request.

    X-User-API-Token HTTP header must be present and set to your API token.

    Attributes must be encoded in multipart-form format.

Example (create Photo for FieldScoutReport with ID 123)

Required attributes:

data[photoable_type] "FieldScoutReport"
data[photoable_id] "123"
data[photo] <content of file>

cURL example:

curl --request POST \
  --url https://operations.cropwise.com/api/v3/photos \
  --header 'X-User-API-Token: YOUR-API-TOKEN' \
  --form 'data[photoable_type]=FieldScoutReport' \
  --form 'data[photoable_id]=123' \
  --form 'data[photo]=@/Users/alex/Desktop/test_photo.jpg'

PHP example:

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->addForm(array(
  'data[photoable_type]' => 'FieldScoutReport',
  'data[photoable_id]' => '123'
), array(
  array(
    'name' => 'data[photo]',
    'type' => null,
    'file' => '/Users/alex/Desktop/test_photo.jpg',
    'data' => null
  )
));

$request->setRequestUrl('https://operations.cropwise.com/api/v3/photos');
$request->setRequestMethod('POST');
$request->setBody($body);

$request->setHeaders(array(
  'Host' => 'operations.cropwise.com',
  'X-User-API-Token' => 'YOUR-API-TOKEN'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();

PHP cURL example (php 5.5+):

$ch = curl_init();

$data = array(
  'data[photoable_type]' => 'FieldScoutReport',
  'data[photoable_id]' => '123',
  'data[photo]' => new CURLFile("/Users/alex/Desktop/test_photo.jpg"),
);

curl_setopt($ch, CURLOPT_URL, 'https://operations.cropwise.com/api/v3/photos');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_SAFE_UPLOAD, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array("X-User-Api-Token: YOUR-API-TOKEN"));

echo curl_exec($ch);

$response = curl_exec($ch);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}

NOTE: All attributes, except photo, could be updated via JSON requests.
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, photoable_id, photoable_type, external_id, uuid, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Photo/v3a

operations.cropwise.com/api/v3a/photos
Photo relations

    Photo belongs to photoable (one of Machine, Implement, AdditionalObject, FieldScoutReport, FieldScoutReportThreatMappingItem, ScoutReportPoint, ScoutReportPointIssue, ScoutReportPointMeasurement).

Photo has next attributes

    id (readonly) - Cropwise Operations Platform ID of Photo.

    photoable_type - Cropwise Operations Platform type of photoable: "Machine", "Implement", "AdditionalObject", "FieldScoutReport", "ScoutReportPoint".

    photoable_id - Cropwise Operations Platform ID of photoable (Machine, Implement, AdditionalObject, FieldScoutReport).

    name - Photo name.

    photo - URLs for photo in different resolutions.

    additional_info - Additional info.

    description - Description.

    md5 (readonly) - md5 digest for photo.

    file_size(readonly) - Photo file size.

    longitude (readonly) - Longtitude of this photo.

    latitude (readonly) - Latitude of this photo.

    altitude (readonly) - Altitude of this photo.

    image_direction (readonly) - Image direction of this photo.

    created_by_user_at- Time of Photo created on user's device.

    external_id - a string field to store id of the element from an external system.

    created_at (readonly) - Time when object created on server.

    updated_at (readonly) - Last time when object was updated.

Photoable types

    Machine

    Implement

    AdditionalObject

    FieldScoutReport

    FieldScoutReportThreatMappingItem

    ScoutReportPoint

    ScoutReportPointIssue

    ScoutReportPointMeasurement

Uploading Photo

IMPORTANT: Photo file can't be uploaded via plain-text JSON HTTP request.

To create Photo record you should send request through multipart-form POST query.

    Content-Type HTTP header should be multipart/form-data. Most of HTTP libs set this header automatically when sending form data via POST request.

    X-User-API-Token HTTP header must be present and set to your API token.

    Attributes must be encoded in multipart-form format.

Example (create Photo for FieldScoutReport with ID 123)

Required attributes:

data[photoable_type] "FieldScoutReport"
data[photoable_id] "123"
data[photo] <content of file>

cURL example:

curl --request POST \
  --url https://operations.cropwise.com/api/v3a/photos \
  --header 'X-User-API-Token: YOUR-API-TOKEN' \
  --form 'data[photoable_type]=FieldScoutReport' \
  --form 'data[photoable_id]=123' \
  --form 'data[photo]=@/Users/alex/Desktop/test_photo.jpg'

PHP example:

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->addForm(array(
  'data[photoable_type]' => 'FieldScoutReport',
  'data[photoable_id]' => '123'
), array(
  array(
    'name' => 'data[photo]',
    'type' => null,
    'file' => '/Users/alex/Desktop/test_photo.jpg',
    'data' => null
  )
));

$request->setRequestUrl('https://operations.cropwise.com/api/v3a/photos');
$request->setRequestMethod('POST');
$request->setBody($body);

$request->setHeaders(array(
  'Host' => 'operations.cropwise.com',
  'X-User-API-Token' => 'YOUR-API-TOKEN'
));

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();

PHP cURL example (php 5.5+):

$ch = curl_init();

$data = array(
  'data[photoable_type]' => 'FieldScoutReport',
  'data[photoable_id]' => '123',
  'data[photo]' => new CURLFile("/Users/alex/Desktop/test_photo.jpg"),
);

curl_setopt($ch, CURLOPT_URL, 'https://operations.cropwise.com/api/v3a/photos');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_SAFE_UPLOAD, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array("X-User-Api-Token: YOUR-API-TOKEN"));

echo curl_exec($ch);

$response = curl_exec($ch);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}

NOTE: All attributes, except photo, could be updated via JSON requests.
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, photoable_id, photoable_type, external_id, uuid, created_at, updated_at
ProductionCycles

operations.cropwise.com/api/v3/production_cycles
Seasons relations

    ProductionCycle belongs to Crop

    ProductionCycle belongs to Season

    ProductionCycle has one HistoryItem

ProductionCycle has next attributes

    (readonly) id - Cropwise Operations Platform ID of ProductionCycle

    name - production cycle name

    crop_id - Cropwise Operations Platform ID of related Crop

    season_id - Cropwise Operations Platform ID of related Season

    (readonly) base_cycle - a note on whether the production cycle is basic

    external_id - a string field for storing id of the element from an external system

    additional_info - your additional info

    description - your description

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, crop_id, season_id, external_id
Comparison filters by (for more info see)

created_at, updated_at
ProductivityEstimate

operations.cropwise.com/api/v3/productivity_estimates
ProductivityEstimate relations

    ProductivityEstimate belongs to Field.

ProductivityEstimate has next attributes

    (readonly) id - Cropwise Operations Platform ID of ProductivityEstimate

    (readonly) field_id - Field ID

    (readonly) year - Year

    (readonly) estimate_value - Estimated productivity

    (readonly) estimate_date - Date productivity was calculated

    (readonly) description - Description

    (readonly) created_at - Time when object created on server

    (readonly) updated_at - Last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

year, field_id
ProductivityEstimateHistory

operations.cropwise.com/api/v3/productivity_estimate_histories
ProductivityEstimateHistory relations

    ProductivityEstimateHistory belongs to Field.

ProductivityEstimateHistory has next attributes

    (readonly) id - Cropwise Operations Platform ID of ProductivityEstimate

    (readonly) field_id - Field ID

    (readonly) year - Year

    (readonly) estimate_history - History of ProductivityEstimation (JSON)

    (readonly) created_at - Time when object created on server

    (readonly) updated_at - Last time when object was updated

Example of estimate_history: { "2018-04-22": 27.799, "2018-04-29": 29.764, "2018-05-06": 31.849 }
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

ProductivityEstimatePeers

operations.cropwise.com/api/v3/productivity_estimate_peers
ProductivityEstimatePeers relations

    ProductivityEstimatePeer belongs to ProductivityEstimate.

ProductivityEstimatePeer has next attributes

    (readonly) id - Cropwise Operations Platform ID of ProductivityEstimatePeer

    (readonly) productivity_estimate_id - Cropwise Operations Platform ID of ProductivityEstimate

    (readonly) year - Season

    (readonly) productivity - Productiovity on field

    (readonly) area - Area of field

    (readonly) crop - Crop on field

    (readonly) variety - Variety of crop

    (readonly) previous_crop_name - Previous crop on field

    (readonly) previous_crop_standard_name - Previous crop's standard_name attribute

    (readonly) accumulated_precipitations - Accumulated precipitations in season

    (readonly) average_soil_moisture - Average soil moisture in season

    (readonly) max_ndvi - Max ndvi by season

    (readonly) sowing_date - Sowing date

    (readonly) harvesting_date - Harvesting date

    (readonly) created_at - Time when object created on server

    (readonly) updated_at - Last time when object was updated

    (readonly) ndvi_values - Array of ndvi values for dates

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

field_id, id, productivity_estimate_id, crop, year, variety, previous_crop_name, previous_crop_standard_name, sowing_date, harvesting_date, created_at, updated_at
Comparison filters by (for more info see)

year, productivity, area, accumulated_precipitations, average_soil_moisture, max_ndvi, sowing_date, harvesting_date, created_at, updated_at
ProtectedDocuments

operations.cropwise.com/api/v3/protected_documents
ProtectedDocument relations

ProtectedDocument belongs to documentable.
ProtectedDocument has next attributes

    (readonly) id - Cropwise Operations Platform ID of ProtectedDocument

    name - name of document (will be set from filename if empty)

    description - description for document

    (readonly) document_url - url of saved file

    (writeonly) document - document file (preferable type - multipart/form-data)

    documentable_id - Cropwise Operations Platform ID of related object

    documentable_type - Related object type (see below).

    (readonly) created_at - Time when object created on server

    (readonly) updated_at - Last time when object was updated

    external_id - a string field for storing id of the element from an external system

    idempotency_key - the idempotency key transmitted during the request, if any.

Documentable types

    AgroOperation

    AgroRecommendation

    Alert

    Counterparty

    LandDocument

    LandParcel

    MaintenanceRecord

Allowed file extensions

    jpg

    jpeg

    gif

    png

    bmp

    tif

    tiff

    doc

    docx

    xls

    xlsx

    ppt

    pptx

    odt

    ods

    odp

    pdf

    numbers

    pages

    key

    zip

    rar

    gz

    tar

    7z

    csv

    txt

    json

    xml

    rtf

Multipart-form POST request with photo/file

To create protected photo/file for land document item we propouse the next workflow:

    Create LandDocument through JSON API with all data (including protected_documents)

    Create LandDocument and then update it with POST query equal to this HTML-form submitting:

HTML form example:

<form action="/api/v3/land_documents/ID" enctype="multipart/form-data" method="PUT">
    <input type="file" name="photo">
</form>

Uploading file

To create ProtectedDocument record you should send request through multipart-form POST request.

    Content-Type HTTP header should be multipart/form-data.

    X-User-API-Token HTTP header must be present and set to your API token.

    Attributes must be encoded in multipart-form format.

Example (create ProtectedDocument for AgroOperation with ID 123)

data[document] <content of file>
data[documentable_type] "AgroOperation"
data[documentable_id] 123
data[name] <some name>
data[description] <some description>
data[idempotency_key] <key>

NOTE: All attributes, except document, could be updated via JSON requests.
Downloading a file

operations.cropwise.com/api/v3/download_protected_documents/<id>

where <id> - Cropwise Operations Platform ID of ProtectedDocument
Filters by

Equality: id, name, documentable_type, documentable_id

Date comparison: created_at, updated_at
PriceLists

operations.cropwise.com/api/v3/price_lists
PriceList relations

    PriceList has many PriceListItems.

PriceList has next attributes

    (readonly) id - Cropwise Operations Platform ID of PriceList

    name - Name of the price list

    active_from - Date from which the price list is active

    active_to - Date until which the price list is active

    archived - Indicates whether the price list is archived

    additional_info - Additional information about the price list

    description - Description of the price list

    external_id - External system ID

    (readonly) created_at - Time when object was created on the server

    (readonly) updated_at - Last time when the object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name
Comparison filters by

created_at, updated_at
Sorting options

id, created_at, updated_at
PriceListItems

operations.cropwise.com/api/v3/price_list_items
PriceListItem relations

    PriceListItem belongs to PriceList

    PriceListItem belongs to Unit

    PriceListItem belongs to a polymorphic Priceable entity (e.g., WhItem)

PriceListItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of PriceListItem

    price_list_id - Associated PriceList ID

    priceable_type - Type of the priceable object (polymorphic)

    priceable_id - ID of the priceable object

    price_cents - Price in cents

    additional_info - Additional information (optional)

    description - Description (optional)

    external_id - External system ID (optional)

    unit_id - Associated Unit ID

    (readonly) created_at - Time when object was created on the server

    (readonly) updated_at - Last time when the object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, price_list_id, priceable_type, priceable_id
Comparison filters by

created_at, updated_at
Sorting options

id, created_at, updated_at
ResponsibleUserMappingItem

operations.cropwise.com/api/v3/responsible_user_mapping_items
ResponsibleUserMappingItem relations

    ResponsibleUserMappingItem belongs to AgriWorkPlan

    ResponsibleUserMappingItem belongs to AgroOperation

    ResponsibleUserMappingItem belongs to MaintenanceRecord

    ResponsibleUserMappingItem belongs to SoilTestTask

    ResponsibleUserMappingItem belongs to User

ResponsibleUserMappingItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of ResponsibleUserMappingItem

    related_object_type - type of object for which this record: AgriWorkPlan,AgroOperation,MaintenanceRecord,SoilTestTask

    related_object_id - Cropwise Operations Platform ID of related object

    user_id - Cropwise Operations Platform ID of User

    external_id - a string field for storing id of the element from an external system

    idempotency_key - the idempotency key transmitted during the request, if any.

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, related_object_type, related_object_id, user_id, external_id, idempotency_key
SatelliteImages

operations.cropwise.com/api/v3/satellite_images
SatelliteImage relations

    SatelliteImage belongs to item (Field, FieldGroup).

SatelliteImage has next attributes

    (readonly) id - Cropwise Operations Platform ID of SatelliteImage

    (readonly) md5 - md5 digest for image

    (readonly) item_type - Cropwise Operations Platform type of item: "FieldGroup", "Field"

    (readonly) item_id - Cropwise Operations Platform ID of item (FieldGroup, Field)

    (readonly) size - image size

    (readonly) date - image date

    (readonly) source - image source

    (readonly) cloudy - image cloudy

    (readonly) data_coverage - data coverage (0.0 – 1.0)

    (readonly) clouds_coverage - coverage by clouds (0.0 – 1.0)

    (readonly) cirrus_coverage - coverage by cirrus clouds (0.0 – 1.0)

    (readonly) min_value - min NDVI value for image

    (readonly) max_value - max NDVI value for image

    (readonly) mean_value - NDVI homogeneity value for image

    (readonly) source_sign - source of image (satellite code name)

    (readonly) image_type - image type ('ndvi', 'groups')

    (readonly) image_metadata — image metadata (depends on image type)

    (readonly) standard_deviation — standard deviation

    (readonly) acquired_at — time when image was acquired by satellite

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Image types

Cropwise Operations Platform process 2 types of satellite images:

    ndvi - NDVI images of Fields

    groups - Visible (RGB) images of FieldGroups.

Acceptable methods

    Resources Collection

    Ids

    Single Resource - Important! Method returns tiff file but not a json!

    Changes

    Changes Ids

    Mass Request

Filters by

    item_type — could be Field or FieldGroup.

    item_id — Cropwise Operations Platform ID of Field or FieldGroup (could be many via ,).

    image_type — for FieldGroup: clouds, group, for Field: ndvi.

    date — date of image equal in format yyyy-mm-dd.

    source_sign — satellite code (s2a, s2b, l8, ps8 and other).

    created_at — date image created_at in format yyyy-mm-dd.

    updated_at — date image updated_at in format yyyy-mm-dd.

Comparison filters by (for more info see)

data_coverage, clouds_coverage, cirrus_coverage, date, acquired_at, created_at, updated_at
Sorting by (for more info see)

date, id, acquired_at, created_at, updated_at
SatelliteImages/v3a

operations.cropwise.com/api/v3a/satellite_images
SatelliteImage relations

    SatelliteImage belongs to item (Field, FieldGroup).

SatelliteImage has next attributes

    (readonly) id - Cropwise Operations Platform ID of SatelliteImage

    (readonly) item_type - Cropwise Operations Platform type of item: "FieldGroup", "Field"

    (readonly) item_id - Cropwise Operations Platform ID of item (FieldGroup, Field)

    (readonly) size - image size

    (readonly) date - acquisition date (in UTC time zone)

    (readonly) image_type - image type ('ndvi', 'groups')

    (readonly) source_sign - source of image (satellite code name: l8, s2a, s2b, ps8, etc.)

    (readonly) data_coverage - data coverage (0.0 – 1.0)

    (readonly) clouds_coverage - coverage by clouds (0.0 – 1.0)

    (readonly) cirrus_coverage - coverage by cirrus clouds (0.0 – 1.0)

    (readonly) min_value — min data value (0.0 – 1.0 for ndvi)

    (readonly) max_value — max data value (0.0 – 1.0 for ndvi)

    (readonly) mean_value — mean data value (0.0 – 1.0 for ndvi)

    (readonly) standard_deviation — standard deviation

    (readonly) acquired_at — time when image was acquired by satellite

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Image types

Cropwise Operations Platform process 2 types of satellite images:

    ndvi - NDVI images of Fields

    groups - Visible (RGB) images of FieldGroups.

Acceptable methods

    Resources Collection

    Ids

    Single Resource - Important! Method returns tiff file but not a json!

    Changes

    Changes Ids

    Mass Request

Filters by

    item_type — could be Field or FieldGroup.

    item_id — Cropwise Operations Platform ID of Field or FieldGroup (could be many via ,).

    image_type — for FieldGroup: clouds, group, for Field: ndvi.

    date — date of image equal in format yyyy-mm-dd.

    source_sign — satellite code (s2a, s2b, l8, ps8 and other).

    created_at — date image created_at in format yyyy-mm-dd.

    updated_at — date image updated_at in format yyyy-mm-dd.

Comparison filters by (for more info see)

data_coverage, clouds_coverage, cirrus_coverage, date, acquired_at, created_at, updated_at
Sorting by (for more info see)

date, id, acquired_at, created_at, updated_at

NdviGrid

operations.cropwise.com/api/v3/ndvi_grid
AgronomistFields object has next attributes

    source_sign - satellite source of the NDVI image (ps8, s2b, s2c, s2a, l8, ps, pre, spot)

    date - acquisition date of the NDVI image (format: YYYY-MM-DD)

    points - GeoJSON FeatureCollection with NDVI values per each grid point of the field

Acceptable methods

    Resources Collection

Required parameters

    field_id - Cropwise Operations Platform ID of the related Field

Optional parameters

    source_sign (string) — NDVI satellite source. If not specified, the system selects the most prioritized source by the following order: ps8, s2b, s2c, s2a, l8, ps, pre, spot.

    date (string, format: YYYY-MM-DD) — acquisition date of the NDVI image. If specified, the data will be provided for the given date. If not specified, the data will be provided for the most latest available image.

ScoutingTasks

operations.cropwise.com/api/v3/scouting_tasks
ScoutingTask relations

    ScoutingTask belongs to User as an author

    ScoutingTask belongs to Field

    ScoutingTask belongs to AutomaticScoutingTask

    ScoutingTask belongs to HistoryItem

    ScoutingTask has one FieldScoutReport

    ScoutingTask has many ScoutingTaskPoints

    ScoutingTask has many ScoutReportPoints

    ScoutingTask has many ScoutingTaskResponsibleUserAssignments

ScoutingTask has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutingTask

    field_id - Cropwise Operations Platform ID of related Field

    history_item_id - Cropwise Operations Platform ID of related HistoryItem

    (readonly) responsible_id - Cropwise Operations Platform ID of responsible User. Deprecated, use scouting_task_responsible_user_assignments instead.

    author_id - Cropwise Operations Platform User ID of author

    external_id - a string field for storing id of the element from an external system

    start_time - start time for scouting task

    end_time - end time for scouting task

    description

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

    status - status can be planned, done, canceled

    image_type - image types can be visible, ndvi, ndvi_contrast, relief

    image_date - date of image to show on map in scouting task

    image_source_sign - can be empty, uav, l8, s2b, s2a

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, field_id, author_id, external_id, status, automatic_scouting_task_id, season, created_at, updated_at

    responsible_id (Deprecated)

Comparison filters by (for more info see)

start_time, end_time, planed_created_at, created_at, updated_at

ScoutingTaskResponsibleUserAssignments

operations.cropwise.com/api/v3/scouting_task_responsible_user_assignments
ScoutingTaskResponsibleUserAssignments relations

    ScoutingTaskResponsibleUserAssignments belongs to ScoutingTask

    ScoutingTaskResponsibleUserAssignments belongs to User as a responsible

ScoutingTaskResponsibleUserAssignments has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutingTaskResponsibleUserAssignments

    (immutable) scouting_task_id - Cropwise Operations Platform ID of ScoutingTask

    (immutable) responsible_user_id - Cropwise Operations Platform ID of responsible User

    external_id - a string field for storing id of the element from an external system

    idempotency_key - The idempotency key transmitted during the request, if any.

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, responsible_user_id, created_at, updated_at, scouting_task_id, external_id, idempotency_key
Comparison filters by (for more info see)

created_at, updated_at
ScoutingTaskPoints

operations.cropwise.com/api/v3/scouting_task_points
ScoutingTaskPoint relations

    ScoutingTaskPoint belongs to ScoutingTask

    ScoutingTaskPoint has one ScoutReportPoint(optional)

ScoutingTaskPoint has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutingTaskPoint

    scouting_task_id - Cropwise Operations Platform ID of related ScoutingTask

    latitude - latitude of this scout point

    longitude - longitude of this scout point

    external_id - a string field for storing id of the element from an external system

    description - some description

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Seasons

operations.cropwise.com/api/v3/seasons
Season relations

    Season has many ProductionCycle

    Season has many AgriWorkPlan

Seasons has next attributes

    (readonly) id - Cropwise Operations Platform ID of Season

    name - season name

    year - Year

    start_date - start date for season

    end_date - end date for season

    external_id - a string field for storing id of the element from an external system

    additional_info - your additional info

    description - your description

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, year, external_id
Comparison filters by (for more info see)

created_at, updated_at
Seed

operations.cropwise.com/api/v3/seeds
Seed relations

    Seed belongs to Crop.

Seed has next attributes

    (readonly) id - Cropwise Operations Platform ID of Seed

    name - name

    manufacturer_name - name of manufacturer

    crop_id - Cropwise Operations Platform ID of Crop

    variety - variety

    reproduction_number - reproduction number

    reproduction - reproduction (one of: original, elite, first, second, third, fourth, fifth, mass)

    additional_info - your system info

    archived - hide item from lists

    description - description

    thousand_seeds_mass - Thousand seeds mass in grams

    sowing_suitability - Sowing suitability in percentages

    pieces_per_one_sowing_unit - Seeds per 1 sowing unit in pieces

    units_of_measurement (deprecated) — use base_inventory_unit_id instead. Units of measurement: 'units', 'kg', 'pieces', 'thousand_pieces', 'million_pieces', 'tn'

    base_inventory_unit_id - ID of the base unit of measurement. See the Unit API for available units.

    wh_item_id - Cropwise Operations Platform ID of WhItem

    wh_item_base_unit_id (deprecated) - Use base_inventory_unit_id instead. Cropwise Operations Platform ID of Unit

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

    ripeness_group - ripeness group (one of: ultra_early, early, mid_early, mid, mid_late, late)

    (readonly) ripeness_group_name - localized ripeness group name

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, crop_id, description, additional_info, archived, variety, reproduction_number, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
Additional info

Seed support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
SharedWeatherStations

operations.cropwise.com/api/v3/shared_weather_stations
SharedWeatherStations has next attributes (all read-only):

    (readonly) id - Cropwise Operations Platform ID of SharedWeatherStation.

    (readonly) name - shared weather station name.

    (readonly) longitude - longitude of shared weather station geoposition.

    (readonly) latitude - latitude of shared weather station geoposition.

    (readonly) integration - name of integration (open_weather, open_agribusiness_weather, agro_prognoz, syngenta_weather)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Single Resource

    Ids

    Changes

    Changes Ids

    Mass Request

SoilTest

operations.cropwise.com/api/v3/soil_tests
SoilTest relations

    SoilTest belongs to Field.

    SoilTest has many SoilTestSamples.

SoilTest has next attributes

    (readonly) id - Cropwise Operations Platform ID of SoilTest

    field_id - Cropwise Operations Platform ID of Field

    name - Name of soil test

    made_at - Date when soil test has been made

    elements - Hash of elements (see below). Every element can be either simple value "pH": 123, or hash of parameters "pH": {"value": 127, ...}.

    description - Description

    laboratory_name - Laboratory name

    attached_file - Attached file

    external_id - ID of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Important!

This is legacy endpoint, in near future it would be replaced by new style, look operations.cropwise.com/api/v3a/soil_tests
Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Additional info

Soil Tests support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
SoilTest/v3a

operations.cropwise.com/api/v3a/soil_tests
SoilTest relations

    SoilTest belongs to Field.

    SoilTest has many SoilTestSamples.

SoilTest has next attributes

    (readonly) id - Cropwise Operations Platform ID of SoilTest

    field_id - Cropwise Operations Platform ID of Field

    name - Name of soil test

    elements - hash of elements (see SoilTest => Available elements). Every element can be or simple value ("pH": 123), or hash of parameters ("pH": {"value": 127, "standard_research_method": "hot_water", "level": "low", "units": "pH" }).

    description - description for SoilTest

    attached_file - attached file

    laboratory_name - laboratory name

    soil_type - soil type. Could be one of: sandy, loamy, clayey, peaty

    probe_depth - depth of the probe. It should be hash of parameters: { "value": 50, "units": "mm" }, allowed units are: cm, mm, inch

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Important!

Every element hash have 4 (four) parameters (value, units, standard_research_method, level). You can define all these parameters or some of them.

    value - Numeric, value of element (required)

    units - String, units of measurement for certain element (required)

    standard_research_method - String, name of standard research method (required). Can be one of following: edta, edta_disodium_salt, ammonium_acetate_with_2g_l_quinol, ammonium_nitrate, ammonium_acetate, ammonium_acetate_with_oxalic_acid, ctdo, dumas_combustion, hot_water, laser_diffraction, leached_with_1aa_10pc, bray_1, bray_2, mehlich_1, mehlich_3, morgan, ambic_1, olsen, dtpa, ab_dtpa, egner_rhiem, schachtschabel, loss_on_ignition, flow_injection_analysis, calcium_phosphate, resine, water, cacl2, spectrophotometry, la_motte, turin, chirikov, saline_extract, kirsanov, kappen, cornfield, machigin, berger_truog, krupsky_alexandrov, gravimetric, gost_26213_2021, iso_10390_2022, dstu_8347_2015 or unspecified.

    level - String, element soil content level. Can be one of: very_low, low, average, high, very_high.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Available elements and their measurement units

    pH - Soil acidity (pH level) | "pH"

    organic_matter - Organic matter (humus) | "%"

    N - Total Nitrogen | "ppm", "kg/ha", "mg/100g", "lb/acre"

    N_NO3 - Nitrogen in nitrate (NO3) form | "ppm", "kg/ha", "mg/100g", "lb/acre"

    N_NH4 - Nitrogen in ammonium (NH4) form | "ppm", "kg/ha", "mg/100g", "lb/acre"

    P - Phosphorus | "ppm", "kg/ha", "mg/100g", "lb/acre", "index"

    K - Potassium | "ppm", "kg/ha", "mg/100g", "lb/acre", "index"

    K_mg_eq - Potassium | "mg-eq/100g"

    Al - Aluminium | "ppm", "kg/ha", "mg/100g", "lb/acre"

    B - Boron | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Ca - Calcium | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Ca_mg_eq - Calcium | "mg-eq/100g"

    Cd - Cadmium | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Cl - Chlorine | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Co - Cobalt | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Cu - Copper | "ppm", "kg/ha", "mg/100g", "lb/acre"

    F - Fluorine | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Fe - Iron | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Mg - Magnesium | "ppm", "kg/ha", "mg/100g", "lb/acre", "index"

    Mg_mg_eq - Magnesium | "mg-eq/100g"

    Mn - Manganese | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Mo - Molybdenum | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Na - Sodium | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Na_mg_eq - Sodium | "mg-eq/100g"

    Ni - Nickel | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Pb - Lead | "ppm", "kg/ha", "mg/100g", "lb/acre"

    S - Sulfur | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Se - Selenium | "ppm", "kg/ha", "mg/100g", "lb/acre"

    Zn - Zinc | "ppm", "kg/ha", "mg/100g", "lb/acre"

    moisture - Moisture | "%"

    moisture_level - Moisture level | "mm"

    relative_moisture_provision_100 - Relative moisture provision | "%"

    pH_salt - pH (salt) | "pH"

    pH_water - pH (water) | "pH"

    pH_hydrolytic - pH (hydro) | "pH"

    electrical_conductivity - Electrical conductivity | "mS/cm"

    hydraulic_conductivity - The ease with which water can move through pore spaces or fractures of soil | "micron/sec"

    base_saturation - Base saturation | "%"

    soil_organic_carbon - Soil organic carbon (SOC) | "%"

    cation_exchange_capacity - Cation exchange capacity | "mg-eq/100g"

    cation_exchange_density - Cation exchange density | "cmolc/dm3"

    alkaline_hydrolyzable_N - Alkaline hydrolyzable Nitrogen (AH-N) | "ppm", "kg/ha", "mg/100g", "lb/acre"

    mineral_N - Mineral Nitrogen | "ppm", "kg/ha", "mg/100g", "lb/acre"

    land_quality_assessment - Land quality assessment | "point"

    sum_of_absorbed_bases - Sum of absorbed bases | "mg-eq/100g"

    sum_of_absorbed_bases_density - Sum of absorbed bases density | "cmolc/dm3"

    dry_residue - Dry residue | "%"

    silt - Silt | "%"

    clay - Clay | "%"

    sand - Sand | "%"

    hydrogen_cation_H_plus - Hydrogen cation H+ | "%"

    acid_saturation - Acid saturation | "%"

    aluminum_cation_Al_3plus - Aluminum cation Al+++ | "ppm", "kg/ha", "mg/100g", "lb/acre"

    reaction_of_soil_solution - Reaction of soil solution | "pH_hydro"

    consolidation_depth - Consolidation depth | "cm"

    tillage - Tillage | "cm"

    zones - Zones | "%"

    density_of_radioactive_contamination - Density of radioactive contamination | "Ci/m2"

    Ca_saturation - Calcium saturation | "%"

    Mg_saturation - Magnesium saturation | "%"

    K_saturation - Potassium saturation | "%"

    Al_saturation - Aluminium saturation | "%"

    H_saturation - Hydrogen saturation | "%"

    Na_saturation - Sodium saturation | "%"

    Ca_Mg_ratio - Calcium-magnesium ratio | "point"

    K_Mg_ratio - Potassium-magnesium ratio | "point"

    Ca_K_ratio - Calcium-potassium ratio | "point"

    phosphorus_buffering_index - Phosphorus buffering index | "point"

    soil_depth_5 - Soil density (you can put any number instead of 5 - greater than 5 and less than 60 with step 5, i.e. soil_depth_10, soil_depth_15...soil_depth_60) | "g/cm3"

    ground_density - Ground density average | "kPa"

    ground_density_min - Ground density minimum | "kPa"

    ground_density_max - Ground density maximum | "kPa"

    ground_density_0 - Ground density by depth (you can put any number instead of 0 - greater than 0 and less than 700 with step 1, i.e. ground_density_1, ground_density_2...ground_density_700) | "kPa"

    electrical_conductivity_25 - Electrical conductivity (available numbers are: 25, 50, 70, 90, 100, 110, 150, 200, 250, 300, i.e electrical_conductivity_25, electrical_conductivity_50 and so on | "mS/cm"

SoilTestSample

operations.cropwise.com/api/v3/soil_test_samples
SoilTestSample relations

    SoilTestSample belongs to SoilTest.

SoilTestSample has next attributes

    (readonly) id - Cropwise Operations Platform ID of SoilTestSample

    soil_test_id - Cropwise Operations Platform ID of SoilTest

    elements - hash of elements (see SoilTest => Available elements)

    coordinates - coordinates ([latitude, longitude])

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

soil_test_id
SoilTestTask/v3

operations.cropwise.com/api/v3/soil_test_tasks
SoilTestTask relations

    SoilTestTask belongs to Field

    SoilTestTask belongs to FieldShape.

SoilTestTask has next attributes

    (readonly) id - Cropwise Operations Platform ID of SoilTestTask

    (readonly) field_id - Cropwise Operations Platform ID of Field

    (readonly) field_shape_id - Cropwise Operations Platform ID of FieldShape

    (readonly) name - name of SoilTestTask

    (readonly) points_as_string - string with point into JSON format

    (readonly) points - array of points into hash format (example: [{"name": "ПАР-01_1", "long": 32.61, "lat": 50.81034}])

    (readonly) zoning_type - string one of "cell", "shape", "custom"

    (readonly) zoning_data_as_string - string with areas into JSON format

    status - string one of "planned", "done", "canceled"

    start_time - time when task planned to start

    end_time - time when task planned to end

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Filters by

field_id
Comparison filters by (for more info see)

created_at, updated_at
SoilTestTask/v3a

operations.cropwise.com/api/v3a/soil_test_tasks
SoilTestTask relations

    SoilTestTask belongs to Field

    SoilTestTask belongs to FieldShape.

SoilTestTask has next attributes

    (readonly) id - Cropwise Operations Platform ID of SoilTestTask

    (readonly) field_id - Cropwise Operations Platform ID of Field

    (readonly) field_shape_id - Cropwise Operations Platform ID of FieldShape

    (readonly) name - name of SoilTestTask

    (readonly) zoning_type - string one of "cell", "shape", "custom"

    (readonly) zoning_data_as_string - string with areas into JSON format

    status - string one of "planned", "done", "canceled"

    start_time - time when task planned to start

    end_time - time when task planned to end

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Filters by

field_id
Comparison filters by (for more info see)

created_at, updated_at
SoilType

operations.cropwise.com/api/v3/soil_types
SoilType relations

    SoilType belongs to FieldShape.

SoilType has next attributes

    (readonly) id - Cropwise Operations Platform ID of SoilTestTask

    (readonly) field_shape_id - Cropwise Operations Platform ID of FieldShape

    (readonly) soil_property_name - name of SoilType by FAO (Food and Agriculture Organization of the United Nations)

    (readonly) soil_property_value - ID of soil property

    (readonly) geo_json - simplified shape in GeoJSON format

    (readonly) external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Filters by

field_shape_id, soil_property_value
Comparison filters by (for more info see)

created_at, updated_at
SparePart

operations.cropwise.com/api/v3/spare_parts
SparePart relations

    SparePart belongs to SparePartManufacturer

SparePart has next attributes

    (readonly) id - Cropwise Operations Platform ID of SparePartManufacturer

    spare_part_manufacturer_id - Cropwise Operations Platform ID of SparePartManufacturer

    name - name of spare part

    part_number - unique part number of spare part for manufacturer

    description - some description

    archived - boolean flag

    additional_info - some additional info

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Additional info

Spare Part support custom fields. You can get access to your own custom_fields by their name 'x_custom_field_name'. (for more info see)
SparePartManufacturer

operations.cropwise.com/api/v3/spare_part_manufacturers
SparePartManufacturer relations

    SparePartManufacturer has many SpareParts

SparePartManufacturer has next attributes

    (readonly) id - Cropwise Operations Platform ID of SparePartManufacturer

    name - name of manufacturer

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

SprayingWindow

operations.cropwise.com/api/v3/spraying_window
SprayingWindow item has next attributes

    (readonly) id - Cropwise Operations Platform ID of SprayingWindow (WeatherItem)

    (readonly) field_group_id - Cropwise Operations Platform ID of weather forecast related FieldGroup

    (readonly) generated_at - time when forecast generated on weather service

    (readonly) daily_forecast - object with daily forecast spraying recommendations; each key is a day beginning unix timestamp; value is an array of hourly recommendations

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Hourly recommendation structure

    (readonly) description - a string with human readable recommendation description

    (readonly) severity - a number that indicates spraying recommendation level at this hour: 0 - best time to spray, 1 - not advisable, but you can spray, 2 - not recommended

    (readonly) status - a string with human readable spraying recommendation level at this hour

    (readonly) timestamp - the hour beginning unix timestamp

    (readonly) weather - object with forecast for humidity, temperature, wind speed for the hour

Acceptable methods

    Resources Collection

TechFluidConsumptionNorm

operations.cropwise.com/api/v3/tech_fluid_consumption_norms
TechFluidConsumptionNorm relations

    TechFluidConsumptionNorm belongs to WorkType

    TechFluidConsumptionNorm belongs to Machine

    TechFluidConsumptionNorm belongs to Implement

    TechFluidConsumptionNorm belongs to MachineryManufacturer

    TechFluidConsumptionNorm belongs to MachineryModel

TechFluidConsumptionNorm has next attributes

    (readonly) id - Cropwise Operations Platform ID of TechFluidConsumptionNorm

    work_type_id - Cropwise Operations Platform ID of WorkType

    machine_id - Cropwise Operations Platform ID of Machine

    implement_id - Cropwise Operations Platform ID of Machine

    machinery_manufacturer_id - Cropwise Operations Platform ID of MachineryManufacturer

    machinery_model_id - Cropwise Operations Platform ID of MachineryModel

    appointment_date - appointment date

    date_end - end date of TechFluidConsumptionNorm

    no_date_end - no date end sign

    norm_per_distance - norm per distance value

    norm_per_area - norm per area value

    norm_per_time - norm per time value

    additional_info - additional info

    external_id - a string field for storing id of the element from an external system

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Comparison filters by (for more info see)

appointment_date, date_end
Sorting by (for more info see)

id, appointment_date, date_end
User

operations.cropwise.com/api/v3/users
User relations

    User belongs to Company.

    User belongs to ConsultingCompany.

    User has many Notes.

    User has many UserRoles.

    User has many UserRoleAssignments.

    User has many UserRolePermissions.

    User has many WorkRecords.

    User has many ScoutingTask (as responsible, author).

    User has many Alerts (as created_by_user, responsible_person).

    User has many AgriWorkPlans (as created_by_user, responsible_person).

    User has many AgroOperations (as responsible_person).

    User has many UserApiSessions.

    User has many AgronomistAssignments.

    User has many AgronomistFields.

    User has many ResponsibleAgronomistsFields.

    User has many AgroRecommendations (as consultant).

    User has many FieldScoutReports.

User Telematics relations

    User has many MachineTask (as driver).

    User has many ServiceLegalAgreementUserAcceptances.

    User has many ServiceLegalAgreement.

User has next attributes

    (readonly) id - Cropwise Operations Platform ID of User

    username - user name

    email - email (that is using as login)

    (writeonly) password - password (!!! writeonly field)

    notification_email - notification email

    mobile_phone - mobile phone

    (readonly) avatar - avatar (see below)

    position - position

    language - language: English: 'en', Русский: 'ru', Português: 'pt', Français: 'fr', Español: 'es', Română: 'ro'

    time_zone - time zone (e.g. "Kyiv")

    yield_units - yield units: 'tonn_per_ha', '100kg_per_ha'

    status - status: 'no_access', 'user', 'admin'

    dispatcher - is dispetcher? (true/false)

    driver - is driver? (true/false)

    agronomist - is agronomist? (true/false)

    telematics_specialist - is telematics_specialist? (true/false)

    rfid - RFID, iButton or another unique identification key. Only 0-9 and A-F letters.

    tax_identification_number - an identifying number used for tax purposes

    additional_info - your system info

    description - description

    (readonly) last_sign_in_at - time of last sign in to Cropwise Operations Platform

    (readonly) current_sign_in_at - time of current sign in to Cropwise Operations Platform

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, username, email, status, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
User/v3a

operations.cropwise.com/api/v3a/users
User relations

    User belongs to Company.

    User belongs to ConsultingCompany.

    User has many Notes.

    User has many UserRoles.

    User has many UserRoleAssignments.

    User has many UserRolePermissions.

    User has many WorkRecords.

    User has many ScoutingTask (as responsible, author).

    User has many Alerts (as created_by_user, responsible_person).

    User has many AgriWorkPlans (as created_by_user, responsible_person).

    User has many AgroOperations (as responsible_person).

    User has many UserApiSessions.

    User has many AgronomistAssignments.

    User has many AgronomistFields.

    User has many ResponsibleAgronomistsFields.

    User has many AgroRecommendations.

    User has many FieldScoutReports.

User Telematics relations

    User has many MachineTask (as driver).

    User has many ServiceLegalAgreementUserAcceptances.

    User has many ServiceLegalAgreement.

User has next attributes

    (readonly) id - Cropwise Operations Platform ID of User

    username - user name

    email - email (that is using as login)

    (writeonly) password - password (!!! writeonly field)

    notification_email - notification email

    mobile_phone - mobile phone

    (readonly) avatar - avatar (Show null instead of fallback URLs.)

    position - position

    language - language: English: 'en', Русский: 'ru', Português: 'pt', Français: 'fr', Español: 'es', Română: 'ro'

    time_zone - time zone (e.g. "Kyiv")

    yield_units - yield units: 'tonn_per_ha', '100kg_per_ha'

    status - status: 'no_access', 'user', 'admin'

    dispatcher - is dispetcher? (true/false)

    driver - is driver? (true/false)

    agronomist - is agronomist? (true/false)

    rfid - RFID, iButton or another unique identification key. Only 0-9 and A-F letters.

    additional_info - your system info

    description - description

    (readonly) last_sign_in_at - time of last sign in to Cropwise Operations Platform

    (readonly) current_sign_in_at - time of current sign in to Cropwise Operations Platform

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

UserRole

operations.cropwise.com/api/v3/user_roles
User has next attributes

    (readonly) id - Cropwise Operations Platform ID of UserRole

    name - name of UserRole

    description - description of UserRole

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

UserRoleAssignments

operations.cropwise.com/api/v3/user_role_assignments
User relations

    UserRoleAssignment belongs to UserRole.

    UserRoleAssignment belongs to User.

User has next attributes

    (readonly) id - Cropwise Operations Platform ID of UserRoleAssignment

    user_role_id - Cropwise Operations Platform ID of UserRole

    user_id - Cropwise Operations Platform ID of User

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

UserRolePermissions

operations.cropwise.com/api/v3/user_role_permissions
User relations

    UserRolePermission belongs to UserRole.

User has next attributes

    (readonly) id - Cropwise Operations Platform ID of UserRolePermission

    user_role_id - Cropwise Operations Platform ID of UserRole

    access_level - access level: no_access, read, manage, full_access

    access_for - type of permission: fields, machinery

    subject_type - type of subject: FieldGroup, MachineRegion

    subject_id - Cropwise Operations Platform ID of subject (field group or machine region)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Version

operations.cropwise.com/api/v3/versions

Versions is "change-log" that keeps history of any objects changes (created/updated/destroyed). This records generated automatically and can't be changed or destroyed.
Version relations

    Has one Object of any type (via item_type and item_id attributes).

Version has next attributes (all read-only)

    (readonly) id - Cropwise Operations Platform ID of Version.

    (readonly) item_type - Object type.

    (readonly) item_id - Object ID.

    (readonly) event - Event type (one of: create, update, destroy).

    (readonly) whodunnit - User ID who made this change (could be null in case of system-generated changes).

    (readonly) snapshot_before_change - Snapshot of changed Object (before changes apply) in JSON.

    (readonly) object_changes - List of changed attribtues of Object in JSON.

    (readonly) created_at - Time when Version record was created.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, item_type, item_id, event, whodunnit, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at
VirtualWeatherStations

operations.cropwise.com/api/v3/virtual_weather_stations
WeatherStations has next attributes (all read-only):

    (readonly) id - Cropwise Operations Platform ID of VirtualWeatherStation.

    (readonly) name - virtual weather station name.

    (readonly) longitude - longitude of virtual weather station geoposition.

    (readonly) latitude - latitude of virtual weather station geoposition.

    (readonly) elevation - elevation of virtual weather station geoposition.

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Single Resource

    Ids

    Changes

    Changes Ids

    Mass Request

VirtualWeatherHistoryItems
VirtualWeatherHistoryItems/v3a

operations.cropwise.com/api/v3a/virtual_weather_history_items

The same endpoint as weather-history-items/v3a but only for weather_historyable_type="VirtualWeatherStation"
VirtualWeatherHistoryItems/v3b

operations.cropwise.com/api/v3b/virtual_weather_history_items

The same endpoint as weather-history-items/v3b but only for weather_historyable_type="VirtualWeatherStation"
VirtualWeatherHistoryItems/v3c

operations.cropwise.com/api/v3c/virtual_weather_history_items

The same endpoint as weather-history-items/v3c but only for weather_historyable_type="VirtualWeatherStation"
Warehouse

operations.cropwise.com/api/v3/warehouses
Warehouse relations

    Warehouse belongs to WarehouseGroup

    Warehouse belongs to User

    Warehouse has many WarehouseRelatedObjectAssignment

    Warehouse has many WhDocuments

Warehouse has next attributes

    (readonly) id - Cropwise Operations Platform ID of Warehouse

    name - name of Warehouse

    warehouse_group_id - Cropwise Operations Platform ID of Warehouse Group

    responsible_user_id - Cropwise Operations Platform ID of responsible User

    description - description

    (readonly) created_at - Time when Warehouse record was created

    (readonly) updated_at - Last time when Warehouse record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resurche

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, warehouse_froup_id, created_at, responsible_user_id, description
Comparison filters by (for more info see)

created_at, updated_at
WarehouseGroup

operations.cropwise.com/api/v3/warehouse_groups
WarehouseGroup relations

    WarehouseGroup has many Warehouses

WarehouseGroup has next attributes

    (readonly) id - Cropwise Operations Platform ID of WarehouseGroup

    parent_id - Cropwise Operations Platform ID of parent WarehouseGroup

    name - name of WarehouseGroup

    description - description

    (readonly) created_at - Time when WarehouseGroup record was created

    (readonly) updated_at - Last time when WarehouseGroup record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resurche

    Changes

    Changes Ids

    Mass Request

Filters by

id, name
Comparison filters by (for more info see)

created_at, updated_at
WhItem

operations.cropwise.com/api/v3/wh_items
WhItem relations

    WhItem belongs to WhItemGroup

    WhItem belongs to Unit

    WhItem belongs to related_object

    WhItem has many WhItemUnitAssignments

    WhItem has many Wdditional_units

    WhItem has many WhDocumentItems

WhItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of WhItem

    name - name of WhItem

    variant_name - a string field for storing a variant name

    sku - Stock Keeping Unit, a string field for storing a unique value used to internally track a inventory

    barcode - a string field for storing barcode of WhItem

    is_expiration_date - boolean, true if WhItem have expiration date

    wh_item_group_id - Cropwise Operations Platform ID of WhItemGeoup

    related_object_type - type of related object ('Seed', 'Chemical', 'Fertilizer', 'SparePart')

    related_object_id - Cropwise Operations Platform ID of related object

    wh_item_base_unit_id (deprecated) - Use base_inventory_unit_id instead. Cropwise Operations Platform ID of Unit

    base_inventory_unit_id - ID of the base unit of measurement. See the Unit API for available units.

    description - description

    external_id - a string field for storing id of the element from an external system

    description - description

    (readonly) created_at - Time when WhItem record was created

    (readonly) updated_at - Last time when WhItem record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resurche

    Changes

    Changes Ids

    Mass Request

Filters by

id, related_object_type, related_object_id, wh_item_group_id
Comparison filters by (for more info see)

created_at, updated_at
WhItemGroup

operations.cropwise.com/api/v3/wh_item_groups
WhItemGroup relations

    WhItemGroup has many wh_items

WhItemGroup has next attributes

    (readonly) id - Cropwise Operations Platform ID of WhItemGroup

    group_type - group type of WhItemGroup ('seed', 'chemical', 'fertilizer', 'spare_part', 'other')

    record_type - Can be system- provided by Cropwise Operations Platform or user - created by user

    user_name - name of WhItemGroup

    (readonly) system_name - system name of WhItemGroup

    description - description

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - Time when WhItemGroup record was created

    (readonly) updated_at - Last time when WhItemGroup record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resurche

    Changes

    Changes Ids

    Mass Request

Filters by

id, group_type, record_type
Comparison filters by (for more info see)

created_at, updated_at
WhDocument

operations.cropwise.com/api/v3/wh_documents
WhDocument relations

    WhDocument belongs to Warehouse

    WhDocument belongs to Unit

    WhDocument belongs to Counterparty

    WhDocument belongs to Field

    WhDocument belongs to User

    WhDocument belongs to RelatedDocument

    WhDocument has many WhItems

    WhDocument has many WhDocumentItems

WhDocument has next attributes

    (readonly) id - Cropwise Operations Platform ID of WhDocument

    document_time - time of document

    document_type - type of document ('goods_receipt', 'goods_issue', 'stock_transfer')

    document_status - status of document ('draft', 'accepted')

    from_warehouse_id - Cropwise Operations Platform ID of Warehouse (defined only for 'goods_receipt' and 'stock_transfer' document type)

    to_warehouse_id - Cropwise Operations Platform ID of Warehouse (defined only for 'goods_issue' and 'stock_transfer' document type)

    counterparty_id - Cropwise Operations Platform ID of Counterparty (defined only for 'goods_receipt' document type)

    created_by_id - Cropwise Operations Platform ID of User

    document_number - a string field for storing number of document

    related_document_type - type of related document ('AgroOperation')

    related_document_id - Cropwise Operations Platform ID related document

    (readonly) creation_type - creation type of document ('manual', 'automatic')

    season - the season (year in format "yyyy") of the document

    field_id - Cropwise Operations Platform ID of Field

    additional_info - additional info

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - Time when WhDocument record was created

    (readonly) updated_at - Last time when WhDocument record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resurche

    Changes

    Changes Ids

    Mass Request

Filters by

id, document_type, document_status, from_warehouse_id, to_warehouse_id, counterparty_id, document_number, season, field_id, external_id
Comparison filters by (for more info see)

document_time, created_at, updated_at
WhRelatedDocumentAssignment

operations.cropwise.com/api/v3/wh_related_document_assignments
WhRelatedDocumentAssignment relations

    WhRelatedDocumentAssignment belongs to WhDocument

WhRelatedDocumentAssignment has next attributes

    (readonly) id - Cropwise Operations Platform ID of WhItemUnitAssignment

    related_document_type - type of related document (AgroOperation, WhDocument, MaintenanceRecord)

    related_document_id - Cropwise Operations Platform ID of related document

    wh_document_id - Cropwise Operations Platform ID of WhDocument

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - Time when WhItemUnitAssignment record was created

    (readonly) updated_at - Last time when WhItemUnitAssignment record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resurche

    Changes

    Changes Ids

    Mass Request

Filters by

id, related_document_type, related_document_id, wh_document_id, external_id
Comparison filters by (for more info see)

created_at, updated_at
WhDocumentItem

operations.cropwise.com/api/v3/wh_document_items
WhDocumentItem relations

    WhDocumentItem belongs to WhDocument

    WhDocumentItem belongs to WhItem

    WhDocumentItem belongs to Unit

    WhDocumentItem belongs to ApplicationMixItem

WhDocumentItem has next attributes

    (readonly) id - Cropwise Operations Platform ID of WhDocumentItem

    wh_item_id - Cropwise Operations Platform ID of WhItem

    position - a number field of WhItem sequence number

    quantity - a number field of quantity

    total_cents - total amount for all quantity in cents

    variant - a string field for storing a variant name

    expiration_date - a string field for storing expiration date of WhItem YYYY-MM-DD

    wh_document_id - Cropwise Operations Platform ID of WhDocument

    unit_id - Cropwise Operations Platform ID of Unit

    (readonly) quantity_in_base_units - quantity in current base unit

    (readonly) created_at - Time when WhDocumentItem record was created

    (readonly) updated_at - Last time when WhDocumentItem record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resurche

    Changes

    Changes Ids

    Mass Request

Filters by

id, wh_document_id, wh_item_id
Comparison filters by (for more info see)

created_at, updated_at
WarehouseRelatedObjectAssignment

operations.cropwise.com/api/v3/warehouse_related_object_assignments
WarehouseRelatedObjectAssignment relations

    Warehouse belongs to Warehouse

    Warehouse belongs to RelatedObject

WarehouseRelatedObjectAssignment has next attributes

    (readonly) id - Cropwise Operations Platform ID of WarehouseRelatedObjectAssignment

    warehouse_id - Cropwise Operations Platform ID of Warehouse

    related_object_type - type of releted object ('Field', 'FieldGroup', 'GroupFolder', 'User', 'AdditionalObject')

    related_object_id - Cropwise Operations Platform ID of releted object

    (readonly) created_at - Time when WarehouseRelatedObjectAssignment record was created

    (readonly) updated_at - Last time when WarehouseRelatedObjectAssignment record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resurche

    Changes

    Changes Ids

    Mass Request

Filters by

id, warehouse_id, related_object_type, related_object_id
Comparison filters by (for more info see)

created_at, updated_at
WhSettings

operations.cropwise.com/api/v3/wh_settings

This API resource has one access method and returns company WhSettings information.
WhSettings object has next attributes

All parameters are readonly

    id - Cropwise Operations Platform ID of Company

    auto_goods_issue_status - the goods issue document will be created with the given status

    auto_goods_issue_from_warehouse - the system will install the first warehouse associated with the specified type

    api_auto_goods_issue_from_warehouse - the system will install the first warehouse associated with the specified type if the desired warehouse is not specified in the parameters (when use API)

    auto_goods_issue - depending on the type of creating entries (agro operations/machine tasks), the system automatic will create a goods issue document

    control_stocks_when_accepted_document - if true it is forbidden to accept documents with a negative balance

Example success response:

{
    "data": {
        "id": 1,
        "auto_goods_issue_status": "accepted",
        "auto_goods_issue_from_warehouse": "responsible",
        "auto_goods_issue": true,
        "api_auto_goods_issue_from_warehouse": "responsible",
        "control_stocks_when_accepted_document": false,
        "created_at": "2023-05-11T09:17:44.351+03:00",
        "updated_at": "2024-04-16T10:52:34.590+03:00",
    }
}

WhStocks

operations.cropwise.com/api/v3/wh_stocks
WhStocks has next attributes

    (readonly) id - Cropwise Operations Platform ID of WhDocumentItem

    stock - warehouse stocks

    value_cents - cents value (present if )

    warehouse_id - Cropwise Operations Platform ID of Warehouse

    wh_item_id - Cropwise Operations Platform ID of WhItem

    variant - a string field for storing a variant name

    expiration_date - a string field for storing expiration date of WhItem YYYY-MM-DD

    unit_id - Cropwise Operations Platform ID of Unit

    (readonly) created_at - Time when WhDocumentItem record was created

    (readonly) updated_at - Last time when WhDocumentItem record was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

Filters by

time, wh_item_id, warehouse_id, variant, expiration_date
Comparison filters by (for more info see)

created_at, updated_at
Example request GET list of items:

https://operations.cropwise.com/api/wh_stocks?warehouse_id=1&time=2023-08-20'
Example success response:

{
"data": [
    {
    "stock": "90.0",
    "value_cents": "9000.0",
    "warehouse_id": 1,
    "id": 321,
    "wh_item_id": 1793,
    "unit_id": 21,
    "variant": "green",
    "expiration_date": "2023-08-27T00:00:00.000+03:00"
    }
  ]
}

WeatherHistoryItems

operations.cropwise.com/api/v3/weather_history_items

for VirtualWeatherStation see link
WeatherHistoryItems relations

    WeatherHistoryItem belongs to field_group.

WeatherHistoryItems has next attributes:

    date - date of record

    temperature_min - minimal temperature value

    temperature_avg - average temperature value

    temperature_max - maximal temperature value

    precipitation - precipation level, millimeters

    snow - snow level, millimeters

    field_group_id - Cropwise Operations Platform ID FieldGroup

Acceptable methods

    Resources Collection

Query params and meta

You can pass next params to this resource:

    field_group_id - Cropwise Operations Platform ID of FieldGroup. Required!

    from_time - begining of time range. Default is 24 hours ago.

    to_time - end of time range. Default is current time.

Example:

https://operations.cropwise.com/api/v3/weather_history_items?field_group_id=622&from_time=2012-01-01&to_time=2012-12-31

The 'meta' block in this resource deffers from typical 'meta' in other resources.

{ "request": { "field_group_id": "622", "from_time": "2012-01-01T00:00:00.000+00:00", "to_time": "2012-12-31T00:00:00.000+00:00", "server_time": "2015-04-24T11:02:06.050+03:00" }, "response": { "from_time": "2012-01-01T00:00:00.000+00:00", "to_time": "2012-12-31T00:00:00.000+00:00", "obtained_records": 366 } }
WeatherHistoryItems/v3a

operations.cropwise.com/api/v3a/weather_history_items

for VirtualWeatherStation see link
WeatherHistoryItems relations

    WeatherHistoryItem belongs to weather_historyable (FieldGroup, SharedWeatherStation, WeatherStation or WmoWeatherStation).

WeatherHistoryItems has next attributes:

    (readonly) id - Cropwise Operations Platform ID of WeatherHistoryItem.

    (readonly) weather_historyable_type - type of weather_historyable object

    (readonly) weather_historyable_id - ID of weather_historyable object

    (readonly) year - year

    (readonly) value - array of daily values [date, temperature mean (C), temperature min. (C), temperature max. (C), daily precipitations (mm), snow depth (m), wind_speed (m/s)].

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Mass Request

    Single Resource

    Ids

    Changes

    Changes Ids

    Resources Collection

Filters by

weather_historyable_type, weather_historyable_id, year
Query examples

https://operations.cropwise.com/api/v3a/weather_history_items?weather_historyable_type=WeatherStation&weather_historyable_id=8767&year=2021,2022

Note! For WmoWeatherStation you can obtain historical data by passing Cropwise Operations Platform ID as parameter:

https://operations.cropwise.com/api/v3a/weather_history_items?wmo_weather_station_id=100071&year=2021,2022
WeatherHistoryItems/v3b

operations.cropwise.com/api/v3b/weather_history_items

The same endpoint as weather-history-items/v3a, except only the value attribute:

    (readonly) value - JSON encoded string of daily values [date, temperature mean (C), temperature min. (C), temperature max. (C), daily precipitations (mm), snow depth (m), wind_speed (m/s)].

WeatherHistoryItems/v3c

operations.cropwise.com/api/v3c/weather_history_items

The same endpoint as weather-history-items/v3a, except only the value attribute:

    (readonly) value - hash of daily values with dates:

      {
          "2022-01-01": {
              "snow": 0.88,
              "wind_speed": 7.09,
              "precipitation": 0.0,
              "temperature_max": 2.43,
              "temperature_min": -2.7,
              "temperature_mean": 0.02
          },
          "2022-01-02": {
              "snow": 0.48,
              "wind_speed": 6.65,
              "precipitation": 0.5,
              "temperature_max": -0.35,
              "temperature_min": -3.07,
              "temperature_mean": -1.5
          },
          ...
      }

List of possible meteo parameters (depends on weather station type, data provider, etc.)

    temperature_mean - average daily air temperature (C°)

    temperature_max - maximal daily air temperature (C°)

    temperature_min - minimal daily air temperature (C°)

    dew_point - dew point (C°)

    crop_heat_units - amount of daily crop heat units (C°)

    growing_degree_day - daily growing degree-days (C°)

    wind_speed - avarage daily speed of wind (meters / seconds)

    wind_direction - average daily direction of wind (degrees)

    precipitation - daily amount of precipation (millimeters)

    precipitation_era5t - precipitation level from ERA5 data source (millimeters)

    evaporation - daily amount of water evaporation (millimeters)

    soil_water_balance - daily amount of water balance of soil (millimeters)

    snow - snow depth (meters)

    relative_humidity - average daily relative humidity (ratio)

    soil_moisture_1 - average daily soil moisture at first level (ratio)

    soil_moisture_2 - average daily soil moisture at second level (ratio)

    soil_moisture_3 - average daily soil moisture at third level (ratio)

    soil_temperature_1 - average daily soil temperature at first level (C°)

    soil_temperature_2 - average daily soil temperature at second level (C°)

    soil_temperature_3 - average daily soil temperature at third level (C°)

    solar_radiation - daily amount of solar radiation (Watts / square meters)

    leaf_wetness - daily amount leaf wetness (minutes)

WeatherItem

operations.cropwise.com/api/v3/weather_items
WeatherItem relations

    WeatherItem belongs to weatherable.

WeatherItem has next attributes (all read-only)

    (readonly) id - Cropwise Operations Platform ID of WeatherItem.

    (readonly) weatherable_type - Cropwise Operations Platform type of weatherable: "FieldGroup", "WeatherStation".

    (readonly) weatherable_id - Cropwise Operations Platform ID of weatherable (FieldGroup, WeatherStation).

    (readonly) longitude - longitude of weatherable object geoposition.

    (readonly) latitude - latitude of weatherable object geoposition.

    (readonly) current_data - hash of current data parameters with values.

    (readonly) forecast_hourly - hash of hourly forecast data parameters with values.

    (readonly) forecast_daily - hash of daily forecast data parameters with values.

    (readonly) additional_forecast - hash of forecast data parameters with values from private weather stations.

    (readonly) generated_at - time when forecast generated on weather service.

    (readonly) created_at - time when object created on server.

    (readonly) updated_at - last time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, weatherable_id, weatherable_type, generated_at, created_at, updated_at
Comparison filters by (for more info see)

generated_at, created_at, updated_at
WeatherStationFieldShapeMappingItems

operations.cropwise.com/api/v3/weather_station_field_shape_mapping_items
WeatherStationFieldShapeMappingItems relations

    WeatherStationFieldShapeMappingItem belongs to FieldShape.

    WeatherStationFieldShapeMappingItem belongs to weather_station (SharedWeatherStation, VirtualWeatherStation, WeatherStation or WmoWeatherStation).

WeatherStationFieldShapeMappingItems has next attributes (all read-only):

    (readonly) id - Cropwise Operations Platform ID of WeatherHistoryItem.

    (readonly) weather_station_type - Cropwise Operations Platform type of weather_station object: "SharedWeatherStation", "VirtualWeatherStation", "WeatherStation" or "WmoWeatherStation".

    (readonly) weather_station_id - ID of weather_station object

    (readonly) field_shape_id - ID of FieldShape object

    (readonly) distance - distance between field shape center and weather station in kilometers

    (readonly) prior - a boolean flag indicating whether the weather station is prioritized

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Single Resource

    Ids

    Changes

    Changes Ids

    Mass Request

Sorting by (for more info see)

id, created_at, updated_at, distance
Comparison filters by (for more info see)

created_at, updated_at, distance
Additional info

There are some limitations on the number of weather stations in radius for each type.
WeatherStations

operations.cropwise.com/api/v3/weather_stations
WeatherStations has next attributes (all read-only):

    (readonly) id - Cropwise Operations Platform ID of WeatherStation.

    (readonly) name - weather station name.

    (readonly) longitude - longitude of weather station geoposition.

    (readonly) latitude - latitude of weather station geoposition.

    (readonly) current_weather - only on single station, hourly weather data array for last 24h obtained, changing each 1h (see example below)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Single Resource

    Ids

    Changes

    Changes Ids

    Mass Request

The attribute current_weather example:

[
      {
        "time": "2024-06-11T11:00:00.000+03:00",
        "precipitation": {
          "sum": 0
        },
        "air_temperature": {
          "aver": 23.9,
          "max": 25.13,
          "min": 22.86
        },
        "leaf_wetness": {
          "time": 0
        },
        "relative_humidity": {
          "aver": 76.72,
          "max": 81.77,
          "min": 68.25
        },
        "dew_point": {
          "aver": 19.5,
          "min": 18.7
        },
        "soil_moisture": {
          "aver": 44.88
        },
        "soil_moisture_1": {
          "aver": 18.47
        },
        "soil_moisture_2": {
          "aver": 36.11
        },
        "soil_temperature": {
          "aver": 17.9,
          "max": 18.1,
          "min": 17.9
        }
      }
    ]

WeatherStationsData

operations.cropwise.com/api/v3/weather_stations_data

This endpoint for receive current weather by collection of weather stations.
WeatherStations has next attributes (all read-only):

    (readonly) id - Cropwise Operations Platform ID of WeatherStation.

    (readonly) current_weather - hourly weather data array for last 24h obtained, changing each 1h (see example into WeatherStations section)

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

Filters by

id
Comparison filters by (for more info see)

created_at, updated_at
WmoWeatherStations

operations.cropwise.com/api/v3/wmo_weather_stations

WMO stands for World Meteorological Organization. This is public type of weather stations. Most of them are government weather stations and observatories.
WmoWeatherStations has next attributes (all read-only):

    (readonly) id - Cropwise Operations Platform ID of WmoWeatherStation.

    (readonly) name - WMO weather station name.

    (readonly) longitude - longitude of wmo weather station geoposition.

    (readonly) latitude - latitude of wmo weather station geoposition.

    (readonly) elevation - elevation of wmo weather station geoposition.

    (readonly) wmo_code - WMO identifier (index number). 5-digit numeric code.

    (readonly) created_at - time when object created on server.

    (readonly) updated_at - last time when object was updated.

Acceptable methods

    Resources Collection

    Single Resource

    Ids

    Changes

    Changes Ids

    Mass Request

WorkRecord

operations.cropwise.com/api/v3/work_records

WorkRecord keeps work history of dispatchers.
Relations

    Belongs to User.

    Has many WorkRecordMachineRegionMappingItems.

    Has many MachineRegions (through WorkRecordMachineRegionMappingItems).

Has next attributes (all read-only)

    (readonly) id - Cropwise Operations Platform ID of WorkRecord.

    (readonly) user_id - User ID.

    (readonly) start_time - Start time of work.

    (readonly) end_time - End time of work.

    (readonly) work_type - Work type (one of: dispatcher).

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

WorkRecordMachineRegionMappingItem

operations.cropwise.com/api/v3/work_record_machine_region_mapping_items

WorkRecordMachineRegionMappingItem is many-to-many relation between WorkRecords and MachineRegions.
Relations

    Belongs to WorkRecord.

    Belongs to MachineRegion.

Has next attributes (all read-only)

    (readonly) id - Cropwise Operations Platform ID of WorkRecordMachineRegionMappingItem.

    (readonly) work_record_id - WorkRecord ID.

    (readonly) machine_region_id - MachineRegion ID.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

WorkType

operations.cropwise.com/api/v3/work_types

WorkType keep available WorkTypes (WorkTypes used in MachineTask, AgroOperation, AgriWorkPlan).
Relations

    Belongs to WorkTypeGroup (required).

    Has many MachineTasks.

    Has many AgroOperations.

    Has many AgriWorkPlans.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkRecordMachineRegionMappingItem.

    work_type_group_id - WorkTypeGroup ID.

    name - Name of WorkType.

    agri - Is it 'agri' type (boolean).

    application - Is it 'application' type (boolean).

    sowing - Is it 'sowing' type (boolean).

    harvesting - Is it 'harvesting' type (boolean).

    soil - Is it 'soil' type (boolean).

    standard_name - Standard name. Reserved field for default WorkTypes.

    hidden - Is it hidden (boolean).

    description - Description.

    external_id - ID for external system (string, must be UNIQUE).

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, standard_name, external_id, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at

Group WorkTypeAllowedCrops (LEGACY! Use AllowedToCrops)

operations.cropwise.com/api/v3/work-type-allowed-crops
WorkTypeAllowedCrops relations

    WorkTypeAllowedCrops belongs to WorkType

    WorkTypeAllowedCrops belongs to Crop

WorkTypeAllowedCrops has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkTypeAllowedCrops

    (immutable) work_type_id - Cropwise Operations Platform ID of WorkType

    (immutable) crop_id - Cropwise Operations Platform ID of Crop

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object created on server

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, work_type_id, crop_id, external_id
Comparison filters by (for more info see)

created_at, updated_at
WorkTypeGroup

operations.cropwise.com/api/v3/work_type_groups

WorkTypeGroup keep groups for WorkTypes.
Relations

    Has many WorkTypes.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkRecordMachineRegionMappingItem.

    name - Name of WorkTypeGroup.

    standard_name - Standard name. Reserved field for default WorkTypesGroups.

    description - Description.

    external_id - ID for external system (string, must be UNIQUE).

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, work_type_group_id, name, agri, application, sowing, harvesting, soil, standard_name, hidden, created_at, updated_at
Comparison filters by (for more info see)

created_at, updated_at

WorkTypeMeasurements

operations.cropwise.com/api/v3/work_type_measurements
Relations

    Belongs to Unit.

    Has many WorkTypes (required).

    Has many WorkTypeMeasurementMixItems.

    Has many WorkTypeMeasurementMappingItems.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkTypeMeasurement.

    work_type_id - WorkType ID.

    name - Name of WorkType.

    data_type - It is type of data (string, integer, float, datetime, date, boolean, select, multi_select).

    hidden - Is it hidden (boolean).

    presence - Is it presence (boolean).

    additional_info - Additional info.

    description - Description.

    external_id - ID for external system (string, must be UNIQUE).

    unit_id - ID of Unit.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, data_type, hidden, presence, unit_id, external_id
Comparison filters by (for more info see)

created_at, updated_at

WorkTypeMeasurementMappingItems

operations.cropwise.com/api/v3/work_type_measurement_mapping_items
Relations

    Belongs to WorkTypeMeasurement.

    Belongs to WorkType.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkTypeMeasurementMappingItem.

    work_type_measurement_id - WorkTypeMeasurement ID.

    work_type_id - WorkType ID.

    external_id - ID for external system (string, must be UNIQUE).

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, work_type_measurement_id, work_type_id
Comparison filters by (for more info see)

created_at, updated_at

WorkTypeMeasurementMixItem

operations.cropwise.com/api/v3/work_type_measurement_mix_items
Relations

    Belongs to WorkTypeMeasurement.

    Belongs to WorkType.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkTypeMeasurementMappingItem.

    measurable_type - Measurable type (AgroOperation).

    measurable_id - Measurable ID.

    work_type_measurement_id - WorkTypeMeasurement ID.

    value - value of work type measurement.

    external_id - ID for external system (string, must be UNIQUE).

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, measurable_type, measurable_id, work_type_measurement_id, value, external_id
Comparison filters by (for more info see)

created_at, updated_at

WorkTypeMeasurements/v3a

operations.cropwise.com/api/v3a/work_type_measurements
Relations

    Belongs to Unit.

    Has many WorkTypes (required).

    Has many WorkTypeMeasurementMixItems.

    Has many WorkTypeMeasurementMappingItems.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkTypeMeasurement.

    work_type_id - WorkType ID.

    name - Name of WorkType.

    data_type - It is type of data (string, integer, float, datetime, date, boolean, select, multi_select).

    hidden - Is it hidden (boolean).

    presence - Is it presence (boolean).

    additional_info - Additional info.

    description - Description.

    external_id - ID for external system (string, must be UNIQUE).

    unit_id - ID of Unit.

    idempotency_key - The idempotency key transmitted during the request, if any.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, name, data_type, hidden, presence, unit_id, external_id
Comparison filters by (for more info see)

created_at, updated_at

WorkTypeMeasurementMappingItems/v3a

operations.cropwise.com/api/v3a/work_type_measurement_mapping_items
Relations

    Belongs to WorkTypeMeasurement.

    Belongs to WorkType.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkTypeMeasurementMappingItem.

    work_type_measurement_id - WorkTypeMeasurement ID.

    work_type_id - WorkType ID.

    external_id - ID for external system (string, must be UNIQUE).

    idempotency_key - The idempotency key transmitted during the request, if any.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, work_type_measurement_id, work_type_id
Comparison filters by (for more info see)

created_at, updated_at

WorkTypeMeasurementMixItem/v3a

operations.cropwise.com/api/v3a/work_type_measurement_mix_items
Relations

    Belongs to WorkTypeMeasurement.

    Belongs to WorkType.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of WorkTypeMeasurementMappingItem.

    measurable_type - Measurable type (AgroOperation).

    measurable_id - Measurable ID.

    work_type_measurement_id - WorkTypeMeasurement ID.

    value - value of work type measurement.

    external_id - ID for external system (string, must be UNIQUE).

    idempotency_key - The idempotency key transmitted during the request, if any.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

id, measurable_type, measurable_id, work_type_measurement_id, value, external_id
Comparison filters by (for more info see)

created_at, updated_at
YieldMaps

operations.cropwise.com/api/v3/yield_maps
YieldMap relations

    YieldMap belongs to Field. Required.

    YieldMap belongs to FieldWorkResult. Required.

YieldMap has next attributes

    (readonly) id - Cropwise Operations Platform ID of YieldMap

    field_id - Cropwise Operations Platform ID of Field

    field_work_result_id - Cropwise Operations Platform ID of FieldWorkResult

    description - description

    property_name - type of map, for example: "moisture", "yield", "applied"

    calculated_average - internally calculated average value by map

    external_average - average value by map from external API

    totals - totals into json format

    external_id - a string field for storing id of the element from an external system

    (readonly) created_at - time when object was created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Count

    Single Resource

    Changes

    Changes Ids

    External ids

Filters by

field_id
Comparison filters by (for more info see)

created_at, updated_at
Sorting by (for more info see)

id, created_at, updated_at
ScoutReportTemplate

operations.cropwise.com/api/v3/scout_report_templates
Relations

    Has many ScoutReportTemplateCropAssignment.

    Has many ScoutReportTemplateMeasurementTypeAssignment.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of template.

    name - Name of template.

    description - Description.

    external_id - ID for external system (string, must be UNIQUE).

    idempotency_key - The idempotency key transmitted during the request, if any.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

ScoutReportTemplateCropAssignment

operations.cropwise.com/api/v3/scout_report_template_crop_assignments
Relations

    ScoutReportTemplateCropAssignment belongs to ScoutReportTemplate

    ScoutReportTemplateCropAssignment belongs to Crop

Object has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportTemplateCropAssignment

    crop_id - Cropwise Operations Platform ID of the Crop

    scout_report_template_id - Cropwise Operations Platform ID of related ScoutReportTemplate

    external_id - ID for external system (string, must be UNIQUE).

    idempotency_key - The idempotency key transmitted during the request, if any.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

ScoutReportTemplateMeasurementTypeAssignment

operations.cropwise.com/api/v3/scout_report_template_measurement_type_assignments
Relations

    ScoutReportTemplateCropAssignment belongs to ScoutReportTemplate

    ScoutReportTemplateCropAssignment belongs to ScoutReportMeasurementType

Object has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportTemplateCropAssignment

    scout_report_measurement_type_id - Cropwise Operations Platform ID of the ScoutReportMeasurementType

    scout_report_template_id - Cropwise Operations Platform ID of related ScoutReportTemplate

    external_id - ID for external system (string, must be UNIQUE).

    idempotency_key - The idempotency key transmitted during the request, if any.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

ScoutReportMeasurementType

operations.cropwise.com/api/v3/scout_report_measurement_types
Relations

    Belongs to Unit. Optional

    Has many ScoutReportPointMeasurements

    Has many ScoutReportMeasurementValueTypes

    Has many ScoutReportTemplateMeasurementTypeAssignments

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportMeasurementType

    human_name - Localised name. Example Density of planting using square meters

    system_name - System name. Example density_of_planting_linear_millions_per_ha

    record_type - Can be system- provided by Cropwise Operations Platform or user - created by user.

    hidden - Is it hidden (boolean).

    calculate_value_expression - String. Formula for calculation calculated_value in ScoutReportPointMeasurement. Only +, -, (, ), *, / signs can be used. Example: "plants_in_rows / (row_width / 100.0 * length_of_row * rows_count)"

    calculated_value_unit_id - Cropwise Operations Platform ID of the Unit for the calculated_value

    round_precision - Accuracy of rounding calculated_value then display.

    max_possible_value - Maximum possible value of calculated value.

    min_possible_value - Minimum possible value of calculated value.

    description - some description

    external_id - a string field for storing id of the element from an external system

    idempotency_key - The idempotency key transmitted during the request, if any

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

ScoutReportMeasurementValueType

operations.cropwise.com/api/v3/scout_report_measurement_value_types
Relations

    Belongs to Unit. Optional

    Belongs to ScoutReportMeasurementType

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of ScoutReportMeasurementValueType

    scout_report_measurement_type_id - Cropwise Operations Platform ID of ScoutReportMeasurementType.

    human_name - Localised name. Example Row width

    system_name - System name. Example row_width

    record_type - Can be system- provided by Cropwise Operations Platform. user - created by user.

    unit_id - Cropwise Operations Platform ID of the Unit

    data_type - String. NOT NULL. One of string, integer, float, datetime, date, boolean, select, multi_select.

    select_list_items - Json. If data_type is select or multi_select it should be select list. Example: [ { 'label': 'One', 'value': 'One' }, { 'label': 'Two', 'value': 'Two' } ]

    description - some description

    external_id - a string field for storing id of the element from an external system

    idempotency_key - The idempotency key transmitted during the request, if any

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

    (readonly)validation_descriptions - Array localized validation descriptions

    (readonly)validation_rules - Json.

        Inclusion in the specified set:

        { "inclusion": "true", "inclusion_options": { "in": ["www", "us", "ca", "jp"] }

        Length Validation:

        { "length": "true", "length_options": { "minimum": 2 }

        Options:
            :minimum - attribute cannot be less than a certain length.
            :maximum - attribute cannot be more than a certain length.
            :is - length of the attribute must be equal to the specified value.

        Numerical values:

        { "numericality": "true", "numericality_options": { "only_integer": true } }

        Options:
            :greater_than - value must be greater than the option value.
            only_integer - regex will be used /\A[+-]?\d+\z/
            :greater_than_or_equal_to - value must be greater than or equal to the option value.
            :equal_to - value should be equal to the option value.
            :less_than - value should be less than the option value.
            :less_than_or_equal_to - value must be less than or equal to the option value.
            :other_than - value should be different from the option value.
            :odd - value should be odd if set to true.
            :even - value should be even if set to true.

        Not empty value:

        { "presence": "true" }

        Skips checking if the value being checked is null:

        { "allow_nil": "true" }

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Unit

operations.cropwise.com/api/v3/units
Relations

    Has many ScoutReportMeasurementType

    Has many ScoutReportMeasurementValueType

Has next attributes

    (readonly) id - Cropwise Operations Platform ID of Unit

    human_name - Localised name. Example plants/m²

    system_name - System name. Example plants_m2

    record_type - Can be system- provided by Cropwise Operations Platform. user - created by user.

    description - some description

    external_id - a string field for storing id of the element from an external system

    idempotency_key - The idempotency key transmitted during the request, if any

    (readonly) created_at - time when object created

    (readonly) updated_at - last time when object was updated

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Security

operations.cropwise.com/api/v3/security
Log out users

Empty POST request to next URL will close all Web & API sessions of User:

https://operations.cropwise.com/api/v3/security/forced_log_out/users/USER_ID

Could be useful in case of stolen mobile device, or for any other security reasons.
PenetrometerSoilTests

operations.cropwise.com/api/v3/penetrometer_soil_tests
Create soil tests for data from penetrometers
Body params

You need to pass next body param to this request:

    data - resource json data format

    description - description what will be included to all created soil tests

    step - ground density step for penetrommeter in mm (default is 25mm if leave this param empty)

Example request:

https://operations.cropwise.com/api/v3/penetrometer_soil_tests
Example body params.

 {
    "description": "soil test description",
    "step": "25",
    "data": [
        {
          "ground_density": "[47,88,164,339,745,900]",
          "lat": "49.68229291181481",
          "lng": "32.36864398912474",
          "created": "2018-03-22T17:47:59+02:00"
        },
        {
          "ground_density": "[1523,3033,3615,3434,3668,2433]",
          "lat": "49.67980225265401",
          "lng": "32.36178429034564",
          "created": "2018-03-17T17:48:27+02:00"
        },
        {
          "ground_density": "[132,202,263,318,473,646,745,1174]",
          "lat": "49.67970645552301",
          "lng": "32.36116741095904",
          "created": "2018-03-17T17:48:27+02:00"
        },
        {
          "ground_density": "[874,2719,3120,3539,3693,3430,3664,2277,2273,2755,3615,1918]",
          "lat": "49.67949889442501",
          "lng": "32.36087130885344",
          "created": "2018-03-17T17:48:27+02:00"
        }
    ]
 }

Example success response:

 {
    "data": {
        "success": true,
        "message": "Soil tests successfully added or updated",
        "soil_tests": [
            {
                "api_link": "https://operations.cropwise.com/api/v3/soil_tests/{SOIL_TEST_ID}",
                "id": 1557,
                "field_id": 74338,
                "elements": {
                    "ground_density_0": 132,
                    "ground_density_25": 202,
                    "ground_density_50": 263,
                    "ground_density_75": 318,
                    "ground_density_100": 473,
                    "ground_density_125": 646,
                    "ground_density_150": 745,
                    "ground_density_175": 1174
                },
                "made_at": "2018-03-17",
                "soil_test_samples": [
                    {
                        "id": {SOIL_TEST_SAMPLE_ID},
                        "soil_test_id": {SOIL_TEST_ID},
                        "lonlat": "POINT (32.36116741095904 49.67970645552301)",
                        "elements": {
                            "ground_density_0": 132,
                            "ground_density_25": 202,
                            "ground_density_50": 263,
                            "ground_density_75": 318,
                            "ground_density_100": 473,
                            "ground_density_125": 646,
                            "ground_density_150": 745,
                            "ground_density_175": 1174
                        },
                        "created_at": "2019-08-29T14:07:27.088+03:00",
                        "updated_at": "2019-08-29T14:07:27.088+03:00"
                    }
                ],
                "created_at": "2019-08-29T14:07:26.990+03:00",
                "updated_at": "2019-08-29T14:07:26.990+03:00"
            }
        ]
    }
}

ExternalServiceItems

operations.cropwise.com/api/v3/external_service_items
GET available integrated data
Body params

You need to pass next body param to this request:

    integration_type - type of integration, one of [my_john_deere claas cnh meteozahist seed_selector] — required!

    item_type - type of mappable Model you want to access(default will return all available data)

    org_id - find items by organisation ID (available only for seed_selector integration_type)

    req_id - find items by request ID (available only for seed_selector integration_type)

Filters by

item_id, item_type, external_item_id, external_item_status
Example request GET list of items by org_id param:

https://operations.cropwise.com/api/v3/external_service_items?integration_type=seed_selector&org_id=793491f2-790c-4dc4-bb64-0f1a330da54e
Example success response:

{
  "data":[
    {
      "id":14846,
      "item_type":"FieldGroup",
      "item_id":"Field Group ID",
      "external_item_id":"External Service Field Group ID",
      "external_item_updated_at":null,
      "additional_info":null,
      "external_item_status":"pending",
      "created_at":"2021-11-15T11:32:42.306+02:00",
      "updated_at":"2021-11-15T11:32:42.306+02:00"
    },
    {
      "id":14847,
      "item_type":"Field",
      "item_id":"Field ID",
      "external_item_id":"External Service Field ID",
      "external_item_updated_at":null,
      "additional_info":null,
      "external_item_status":"pending",
      "created_at":"2021-11-15T11:32:51.804+02:00",
      "updated_at":"2021-11-15T11:32:51.804+02:00"
    }
  ],
  "meta":{
    "request":{
      "from_id":0,
      "limit":null,
      "server_time":"2021-12-07T14:46:46.226+02:00"
    },
    "response":{
      "limit":1000,
      "obtained_records":2,
      "first_record_id":14846,
      "last_record_id":14847
    }
  }
}

Example request GET list of items:

https://operations.cropwise.com/api/v3/external_service_items?integration_type=meteozahist&model_type=FieldShape
Example success response:

{
    "data": [
        {
            "id": 32,
            "item_type": "FieldShape",
            "item_id": 117934,
            "external_item_id": "need to update",
            "external_item_updated_at": null,
            "additional_info": null,
            "external_item_status": "pending",
            "created_at": "2020-01-30T11:12:08.789+02:00",
            "updated_at": "2020-01-30T11:12:08.789+02:00"
        },
        {
            "id": 33,
            "item_type": "FieldShape",
            "item_id": 118153,
            "external_item_id": "need to update",
            "external_item_updated_at": null,
            "additional_info": null,
            "external_item_status": "pending",
            "created_at": "2020-01-30T11:12:09.807+02:00",
            "updated_at": "2020-01-30T11:12:09.807+02:00"
        }
    ],
    "meta": {
        "request": {
            "from_id": 0,
            "limit": null,
            "server_time": "2020-01-30T13:55:27.595+02:00"
        },
        "response": {
            "limit": 1000,
            "obtained_records": 2,
            "first_record_id": 32,
            "last_record_id": 33
        }
    }
}

Example request PUT item:

https://operations.cropwise.com/api/v3/external_service_items/32

{
  "data": {
    "additional_info": "link",
    "external_item_status": "enabled"
  }
}

Example success response:

{
    "data": {
        "id": 32,
        "item_type": "FieldShape",
        "item_id": 117934,
        "external_item_id": "need to update",
        "external_item_updated_at": null,
        "additional_info": "link",
        "external_item_status": "enabled",
        "created_at": "2020-01-30T11:12:08.789+02:00",
        "updated_at": "2020-01-30T11:12:08.789+02:00"
    }
}

GeoRasterImages

operations.cropwise.com/api/v3/geo_raster_images
Demands to images taken by drones

To upload your drone imagery, we require the imagery to be a GeoTIFF file. A GeoTIFF includes georeferencing information embedded into the TIFF file. Maximum file size supported is 4GB.

Visible: available format is GeoTIFF with 3 RGB layers. The metadata should include the projection parameters, geo-referencing, the value of NoData. NDVI: available format is GeoTIFF with 1 Gray layer. The metadata should include the projection parameters, geo-referencing, the value of NoData. By uploading this type of the picture you need to specify the x and y coefficients with which the vegetation index will be calculated according to the formula: NDVI = pixel value / x + y.
Relations

    Has many Fields.

Has next attributes

    (readonly) id - Cropwise Operations Platform ID.

    name - name of image.

    taken_at - date and time when the image was taken.

    (immutable) crop_to_shape - boolean, if true, the image will be cropped to the field shape active at the taken_at time.

    (immutable) image_data_type - string, type of image data, available values: visible, ndvi.

    description - string, description of image.

    (immutable) ndvi_function_x_argument - float, x argument of NDVI function.

    (immutable) ndvi_function_y_argument - float, y argument of NDVI function.

    (immutable) create_image_url - string, url to download image for processing from external storage Google Drive AWS S3 Google Cloud Storage etc. Image should be available 24 hours after creation.

    external_id - ID for external system (string, must be UNIQUE).

    field_ids - array of field ids, to which the image is attached.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

    (readonly) download_url - url to download image after processing.

    (readonly) tile_server_url - url to tile server with processed image.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Create Resource

    Update Resource

    Delete Resource

    Changes

    Changes Ids

    Mass Request

Filters by

field_ids, image_data_type
Comparison filters by (for more info see)

created_at, updated_at, taken_at
Sorting by (for more info see)

id, created_at, updated_at, taken_at
GeoRasterImageAssignments

operations.cropwise.com/api/v3/geo_raster_image_assignments
Relations

    Belongs to GeoRasterImage

Has next attributes

    (readonly) id - Cropwise Operations Platform ID.

    assignment_id - ID of Assignment object.

    assignment_type - string, type of assignment: Field.

    (readonly) created_at - Server time when object was created.

    (readonly) updated_at - Server time when object was updated.

Acceptable methods

    Resources Collection

    Ids

    Single Resource

    Changes

    Changes Ids

    Mass Request

Filters by

assignment_id, geo_raster_image_id
Comparison filters by (for more info see)

created_at, updated_at
Sorting by (for more info see)

id, created_at, updated_at
Services
FetchFuelData

POST operations.cropwise.com/api/services/v1/fetch_fuel_data
Body params

You need to pass next body param to this request:

    from_time - start of period fuel data is requested for (If not set data for last hour will be shown)

    to_time - end of period fuel data is requested for (If not set data for last hour will be shown)

    object_type - type of object data is requested. Could be [Machine, FuelStation],

    [object_ids] - array of ids of objects

    [object_external_ids] - array of external identifiers

    only_fuel_consumption_accounting - boolean to select data only for data source parameters with fuel_consumption_accounting flag enabled

Example request get list of items:

https://operations.cropwise.com/api/services/v1/fetch_fuel_data'
Example success response:

{
    "data": [
        {
            period_start: 'Tue, 04 Jun 2024 11:00:00.000000000 EEST +03:00', 
            fuel_consumption: 0.20000000000001705, 
            refuel: 0.1, 
            data_source_parameter_id: 2296, 
            fuel_drain: 0.0
        },
    ]
}

