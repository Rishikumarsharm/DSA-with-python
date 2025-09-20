class Node:
    def __init__(self,next=None,item=None):
       self.next=next
       self.item=item
class Queue():
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.rear==None
    def enqeue(self,data):
        n=Node(data)    
        if self.is_empty():
             self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1    
    def dequeue(self):
       if self.is_empty():
          raise IndexError("Queue is empty") 
       elif self.front==self.rear:
           self.rear=None
           self.front=None
       else:
           self.front=self.front.next 
           self.item_count-=1              
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
q2=Queue()
q2.enqeue(12)            
q2.enqeue(22)            
q2.enqeue(32)            
q2.enqeue(42)            
q2.enqeue(52)
print("remove the element",q2.dequeue())
print("remove the element",q2.dequeue())
print("remove the element",q2.dequeue())
print("size of stack",q2.size())
print()            
                     
            