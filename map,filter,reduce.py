

'''
def cube(x):
    return x**3

print(cube(3))

l=[1,2,3,4,5,6]
newl=list(map(cube,l))   #map k andar function ka naam aur uss list ka naam jisme aap apni woh function apply karna chahte ho 
print(newl)


#FILTER :- FILTER chaatne ka kaam karta haii 
def filter_function(a):  
    return a>4                 #ye ab 4 se bada jo bhi hai usko filter karega 

newnewl=list(filter(filter_function,l))   #is filter mai yefunction true aur false return karega aur woh compare karega uske baaju mai jo list hai usse
print(newnewl)
'''

#reduce : reduce ko sabse pehle import karna hota hai directapply nahi kar sakte 
from functools import reduce

#list of numbers
numbers = [1,2,4,5,3]
#numbers=[3,3,4,5]

#calculate the cum of the numbers using the reduce function

sum = reduce(lambda x,y:x+y,numbers)

#print the sum
print(sum)

