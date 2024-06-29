'''Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности.
'''
n, m = map(int, input().split())

set_1 = set()
set_2 = set()

for i in range(n+m):
    if i < n:
        set_1.add(input())
    else:
        set_2.add(input())
    
   
all_ = set_1 & set_2
only_first = set_1 - set_2
only_second = set_2 - set_1

print(len(all_), ' '.join(sorted(all_)), sep="\n")
# Дописать сортировку
print(len(only_first), ' '.join(sorted(only_first)), sep="\n")

print(len(only_second), ' '.join(sorted(only_second)), sep="\n")