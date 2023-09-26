'''
#operators
print("Arithmatic operators :")
print("3+1 i.e",3+1)
print("3-1 i.e",3-1)
print("3%1 i.e",3%1)
print("3*1 i.e",3*1)
print("3/1 i.e",3/1)

print("Assignment operators : ")
a=34
a-=12
a+=12
a/=12
a*=12
print(a)

print("comparison operator :")
c=(14<=7)
print(c)


#typeconversion or typecasting
a="21"
a=float(a)
print(type(a))
print(a+5)

#input function
#a=input("Enter your name : ")
#a=int(a)  #convert a to integer
#print(type(a))

#STRINGS
b="Reeshu"
print(type(b))
greeting="Good morning, "
print(greeting+b)

name="harrybhai"
print(name[1:4]) #isme 0,1,2 hi milega 3 wala nahi milega
print(name[1::3])

story="mera naam reeshu hai "
#string functions
print(len(story))
print(story.endswith("hai "))
print(story.count("r"))
print(story.capitalize())
print(story.find("reeshu"))
print(story.replace("reeshu","babu"))

#escape sequence character
story="jai shree ram"
print(story)


#LIST 
#creating a list using []
a=[1,2,3,42,2]
#print the list using print()
print(a[4])

#access using index using a[0],a[1],a[2]
print(a[4])

#change the value of list using 
a[0]=69
print(a)

#we can create a list with items of different types
c=[45,"harry",False,6.9]
print(c)

#list slicing
friends=["reeshu","babu","baba","nappu"]
print(friends[0:4])
print(friends[-1])

#list methods
l1=[1,4,2,44,23]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(99)
print(l1)
l1.insert(0,444)
print(l1)
l1.pop(0)
print(l1)
l1.remove(23)
print(l1)


#tuples
#creating a tuple using ()
t=(1,2,3,4,5)
#t1=() #empty tuple
#t1=(1) #wrong way to declare a tuple with single element
t1=(1,) #tuple with single element
print(t1)


#we cannot update tuple values
#t[0]=88
#print(t)

#tuple methods
print(t.count(1))
print(t.index(1))


#dictionary :- collection of key value pairs
a={
    "fast":"in a quick manner",
    "harry":"a coder",
    "marks":[1,2,3,4]
}
a['fast']="babu"  #ye mutable hai 
print(a['fast'])

#dictionary metods
print(a.keys())
print(list(a.keys()))
print(a.values())
b={
    "baba":"boss"
}
a.update(b)
print(a)

#sets
a={1,2,3,4}
print(type(a)) 
#important : this syntax will create an empty dictionary
a={}
print(type(a))

#ab empty set can be created using the below syntax:
b=set()
print(type(b))

b.add(3)
b.add(2)
print(b)
b.add((2,11,33,2))
print(b)

#set methods
print(len(b))
b.remove(3)
print(b)


#conditional expressions

a=2
if(a>3):
    print("The value of a is greater than 3")
elif(a>7):
    print("sahi hai bhai")
else:
    print("ek no bhau kadakkkkk")

print("done bhai ")

age =int(input("enter your age "))
if(age>18):
    print("abhi tu maje kar sakte hai" )
else:
    print("ja homeweork kar bsdk")

a=[45,33,2]
print(45 in a)


#loops in python


#while loop
i=0
while i<10:
    print("yes" +str(i))
    i=i+1

print("done")

i=1
while i<=50:
    print(i)
    i=i+1;


fruits=['banana','kela','mango','aam']
i=1
while i<len(fruits):
    print(fruits[i])
    i=i+1

#for loop

fruit=['banana','kela','mango','aam']

for item in fruit:
    print(fruit)

for i in range(8):
    print(i)
print("done")

for i in range(1,8,1):   #isme 0 se nahi 1 se chalu hoga aur last mai jo 8th hai usko hatake 7 tak jaaytega 
    
    print(i)

print("bas kar bhai")

for i in range(10):
    print(i)
else:
    print("this is inside of else")

#break statement
for i in range(10):
    print(i)
    if i==5:
        break
#else
    else:
        print("this is inside else of for")


#continue statement

for i in range(10):
    if i==5:
        continue
    print(i)

#pass statement
i=4
if i>0:
    pass   #pass ek null statement hai woh kuch nahi bhejta hai


#functions in python

def percent(marks):
    p= ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[45,78,86,77]  
percentage1=percent(marks1)


marks2=[75,98,88,78]
percentage2=percent(marks2)
print(percentage1,percentage2)


def greet(name="babu"):
    print("good day "+ name)
def mysum(num1,num2):
    p=num1+num2
    return p

greet("reeshu")
s=mysum(12,99)
print(s)
greet()

#recursion

#factorial program
#n1=1*2*3....*n


def factorial(n):
    for i in range(n):
        if n==0 or n==1:
            return n
        return n*factorial(n-1)

f=factorial(1)
print(f)

'''

#file i/o
#use open function to read the contents of the file
#f=open('sample.txt','r')
f=open('sample.txt') #by default wohread mode mai hota hai tpoh zarurat nahi hai 'r' likhne ki :)
data=f.readline()  
print(data)







