numbers = list(map(float, input("Введите два числа через пробел: ").split()))
if numbers[0] < numbers[1]:
    print(f"Наименьшее число: {numbers[0]}")
else:
    print(f"Наименьшее число: {numbers[1]}")
