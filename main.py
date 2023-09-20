try:
    x = int(input("Введіть перше число: "))
    y = int(input("Введіть друге число: "))

    if x == y:
        print("Числа рівні.")

    elif x < y:
        print("Перше число: ", x, "Друге число: ", y)

    else:
        print("Перше число: ", y, "Друге число: ", x)

except Exception as e:
    print(e)