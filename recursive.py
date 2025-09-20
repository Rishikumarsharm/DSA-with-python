def rec(n):
     if n>0:
        rec(n-1)
        print(n,end=' ')
rec(10)  

def numrev(n):
    if n>0:
        print(n,end='  ')
        numrev(n-1)
numrev(10)  

def printodd(n):
    if n>0:
        printodd(n-1)
        print(2*n-1,end=' ')
printodd(10)                  
        
def printeven(n):
    if n>0:
        printeven(n-1)
        print(2*n,end=' ')
printeven(10)  

def printoddrev(n):
    if n>0:
        print(2*n-1,end=' ')
        printodd(n-1)
printodd(10)                  
        
def printevenrev(n):
    if n>0:
        print(2*n,end=' ')
        printeven(n-1)
printeven(10)                  
     
    
    
    
      