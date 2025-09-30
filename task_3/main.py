date = list(map(int, input("Введите дату через пробел (чило месяц)").split()))
month = date[1]
day = date[0]
if month < 1 or month > 12:
    print("Такого месяца не бывает")
else:    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 28
    if day < 1 or day > max_days:
        print("Такого дня в этом месяце нету")
    else: 
        if month in [12, 1, 2]:
            print("Зима")
        elif month in [3, 4, 5]:
            print("Весна")
        elif month in [6, 7, 8]:
            print("Лето")
        elif month in [9, 10, 11]:
            print("Осень")    
