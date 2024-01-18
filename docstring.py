'''
Bilkul, bhai! Python me docstring ek special type ka comment hota hai jo function, module, 
ya class ke documentation ke liye use hota hai. Iska mtlb hota hai "documentation string".
 Docstring aksar triple quotes (""") ke bich me likha jata hai, jisme aap details me apne code ke bare me likh
   sakte hain.


Yeh ek example dekhein:
def greet(name):
    """
    This function greets the person passed in as a parameter.
    
    Parameters:
    name (str): The name of the person to be greeted.
    
    Returns:
    str: A greeting message.
    """
    greeting = f"Hello, {name}! How are you doing today?"
    return greet

greet("reeshu")

Is example me, greet function ke docstring me function ke parameters,
 unki types, aur return type ke bare me information di gayi hai. 
 Jab aap is function ka use karte hain, aap easily samajh sakte hain ki iska istemal kaise karna hai.

Docstring ka istemal aapke code ko maintain karne me aur dusre developers ko aapke code samajhne me madad karta hai.
 Aap docstring ko help function ke sath bhi use karke dekh sakte hain:

 help(greet)

 Isse aapko function ke docstring ka summary mil jayega.

Docstring likhne se aapka code professional aur user-friendly ban jata hai.
 Aur aapki team ke members ko bhi aasani se samajhne me madad milti hai.





'''

def add(a,b):
    """
    ye ek docstring hai bhai 
    """
    print(a+b)


#anss = 
add(2,4)
#print(anss)
print(add.__doc__)
 #do tarike k docstring type nikalne hote hai 
#help function se function k saath saath comments print hota hai 
# print(add.__doc__) isse bas function k andar k comments print hote hai 
