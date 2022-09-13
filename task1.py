# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

def InputNumbers():
    index = True
    while index:
        try:
            number = float(input("Введите вещественное число : "))
            index = False
        except ValueError:
            print("Это не вещественное число.")
    return number


def SumNumbers(num):
    sumNumber = 0
    num = str(num)
    for i in num:
        if i != '.' and i != '-':
            sumNumber = sumNumber + int(i)
    return sumNumber


number = InputNumbers()
print(f"{number} -> {SumNumbers(number)}")
