'''Дан текст: в первой строке записано число строк, далее идут сами строки.
Определите, сколько различных слов содержится в этом тексте.
Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или
символами конца строки.
'''
heights = map(int, input().split())
petya = int(input())

for i, val in enumerate(heights):
    if val < petya:
        print(i + 1)
        break