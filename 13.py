'''Дана строка. Замените в этой строке все появления буквы  h  на букву  H ,
кроме первого и последнего вхождения.
'''
a,b = map(int, input().split())
nums = list()
for i in range(a,b+1):
    if i % 2 == 0:
        nums.append(i)
        
print(', '.join(list(map(str, nums))))