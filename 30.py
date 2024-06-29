'''. Реализуйте функцию, которая принимает в качестве первого аргумента строку,
а затем любое количество аргументов и возвращает строку, являющуюся
объединением всех аргументов разделенных строкой из первого аргумента.
Метод строк join не применять.
'''
class Stack:
    def __init__(self) -> None:
        self.__stack = list()
        
    
    def push(self, value) -> None:
        self.__stack.append(value)
        
    
    def pop(self) -> None:
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()
        
    
    def __len__(self) -> int:
        return len(self.__stack)
    
    
    def __contains__(self, value) -> bool:
        return value in self.__stack
    
    
    def __iter__(self):
        return iter(self.__stack)
    
    
    def __str__(self) -> str:
        return ', '.join(list(map(str, self.__stack[::-1])))
    
    
    def stack(self) -> list:
        return self.__stack