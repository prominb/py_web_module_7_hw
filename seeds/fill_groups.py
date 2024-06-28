from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Group


groups = ("КІТ-122А", "КІТ-123Б", "КІТ-125А")

def drop_data():
    try:
        session.query(Group).delete()
        session.commit()
        print("Дані таблиці GROUPS видалено!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()

def insert_groups():
    try:
        for grp in groups:
            group = Group(name=grp)
            session.add(group)
        session.commit()
        print("Групи успішно додано!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()

def main():
    # drop_data()
    insert_groups()

if __name__ == '__main__':
    main()
