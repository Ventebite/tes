'''Дана строка. Замените в этой строке все цифры  1  на слово  one .'''
def check_sqr(x: int, y: int, z: int) -> str:
    if (x==y==z):
        print("equilateral")
    elif (x==y) or (y==z) or (x==z):
        print("isosceles")
    else:
        print("scalene")
    
check_sqr(3,4,5)