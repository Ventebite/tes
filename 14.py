'''. Петя перешёл в другую школу. На уроке физкультуры ему понадобилось
определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность
натуральных чисел, означающих рост каждого человека в строю. После этого
вводится число X – рост Пети. Все числа во входных данных натуральные и
не превышают 200.
Выведите номер, под которым Петя должен встать в строй. Если в строю есть
люди с одинаковым ростом, таким же, как у Пети, то он должен встать после
них.
'''
nums = map(int, input().split(','))

for i in nums:
    if int(str(i), 2)%5 == 0:
        print(i)