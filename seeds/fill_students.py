from sqlalchemy.exc import SQLAlchemyError
from faker import Faker

from conf.db import session
from conf.models import Student


fake = Faker('uk-UA')

def drop_data():  # ВИнести окремо, 5 раз одне і теж написано
    try:
        session.query(Student).delete()
        session.commit()
        print("Дані таблиці STUDENTS видалено!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()

def insert_students():
    try:
        for i in range(1, 4):  # ЦЕ неправильно, треба ID витягнути з БД
            for _ in range (15): 
                student = Student(
                    fullname = fake.name(),
                    group_id = i
                )
                session.add(student)
        session.commit()
        print("Студентів успішно додано!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()


def main():
    # drop_data()
    insert_students()


if __name__ == '__main__':
    main()
