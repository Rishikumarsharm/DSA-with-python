class Deque:
    def __init__(self):
        self.item=[]

                
    def is_empty(self):
      return len(self.item)==0
        
    def insert_front(self,data):
        self.item.insert(0,data)
    def insert_rear(self,data):
        self.item.append(data)
    
    def delete_front(self):
        if not self.is_empty():
            self.item.pop(0)
            return self.item
        else:
            raise IndexError("Deque is empty") 
    def delete_rear(self):
        if not self.is_empty():
            self.item.pop()
            return self.item
        else:
            raise IndexError("Deque is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("Deque is empty")    
        
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Deque is empty")
        
    def size(self):
        return len(self.item)
    
d=Deque()
d.insert_rear(23)                         
d.insert_front(23)
d.insert_rear(34)
d.insert_front(12)
d.insert_rear(12)
print(d.item)  
d.delete_front()
d.delete_rear()
print(d.item)    
print(d.size())
print(d.get_front())                   
print(d.get_rear())                   

    
                
                