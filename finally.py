
#finally:- it is another clause of exception handling 
#finally ka use exception ho ya na ho tab bhi use hota hai 
#ye finally k andar k statements ko execute karta hai chahe exception ho ya na ho:)

'''try:

   l=[1,2,3,4]
   i=int(input("Enter the index: "))
   print(l[i])
except:
   print("some error occured")
finally:
   print("I am already executed ")'''

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Zero se divide nahi ho sakta!")
finally:
    print("Ye code hamesha chalega, chahe exception aaye ya na aaye.")

print("Ye statement hamesha execute hogi, chahe exception aaye ya na aaye.")




