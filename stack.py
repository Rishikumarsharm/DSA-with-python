class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return  len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return  self.items.pop()    
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1] 
        else:
            raise IndexError("stack is empty")   
    def size(self):
        return len(self.items)   

s=stack()
s.push(45)
s.push(40)
s.push(5)
s.push(41)
print(s.items)
print("Top Element is:",s.peek())
print("Removed element:",s.pop())
print("top element is",s.peek())
print()
print(s.items)




       