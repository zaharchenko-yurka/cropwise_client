import logging
import os


LOG_DIR = ".logs"
LOG_FILE = "cropwise   .log"

def setup_logging():
    '''
    Налаштування логування.
    '''
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE), encoding='utf-8'),
            logging.StreamHandler()
        ]
    )