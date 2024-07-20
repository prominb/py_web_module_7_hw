from sqlalchemy import func, desc, select, and_

from conf.db import session
from conf.models import Teacher, Group, Student, Subject, Grade


def select_1():  # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result

def select_2():  # Знайти студента із найвищим середнім балом з певного предмета.
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject).filter(Subject.name == 'Прикладна комп’ютерна інженерія')\
        .group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()
    return result

def select_3():  # Знайти середній бал у групах з певного предмета.
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject).join(Group)\
        .filter(Subject.name == 'Сучасне програмування, мобільні пристрої та комп’ютерні ігри')\
        .group_by(Group.id).all()
    return result

def select_4():  # Знайти середній бал на потоці (по всій таблиці оцінок).
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).scalar()
    return result

def select_5():  # Знайти які курси читає певний викладач.
    result = session.execute(
        select(Subject.name).
        join(Teacher).
        where(
            Teacher.fullname.like("Шмиг%")
        )
    ).scalars().all()
    return result

def select_6():  # Знайти список студентів у певній групі.
    result = session.query(Student.fullname).\
        select_from(Student).\
        join(Group).\
        filter(Group.name == "КІТ-123Б").\
        all()
    return result

def select_7():  # Знайти оцінки студентів у окремій групі з певного предмета.
    result = session.query(Student.fullname, Grade.grade).\
        select_from(Grade).\
        join(Student).\
        join(Subject).\
        join(Group).\
        filter(Group.name == 'КІТ-125А').\
        filter(Subject.name == 'Автоматизація та комп’ютерно-інтегровані технології').all()
    return result

def select_8():  # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    result = session.query(Teacher.fullname, Subject.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')).\
        select_from(Teacher).\
        join(Subject).\
        join(Grade).\
        filter(Teacher.fullname.like("Шмигаль%")).\
        group_by(Subject.id, Teacher.id).\
        all()
    return result

def select_9():  # Знайти список курсів, які відвідує певний студент.
    result = session.query(Student.fullname, Subject.name).\
        select_from(Student).\
        join(Grade).\
        join(Subject).\
        filter(Student.fullname.like("%Дарина Кабалюк%")).\
        distinct().all()
    return result

def select_10():  # Список курсів, які певному студенту читає певний викладач.
    result = (
        session.query(Subject.name)
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Teacher)
        .filter(Student.fullname == 'Яків Мазепа')
        .filter(Teacher.fullname == 'Свириденко Юлія Анатоліївна')
        .distinct().all()
    )
    return result

def select_11():  # Середній бал, який певний викладач ставить певному студентові.
    result = (
        session.query(Subject.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Teacher)
        .filter(Student.fullname == 'Яків Мазепа')
        .filter(Teacher.fullname == 'Шмигаль Денис Анатолійович')
        .group_by(Subject.id)
        .all()
    )
    return result

def select_12():  # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    subquery = (
        session.query(func.max(Grade.grade_date))
        .select_from(Grade)
    ).scalar_subquery()

    result = (
        session.query(Student.fullname, Group.name, Subject.name, Grade.grade_date, Grade.grade)
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Group)
        .filter(
            and_(
                Group.id == 3,
                Subject.id == 6,
                Grade.grade_date == subquery,
            )
        )
        .order_by(Student.fullname).all()
    )
    return result

def main():
    print(select_12())

if __name__ == '__main__':
    main()
