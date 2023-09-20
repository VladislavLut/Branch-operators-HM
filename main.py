try:
    n = int(input('Введіть число: '))

    if n == 1:
        print('Січень')

    if n == 2:
        print('Лютий')

except Exception as e:
    print(e)