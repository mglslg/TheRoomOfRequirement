import db_manager


def save(info_raw):
    db = db_manager.get_db()
    cursor = db.cursor()
    cursor.execute("insert into info_raw(title) values('lalala')")
    db.commit()
    db.close()
