class Test:
    x=5 #class variable object
    @staticmethod
    def hello():
        print("i am lokesh kumar") 
        
t1=Test() 
print(t1.hello())
t2=Test()        
print(t2.hello())

class Test1:
    x=5
    def __init__(self,a,b): 
        self.a=a #instance object
        self.b=b
    def show(self):
        print(self.a,self.b)
    @staticmethod
    def f2():
        pass
    @classmethod
    def f3(cls):
        print(cls.x)      

t1=Test1(5,6) 
print(t1.a,t1.b)   

t2=Test1(3,5) 
print(t2.a,t2.b)  
t2.show()  #instance object method
t1.f3()

class employee:
    def __init__(self,name=None,empid=None,salary=None):
        self.empid=empid
        self.salary=salary
        self.name=name
    def setEmpid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name=name
    def setsalary(self,salary):
        self.salary=salary 
    def getEmpid(self):
        return self.empid
    def getEmpName(self):
        return self.name
    def getsalary(self):
        return self.salary

e1=employee(2,"jadu",30000)
e2=employee(1,"lokesh",40000)    
e1.setEmpid(2)
e1.setName("Lokesh")
e1.setsalary(40000)
print(e1.getEmpid(),e1.getEmpName(),e1.getsalary()) 
print(e2.getEmpid(),e2.getEmpName(),e2.getsalary()) 
            
        
                   