from singly_linked import *

class stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0
    def is_empty(self):
        return self.mylist==None
    def push(self,data):
        self.mylist.insert_at_start(data) 
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
          self.mylist.delete_first()
          self.item_count-=1
    def peek(self):
        if not self.is_empty():
         return self.mylist.start.item
    def size(self):
        return self.item_count

#driver code
s1=stack()
s1.push(10)        
s1.push(20)        
s1.push(30)        
s1.push(40)        
s1.push(50)
print("Top Element is ",s1.peek())
print("removing first element ",s1.pop())
print("size of the list",s1.size())
print()        
                    
        
        
