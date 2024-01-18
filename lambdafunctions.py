#lambda function:-  ye ek function k argumentko leta hai aur isse code thoda kam likhna hota hai 
#itis a small anonymous function without a name 
#Syntax
#lambda arguments : expression
#anonymous matlab unknown person
square=lambda x:x**2
result=square(5)
print(result)

sum=lambda x,y:x+y/3
print(sum(2,3))

areaofcircle=lambda pi,r:pi*(r**2)
print(areaofcircle(3.142,2))

def appl(fx,value):
    return 6+fx(value) #ye fx yaha par first class function hai , first class function ko ham kisi function k argument mai daal sakte hai jaise hamne fx ko daala 

print(appl(lambda x:x*x,2))
    