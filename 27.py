'''В генеалогическом древе у каждого человека, кроме родоначальника, есть
ровно один родитель.
Даны два элемента в дереве. Определите, является ли один из них потомком
другого.
Программа получает на вход число элементов в генеалогическом древе  N .
Далее следует  N−1  строка, задающие родителя для каждого элемента древа,
кроме родоначальника. Каждая строка имеет вид  имя_потомка имя_родителя .
Далее идет число запросов  K . В каждой из следующих  K  строк, содержатся
имена двух элементов дерева.
Для каждого такого запроса выведите одно из трех чисел: 1, если первый
элемент является предком второго, 2, если второй является предком первого
или 0, если ни один из них не является предком другого.
'''
nums = list(map(int, input().split()))

result = list()

for i in range(len(nums)):
    if (nums[i] not in nums[:i]) and (nums[i] not in nums[i+1:]):
        result.append(nums[i])
        
    
print(result)