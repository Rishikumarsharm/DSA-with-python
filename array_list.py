from array import *
al=array('i',[23,4,5,6,78,5])
print(al)
array('i',[23,56,76])
for x in al:
    print(x,end=" ")
al.append(20)
print(al)
al.insert(2,100)
print(al)
print(al.index(4))
al.pop(2)
print(al)
al.extend([1,2,3])
print(al)


