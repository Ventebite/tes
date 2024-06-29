'''Реализуйте функцию, которая принимает в качестве первого аргумента строку,
а затем любое количество именованных аргументов. Именованные аргументы
представляют собой множества. Принадлежность элемента к конкретному
множеству определяется по первому символу имени аргумента. Найти
объединение, пересечение или симметрическую разность полученных
множеств.
'''
class Queue:
    def __init__(self) -> None:
        self.__queue = list()
        
        
    def push(self, value) -> None:
        self.__queue.append(value)
        
    
    def pop(self) -> int | None:
        if len(self.__queue) == 0:
            return None
        return self.__queue.pop(self.__queue[0])
        
        
    def __len__(self) -> int:
        return len(self.__queue)
    
    
    def __contains__(self, value) -> bool:
        return value in self.__queue
    
    
    def __iter__(self):
        return iter(self.__queue)
    
    
    def __str__(self) -> str:
        return ', '.join(list(map(str, self.__queue)))
    
    
    def queue(self) -> list:
        return self.__queue