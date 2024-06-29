'''Напишите программу для проверки корректности пароля введенного
пользователем. Пароль должен иметь следующие свойства:
Не менее 1 буквы из диапазона a-z и 1 из диапазона A-Z
Не менее одной цифры в диапазоне 0-9
Не менее одного символа из $#@
Длина не менее 6 и не более 16 символов'''
n = int(input())
rules = list()
miscs = int()

for i in range(n):
    rules.append(str(input()))
    
letter = str(input()).split()

for i in letter:
    if i.islower():
        miscs += 1
        continue
    
print(miscs)