from configparser import ConfigParser
import os

current_dir = os.getcwd()
config_file_path = os.path.join(current_dir,'..','config','config.conf')
config = ConfigParser()
config.read(config_file_path)

# api keys
CLIENT_ID=config.get('api_keys','CLIENT_ID')
SECRET_KEY=config.get('api_keys','SECRET_KEY')

# database

POSTGRES_USER=config.get('database','POSTGRES_USER')
POSTGRES_PASSWORD=config.get('database','POSTGRES_PASSWORD')
POSTGRES_DB=config.get('database','POSTGRES_DB')
POSTGRES_HOST=config.get('database','POSTGRES_HOST')
POSTGRES_PORT=config.get('database','POSTGRES_PORT')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)

INPUT_PATH=config.get('file_paths','input_path')
OUTPUT_PATH=config.get('file_paths','output_path')