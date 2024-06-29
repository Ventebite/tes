''' Определите среднее значение всех элементов последовательности,
завершающейся числом 0.
'''
n = int(input())
count_words = set()


for i in range(n):
    for word in input().split(' '):
        count_words.add(word)
        
if '' in count_words:
    count_words.remove('')
    
print(len(count_words), count_words, sep='\t')
