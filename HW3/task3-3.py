# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[2] + my_list[1]


a = int(input("Первое число: "))
b = int(input("Второе число: "))
с = int(input("Третье число: "))

print(my_func(a, b, с))
