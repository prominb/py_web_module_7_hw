from random import randint

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Grade


fake = Faker('uk-UA')
grades = 5
students = 45
subjects = 6

def drop_data():
    try:
        session.query(Grade).delete()
        session.commit()
        print("Дані таблиці GRADES видалено!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()

def insert_grades():
    try:
        for student_id in range(1, students + 1):
            for subject_id in range(1, subjects + 1):
                for _ in range(4):
                    grade = Grade(
                        grade = randint(0, 100),
                        grade_date = fake.date_between(start_date='-3y', end_date='today'),  # Хай буде за 3 роки
                        student_id = student_id,
                        subject_id = subject_id
                    )
                    session.add(grade)
        session.commit()
        print("Оцінки успішно додано!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()
