import os
import pathlib

import yaml

BASE_DIR = pathlib.Path(__file__).parent
config_path = BASE_DIR / 'config' / 'app.yaml'


def get_config(path):
    with open(path) as yamlfile:
        return yaml.safe_load(yamlfile)


config = get_config(config_path)

config = {
    'postgres': {
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
    },
}

FCM_SERVER_KEY = os.getenv('FCM_SERVER_KEY', 'token')
NOTIFICATION_TOKEN = os.getenv('NOTIFICATION_TOKEN', 'token')
