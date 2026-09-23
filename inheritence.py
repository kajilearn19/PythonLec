class Dad :
    def __init__ (self,name):
        self.name = name

    def getName(self):
        return self.name
        
    def sayHello(self):
        return "Hi from dad"

class Mom :
    def __init__(self,age):
        self.age=age

    def getAge(self):
        return self.age

    def sayHello(self):
        return "Hi from mom"
        
class Child (Dad,Mom):
    
    def __init__ (self,name,age):
        super().__init__(name)
        super().__init__(age)
        
    def sayHi(self):
        return "HI"

Jhon = Dad("Jhon")
print(Jhon.getName())
mom = Mom(25)
print(mom.getAge())
jhon = Child("Jhon",25)
abi = Child(30,"abi")
mathu = Child("Mathu",25)
print(jhon.sayHello())
print(abi.sayHello())
print(abi.getName())
print(abi.sayHi())




