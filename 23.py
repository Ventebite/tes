'''Каждый из некоторого множества школьников некоторой школы знает
некоторое количество языков. Нужно определить сколько языков знают все
школьники, и сколько языков знает хотя бы один из школьников.
В первой строке задано количество школьников. Для каждого из школьников
сперва записано количество языков, которое он знает, а затем - названия
языков, по одному в строке.
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких
языков. Языки нужно выводить в лексикографическом порядке, по одному на
строке.
'''
def task(meth: str, *args: int) -> int | float:
    result = {
        "min": min(args),
        "max": max(args),
        "avg": sum(args) / len(args)
    }
    return result[meth.lower()]


print(task("avg", 1,2,3))