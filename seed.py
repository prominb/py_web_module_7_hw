from time import sleep

from seeds.fill_grades import insert_grades
from seeds.fill_groups import insert_groups
from seeds.fill_students import insert_students
from seeds.fill_subjects import insert_subjects
from seeds.fill_teachers import insert_teachers


def main():
    print("Start")
    insert_teachers()
    sleep(3)
    insert_groups()
    sleep(3)
    insert_students()
    sleep(3)
    insert_subjects()
    sleep(3)
    insert_grades()
    print("Finish")


if __name__ == '__main__':
    main()
