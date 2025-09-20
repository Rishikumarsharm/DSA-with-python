class Node:
    def __init__(self,item=None,pri=None,next=None):
        self.item=item
        self.pri=pri
        self.next=next
class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count=0
    def push(self,data,pri):
        n=Node(data,pri)
        if not self.start or pri<self.start.pri:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.pri<=pri:
                temp=temp.next
            n.next=temp.next
            temp.next=n    
    def is_empty(self):  
        return self.start==None   
        
    def pop(self):
        if self.is_empty():
           raise IndexError("priority queue is empty")
        data=self.start.item  
        self.start=self.start.next 
        self.item_count-=1
        return data
   
    def size(self):
        return self.item_count

p=PriorityQueue()
p.push("Amit",5)    
p.push(20,2)    
p.push("rohit",3)    
p.push(40,1)    
p.push("govind",4)

while not p.is_empty():
    print(p.pop())

    
        
            
      
            