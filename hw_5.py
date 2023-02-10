# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# a = int(input('Введите число А: '))
# b = int(input('Введите число B: '))

# def degree(a,b):
#     if b > 0:
#         return a*degree(a,b-1)
#     return 1

# print(degree(a,b))

# # Задача 28: Напишите рекурсивную функцию sum(a, b),
# # возвращающую сумму двух целых неотрицательных чисел. Из
# # всех арифметических операций допускаются только +1 и -1.
# # Также нельзя использовать циклы.

# def total(a,b):
#     if b > 0:
#         return a+total(1, b-1)
#     return 1

# print(total(2,8))

# задача калькулятор необязательная.
# Решать только через рекурсию!. Пользоваться встроенными функциями 
# вычисления таких выражений нельзя, если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел. 
# Надо посчитать результат введенного выражения.
# Например,

# на входе
# 1+9/3*7-4
# на выходе
# 18


expr = input('Введите выражение:  ')

def calc(lst):# здесь применяется рекурсия
    if len(lst) == 1:
        return lst[len(lst)-1]
    else: 
        if lst[len(lst)-2] == '+':
            return calc(lst[:-2]) + lst[len(lst)-1] 
        if lst[len(lst)-2] == '-':
            return calc(lst[:-2]) - lst[len(lst)-1] 

def div(lst):
    while '/' in lst or '*' in lst:
        for elm in lst:
            if elm == '/':
                idx = lst.index('/')
                lst[idx-1] = lst[idx-1]/lst[idx+1]
                del lst[idx:idx+2]                
            if elm == '*':
                idx = lst.index('*')
                lst[idx-1] = lst[idx-1]*lst[idx+1]
                del lst[idx:idx+2]
                
    return lst
def parse(text):
    res = []
    digit = ''
    for elm in text:
        if elm.isdigit():
            digit+=elm
        else:
            res.append(float(digit))
            res.append(elm)
            digit = ''
    res.append(float(digit))
    return res

print(calc(div(parse(expr))))
print(eval(expr))# для проверки работы алгоритма