def gyaan():
    '''
    Virtual environment ka use Python projects ke liye environment isolate karne aur dependencies management ke liye hota hai. Yeh aapko project-specific libraries aur dependencies ko alag rakhne mein madad karta hai, jisse ek project ke dependencies dusre projects ko affect na karein.

Virtual environment banane se pehle, aapke system-wide Python installation ko use karte hain. Lekin jab aap ek virtual environment create karte hain, toh ek alag Python interpreter aur ek isolated environment create hota hai jisme aap apne project ke specific dependencies ko install kar sakte hain.

Yahan ek simple example hai:

System-wide Python Installation:

Suppose aapke system mein global Python version 3.8 installed hai.
Virtual Environment Create Karein:

Aapne ek project directory mein gaye.
python -m venv myenv command se ek virtual environment create kiya.
Isne ek myenv naam ka folder create kiya jisme alag Python interpreter aur environment files hain.
Virtual Environment Activate Karein:

Aapne myenv ko activate kiya.
Ab aapka command prompt ya terminal myenv mein chala gaya, jise indicate karta hai ki aap ab is virtual environment mein hain.
Packages Install Karein:

Jab aap virtual environment mein hain, aap pip install package_name se project-specific packages install kar sakte hain.
Ye packages sirf is virtual environment mein hi hote hain.
Virtual Environment Deactivate Karein:

Jab aap apne project se bahar nikalna chahte hain, aap deactivate command ka istemal karte hain.
Ab aap system-wide Python installation mein wapas laut jaate hain.
Is tareeke se, aap alag-alag projects ke liye alag-alag virtual environments bana sakte hain aur inmein apne dependencies ko manage kar sakte hain, jisse ek project dusre project ko affect na kare.
    '''

print(gyaan.__doc__)

