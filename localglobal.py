def document():
    '''
    Haan, bilkul sahi. Jo bhi variables kisi function ke andar define hote hain,
    unhe hum local variables kehte hain. Local variables ka scope sirf us function tak hi hota hai,
    aur function ke bahar inhe access nahi kiya ja sakta. Yani ki, agar aap kisi function ke bahar
     kisi local variable ko access karne ki koshish karenge, toh error milega. Iske alawa, ek function ke andar define kiye gaye
    local variables doosre functions mein bhi access nahi kiye ja sakte hain.

  toh phir ham usko kaise access kar sakte hai function k bahar???
Local variable ko function ke bahar access karne ke liye aapko ek technique ka use karna padta
 hai.Aapko function ke andar return keyword ka use karke variable ko function se bahar 
 laana hoga.Yeh returned value ko aap kisi variable mein store karke access kar sakte hain.

 def get_local_variable():
        local_variable = 50
    return local_variable  # Local variable ko function se bahar laane ke liye return keyword ka use

result = get_local_variable()
print(result)  # Yeh line chalegi, aur 'local_variable' ki value 50 hogi

global variable mai kya idea hai ???

-->Global variable woh variables hote hain jo program ke bhar, 
yani ki kisi function ke bahar define hote hain. 
Inhe aap program ke kisi bhi hisse se access kar sakte hain. 
Global variables ka scope program ke poore area mein hota hai.

global_variable = 100  # 'global_variable' ek global variable hai

def print_global_variable():
    print(global_variable)

print_global_variable()  # Yeh line chalegi, aur 'global_variable' ki value 100 hogi
print(global_variable)  # Yeh line bhi chalegi, kyunki 'global_variable' global scope mein hai

Isme, global_variable ek global variable hai jo program ke bahut se hisson se access kiya ja
 sakta hai. Jab bhi aap global variable ko modify karte hain, 
toh us modification ka asar program ke poore area mein hota hai.

global_variable = 100  # 'global_variable' ki initial value set ki gayi hai

def modify_global_variable():
    global global_variable  # 'global' keyword ka use karke global variable ko modify kiya ja sakta hai
    global_variable = 200

modify_global_variable()
print(global_variable)  # Yeh line chalegi, aur 'global_variable' ki value 200 hogi

Isme, modify_global_variable function mein global_variable ko 200 set kiya gaya hai, aur iski value ab program ke kisi bhi hisse se access ki ja sakti hai.

Global variables ka use kisi value ko program ke poore area mein share karne ke liye hota hai, 
jisse ki multiple functions ya modules un values ko access aur modify kar sakein.
    '''

print(document.__doc__)