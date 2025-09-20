from singly_linked import *

class stack(SLL):
    def __init__(self):
        super().__init__() #in python the parent class needs to be called 
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
          self.delete_first()
          self.item_count-=1
        else:
            raise self.is_empty()
    def peek(self):
        if not self.is_empty():
          return  self.start.item
        else:
            raise self.is_empty()
    def size(self):
        return self.item_count

s2=stack()
s2.push(10)                
s2.push(20)                
s2.push(30)                
s2.push(40)                
s2.push(50)
print("Top element in stack",s2.peek())
print("remove the first element",s2.pop())
print("the element is now on the top ",s2.start.item)
print("remove the first element",s2.pop())
print(s2.size())
print("remove the first element",s2.pop())
print(s2.size())
print()                