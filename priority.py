class priorityQueue:
    def __init__(self):
        self.items=[]
        self.item_count=0
        
    def is_empty(self):
        return len(self.items)==0    
            
    def push(self,data,pri):
        index=0
        while index<len(self.items) and self.items[index][1]<=pri:
            index+=1
        self.items.insert(index,(data,pri))
    
    def pop(self):
        if self.is_empty():
            raise IndexError("priorityQueue is Empty")
        self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)  
        
    def size(self):
        return self.item_count    
            
p=priorityQueue()
p.push("Lokesh ",3)
p.push("Aditya ",2)      
p.push("Vishal",4)
p.push("anurag",5)
p.push("kirti",1)
print(p.items)
p.pop()
print(p.size()) 
print(p.items)               
    