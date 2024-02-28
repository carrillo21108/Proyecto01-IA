from abc import ABC, abstractmethod
import heapq

# Definir la interfaz
class QueueInterface(ABC):
    @abstractmethod
    def empty(self):
        pass
    
    @abstractmethod
    def first(self):
        pass
    
    @abstractmethod
    def remove_first(self):
        pass
    
    @abstractmethod
    def insert(self,item):
        pass

# Clase Padre que implementa la interfaz
class Queue(QueueInterface):
    def __init__(self):
       self.content = []         

    def empty(self):
        return len(self.content)==0
        
    def first(self):
        if not self.empty():
            return self.content[0]
        
    def remove_first(self):
        item = self.first()
        if item:
            self.content.pop(0)
            return item
        
    def insert(self,item):
        pass
        
#Clase Hija FIFO
class Fifo(Queue):
    def insert(self,item):
        self.content.append(item)
        return self.content
    

#Clase Hija LIFO
class Lifo(Queue):
    def insert(self,item):
        self.content.insert(0,item)
        return self.content
    
#Clase Hija PriorityQueue
class PriorityQueue(Queue):
    def insert(self,item,priority):
        heapq.heappush(self.content,(priority,item))
        return self.content
    
    def remove_first(self):
        item = self.first()
        if item:
            heapq.heappop(self.content)
            return item