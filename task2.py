# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def InputNumbers():
    index = True
    while index:
        try:
            number = int(input("Введите целое число : "))
            index = False
        except ValueError:
            print("Это не целое число.")
    return number


def Factorial(number):
    if number > 1:
        number = number*Factorial(number-1)
    return number


def SetOfWorks(number):
    if number < 1:
        print(f"N = {number}, тогда набор произведений чисел от 1 до N не существует")
    else:
        setOfWorks = []
        i = 1
        while i<=number:
            setOfWorks.append(Factorial(i))
            i=i+1
        return setOfWorks


number = InputNumbers()
print(f"{number} -> {SetOfWorks(number)}")
