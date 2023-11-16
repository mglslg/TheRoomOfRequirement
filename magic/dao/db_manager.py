import pymysql
import db_config


def get_db():
    db = pymysql.connect(**db_config.db_config)
    return db
