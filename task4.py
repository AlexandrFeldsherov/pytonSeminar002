# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time

def RND():
    rnd=int(time.time_ns()/100%10)
    return rnd

def RandomNumberInt(a,x):

    randDelta=x-a
    count=0
    while randDelta>1:
        randDelta=randDelta/10
        count=count+1
    randArray=[]
    i=0
    while i<count:
        j=10000
        while j>0:
                j=j-1
                numberRandom=RND()
        randArray.append(numberRandom)
        i=i+1  
    rand = int(''.join(map(str, randArray)))
    rand=float(rand/(10**count))
    rand=int((x-a)*rand)
    return a+rand


i=int(input("Введите количество цифр для вывода :"))
a=int(input("Введите начало диапазона :"))
x=int(input("Введите конец диапазона :"))

while i>=0:
    i=i-1
    number=RandomNumberInt(a,x)
    print(number)

