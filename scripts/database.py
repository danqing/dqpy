import sys

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists, drop_database

from dq.config import Config

ACTION_CREATE = 'create'
ACTION_DROP = 'drop'


def create():
    try:
        engine = create_engine(Config.get('mysql.url'))
        if not database_exists(engine.url):
            create_database(engine.url)
    except Exception as e:
        print('Unable to create database: %s' % e)


def drop():
    try:
        engine = create_engine(Config.get('mysql.url'))
        drop_database(engine.url)
    except Exception as e:
        print('Unable to drop database: %s' % e)


if __name__ == '__main__':
    action = sys.argv[1]
    if action == ACTION_CREATE:
        create()
    elif action == ACTION_DROP:
        drop()
