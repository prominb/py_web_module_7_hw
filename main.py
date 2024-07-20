import my_select


def main():
    select_number = int(input("Ведіть номер запиту від 1 до 12: "))
    if select_number == 1:
        print(my_select.select_1())
    elif select_number == 2:
        print(my_select.select_2())
    elif select_number == 3:
        print(my_select.select_3())
    elif select_number == 4:
        print(my_select.select_4())
    elif select_number == 5:
        print(my_select.select_5())
    elif select_number == 6:
        print(my_select.select_6())
    elif select_number == 7:
        print(my_select.select_7())
    elif select_number == 8:
        print(my_select.select_8())
    elif select_number == 9:
        print(my_select.select_9())
    elif select_number == 10:
        print(my_select.select_10())
    elif select_number == 11:
        print(my_select.select_11())
    elif select_number == 12:
        print(my_select.select_12())


if __name__ == '__main__':
    main()
