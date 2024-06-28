from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Subject


subjects = (
    ("Системи штучного інтелекту", 1),
    ("Сучасне програмування, мобільні пристрої та комп’ютерні ігри", 1),
    ("Прикладна комп’ютерна інженерія", 2),
    ("Кібербезпека", 3),
    ("Автоматизація та комп’ютерно-інтегровані технології", 4),
    ("Метрологія та інформаційно-вимірювальна техніка", 5),
)

def drop_data():
    try:
        session.query(Subject).delete()
        session.commit()
        print("Дані таблиці SUBJECTS видалено!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()

def insert_subjects():
    try:
        for sbj in subjects:
            subject = Subject(name=sbj[0], teacher_id=sbj[1])
            session.add(subject)
        session.commit()
        print("Предмети успішно додано!")
    except SQLAlchemyError as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()

def main():
    # drop_data()
    insert_subjects()

if __name__ == '__main__':
    main()
