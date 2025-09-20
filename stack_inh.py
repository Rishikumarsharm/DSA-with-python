class stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            return IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            return IndexError("stack is empty")   
    def size(self):
        return len(self)
    def insert(self,item,data):
         raise AttributeError("not Attribute 'insert' in stack ")
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s)
print("the top element is ",s.peek())
print("the removed element is ",s.pop())
print()
print(s)
print("the removed element is ",s.pop())
print(s.size())             
print(s)                
        
    