try:
    n = int(input("Введіть число: "))

    if n > 0:
        print("Number is positive")

    elif n < 0:
        print("Number is negative")

    elif n == 0:
        print("Number is equal to zero")

    else:
        print("Невірне число")

except Exception as e:
    print(e)