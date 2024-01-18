#Classes and objects 

#class is a blueprint to creating an objects 
#objects is an instance of a class 

'''
class person:
    name="reeshu"
    occupation="software developer"
    networth=10

a = person()

print(a.name)
'''

#self : self ka matlab woh object jiske liye ye method call kiya ja raha hai  jaise niche diya hai a.info() 


class person:
    name="reeshu"
    occupation="software developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation} and his networth is {self.networth}")

a = person()
a.info()

