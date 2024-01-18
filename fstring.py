#fstring: ye use hota hai string ko formatting karne k liye 
#letter =  "hey my name is {1} and i am from {0}"

country = 'India'
name = 'Akash'

#print(letter.format(country,name))
print(f'hey my name is {name} and i am from {country}')


a = int(input("Enter the number: "))

print(f"{a} ka pahada hai ye:  ")

for i in range(1,11):
    print(f"{a} X {i} = {(a*i)}")