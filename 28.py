'''В генеалогическом древе у каждого человека, кроме родоначальника, есть
ровно один родитель.
В генеалогическом древе определите для двух элементов их наименьшего
общего предка (Lowest Common Ancestor). Наименьшим общим предком
элементов A и B является такой элемент C, что С является предком A, C
является предком B, при этом глубина C является наибольшей из возможных.
При этом элемент считается своим собственным предком.
Программа получает на вход число элементов в генеалогическом древе  N .
Далее следует  N−1  строка, задающие родителя для каждого элемента древа,
кроме родоначальника. Каждая строка имеет вид  имя_потомка имя_родителя .
Далее идет число запросов  K . В каждой из следующих  K  строк, содержатся
имена двух элементов дерева.
Для каждого запроса выведите наименьшего общего предка данных
элементов.
'''
n, k = list(map(int, input().split()))

balls = ["I"]*n

for i in range(k):
    l, r = list(map(int, input().split()))
    for j in range(l-1, r):
        balls[j] = '.'
    
print(''.join(balls))