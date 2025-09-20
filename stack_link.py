class Node:
    def __init__(self,next=None,item=None):
                  self.next=next
                  self.item=item

class stack:
    def __init__(self):
        self.top=None
        self.item_count=0
    def is_empty(self):
        return self.top==None 
    def push(self,data):
           n=Node(data,self.top)
           self.top=n
           self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.top.item
            self.top=self.top.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.top.item
            
        else:
            raise self.is_empty()   
    def size(self):
        return self.item_count
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print("top element is",s.peek())
print()
print("top element is",s.peek())
print("size of the stack",s.size())
print("the removed element is",s.pop())
print()

       
        
        
           

           
                                  