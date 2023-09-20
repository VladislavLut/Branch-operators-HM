try:
    x = int(input("Введіть перше число: "))
    y = int(input("Введіть друге число: "))

    if x == y:
        print("Числа рівні.")

except Exception as e:
    print(e)