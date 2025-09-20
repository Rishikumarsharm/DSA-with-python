class queue:
    def __init__(self):
        self.item=[]
        self.front=0
        self.rear=0
        self.item_count=0
    def is_empty(self):
        return len(self.item)==None
    def enqueue(self,data):
        self.item.append(data)
        self.rear+=1 
        self.item_count+=1        
    def dequeue(self):
        if not self.is_empty():
         self.item.pop(0)
         self.front+=1
         self.item_count-=1
         return self.item
    def get_front(self):
        return self.front
    def get_rear(self):
        return self.rear
    def size(self):
        return self.item_count
 
q=queue()
q.enqueue(10)    
q.enqueue(20)    
q.enqueue(30)    
q.enqueue(40)    
q.enqueue(50)
print(q.item)
print("remove the rear element",(q.dequeue()))
print("remove the rear element",(q.dequeue()))
print("remove the rear element",(q.dequeue()))
print("the position of rear is",q.get_rear())
print("the position of front is",q.get_front())
print("size of the list is",q.size())
print()
    
            
    