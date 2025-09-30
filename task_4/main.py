num = list(map(float, input("Введите 3 чила через пробел (чило месяц)").split()))
if num[0] < num[1] and num[0] < num[2]:
    print(f"Наименьшее число {num[0]}")
elif num[1] < num[0] and num[1] < num[2]:
    print(f"Наименьшее число {num[1]}")
    elif num[2] < num[1] and num[2] < num[0]:
print(f"Наименьшее число {num[2]}")
