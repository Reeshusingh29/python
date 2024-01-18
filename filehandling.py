#writing a file   writing a file mai ham write function k andar hi naya file generate kar sakte hai 

#f=open('myfile.txt','w')
#text = f.write('helloo')
#print(text)
#f.close()

#Reading a file 

#f=open('myfile.txt','w')
#f.write('Hello world!')
#f.close()

#appending a file

#f=open('myfile.txt','a')
#f.write('Hello world')
#f.close()

#with open('myfile.txt','a') as f:
#    f.write("hey guys welcome to the channel!")
'''
#readline mode:- ye method file ko line by line read karti hai 

f=open('myfile.txt','r')   
while True:
    line = f.readline()
   # print(line)
    if not line :   #if no more lines are there in the file then it will break
        print(line,type(line))
        break
    print(line)
'''
'''
#writeline method :- ye elk list k elements ko text mai dikhati hai 
writelines() method ka use ek sequence (jaise ki list) ko file mein likhne ke liye hota hai.
 Yeh method ek iterable ko  accept karta hai aur uske saare elements ko file mein likh deta hai.
    
lines_to_write = ['Line 1\n', 'Line 2\n', 'Line 3\n']

with open('newfile.txt', 'w') as new_file:
    new_file.writelines(lines_to_write)
'''
'''
#seek method:- ye ek number leta hai apne parameter mai aur phir uske aage k words jitna read ka limithai utna read karta hai 
with open('myfile.txt','r') as f:
    print(type(f))
    #move to the 7th byte in the file
    f.seek(10)

    #read the next 5 bytes
    data = f.read(5)
    print(data)
    

#tell() methid:- ye hame batata hai kio kaha tak hamne seek kiya hai 
with open('myfile.txt','r') as f:
    print(type(f))
    #move to the 7th byte in the file
    f.seek(10)
     
     #tell()
    print(f.tell())
    #read the next 5 bytes
    data = f.read(5)
    print(data)
'''
#truncate method
#agar mujhe tay karna hai ki meri file ki size kyaho toh truncate wahi karta hai 
#jaise niche hamne truncate mai 5 likha hai toh usse
#toh usne hello brother mai pehlw 5 liya hai aur hello print kiya hai 

with open('sample.txt','w') as f:
    f.write('Hello brother')
    f.truncate(5)

with open('sample.txt','r') as f:
    print(f.read())