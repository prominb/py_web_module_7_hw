from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher


teachers = ("Шмигаль Денис Анатолійович",
            "Свириденко Юлія Анатоліївна",
            "Стефанішина Ольга Віталіївна",
            "Кубраков Олександр Миколайович",
            "Верещук Ірина Андріївна")

def drop_data():
    try:
        session.query(Teacher).delete()
        session.commit()
        print("Дані таблиці TEACHERS видалено!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()

def insert_teachers():
    try:
        for tcr in teachers:
            teacher = Teacher(fullname=tcr)
            session.add(teacher)
        session.commit()
        print("Вчителів успішно додано!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()

# def main():
#     # drop_data()
#     insert_teachers()

# if __name__ == '__main__':
#     main()
# def test_func():
#     print(teachers)
