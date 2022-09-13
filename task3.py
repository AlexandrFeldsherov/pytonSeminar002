# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

from posixpath import split


def InputNumbers():
    index = True
    while index:
        try:
            number = int(input("Введите целое число : "))
            index = False
        except ValueError:
            print("Это не целое число.")
    return number


def ReversNumber(num):
    num = str(num)
    listNum = []
    for i in num:
        listNum.append(i)
    revListNum = listNum
    revListNum.reverse()
    return int(''.join(map(str, revListNum)))


def PalindromeSearch(num):
    palindrom = num+ReversNumber(num)
    if palindrom == ReversNumber(palindrom):
        return palindrom
    else:
        palindrom = PalindromeSearch(palindrom)
    return palindrom


number = InputNumbers()
revNum = ReversNumber(number)
if number == revNum:
    print(f"Введенное число {number} палиндром")
else:
    palindrom = PalindromeSearch(number)
    print(f"Палиндром введенного числа {number} -> {palindrom}")
