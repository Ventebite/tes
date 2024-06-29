'''Дана строка, в которой буква  h  встречается как минимум два раза.
Разверните последовательность символов, заключенную между первым и
последним появлением буквы  h , в противоположном порядке.
'''
import re

password = input()

if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$", password):
    print('Password is not valid')
else:
    print('Password is valid')