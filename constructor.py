#Constructorsin python 

#constructors banane k liye ham __init__() use karte hai 
#jab jab ham koi new object banayege tab tab constructor call hoga 
#ek object k liye ek hi baar call hoga 
#Yeh self parameter current instance ko represent karta hai, jo ki method ko call kar raha hai.
# Yani, jab aap method call karte hain,
# toh self ke through wo method us instance ke data aur attributes ko access aur modify kar sakta hai.
#constructor do type k hote hai 
#1. default aur parameterized 

class person:
    def __init__(self,n,o): #ye parameterized hai aur agar isme sirf self hota toh ye default hota :)
        print("hello world!")
        self.name=n 
        self.occ=o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("Reeshu","Software developer")
b=person("baba","hr")    #aise hi mai jitne baar ek class k multiple object create karuga tab tab woh constructor call karega 
a.info()
b.info()


        
        