'''Напишите программу, которая принимает разделенную запятыми
последовательность четырехзначных бинарных чисел и выводит через
запятую числа кратные 5'''
n = int(input())
customers = dict()

for i in range(n):
    name, item, count = input().split()
    if name not in customers:
        customers[name] = {item: int(count)}
    elif item not in customers[name]:
        customers[name][item] = int(count)
    else:
        customers[name][item] += int(count)
        
print(customers)
