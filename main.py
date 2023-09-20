try:
    n = int(input("Введіть число: "))
    if n == 1:
        print("Понеділок")

    if n == 2:
        print("Вівторок")

    if n == 3:
        print("Середа")

    if n == 4:
        print("Четверг")

    if n == 5:
        print("П'ятниця")

    if n == 6:
        print("Субота")

    if n == 7:
        print("Неділя")



except Exception as e:
    print(e)