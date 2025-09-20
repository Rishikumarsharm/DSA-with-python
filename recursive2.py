def recsum(n):
    if n==0:
        return 0
    else:
        return n+recsum(n-1)
print(recsum(5))  

def oddsum(n):
    if n==1:
        return 1
    
    return 2*n-1+oddsum(n-1)
print(oddsum(10))

def evensum(n):
    if n==1:
        return 2    
    return 2*n+evensum(n-1)
print(evensum(10))    
    
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))      
    
def sqr(n):
    if n==0 or n==1:
        return 1
    else:
        return n*n+sqr(n-1) 
print(sqr(5))      
        
    
    
    
    
    
    
    
    