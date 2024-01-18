a = (input("Enter the number: "))

#print(f"{a} ka pahada hai ye:  ")
try:
    for i in range(1,11):
     print(f"{int(a)} X {i} = {int(a*i)}")
except Exception as e:
    print("bhai input toph sahi se de bhai ")


print("ye part toh run hoga chahe error aaye ya na aaye ")

try:
    # Yahaan par koi code hota hai jo hum chahte hain ki sahi se chale
    result = 10 / 0  # Divide by zero exception hoga yahan
except ZeroDivisionError:
    # Agar exception hoti hai (yahan par ZeroDivisionError), to ye block chalega
    print("Zero se divide nahi kar sakte!")
else:
    # Agar koi exception nahi hoti, to ye block chalega
    print("Division successful. Result:", result)



try:
    # Yahaan par koi code hota hai jo hum chahte hain ki sahi se chale
    numbers = [1, 2, 3]
    print(numbers[4])  # List index out of range exception hoga yahan
except IndexError:
    # Agar exception hoti hai (yahan par IndexError), to ye block chalega
    print("List index out of range!")
else:
    # Agar koi exception nahi hoti, to ye block chalega
    print("Access successful.")
