####sample scrypt to encrypt and decrypt
import os
import sys
#ask for user input
print(" This is a small program to Encrypt and Decrypt text files")
print("\n")
print("* Please note that at this point, this program works only for .txt files*")
print("\n")
print("**In order to Decrypt a file, it has to encrypted using this program**")
print("\n")
print("LETS GET STARTED !!!\n")
print("\n")
#master reference list 
master={'A':'Jkbj','B': 'kbsi', 'C':'hnwf','D':'j’ix','E':'zfcx','F':'zasx','G':'degt','H':'u6ku','I':',j,a','J':'rfgu','K':'iln/','L':'jklj','M':'io89','N':'7y6g','O':'uj/;','P':'Kagg','Q':'yUJJ','R':'YI8I','S':'hyui','T':'uuKU','U':'Uujh','V':'yg^y','W':'tffd','X':'dgy&','Y':'8okk','Z':'&*nj',"a":"gtfd","b":"$32g", "c":"fgsd", "d":"8&89","e":"cfjl","f":"0h^g","g":"dh#7","h":")J(5","i":"hadj"," ":"uhty","j":"nb6d","k":"!8f#","l":"4jaj","m":"tg4p","n":"&6gh","o":"^98$","p":"bt98","q":"b438","r":"89h6","s":"oijh","t":"87#t","u":"NIHT","v":"&15b","w":"Stg^","x":"87H6","y":"gdfh","z":"8&%^","0":"ikgt","1":"fgty","2":"ThGt","3":"&^hj","4":"POlk","5":"mnjh","6":"^&%j","7":"mijh","8":"789j","9":"yh{o","!":"kjnb","@":"trFb","#":"nilo","$":"Pl*&","%":"5875","^":"kjhy","&":"tr46","*":"yt0&","(":"JH>k",")":"mnh7",":":"freh",";":"bhyt","'":"plki",'"':"7hgt","/":"Ft5r","?":"po8s",",":"7*9^",".":"yh4&","[":"io76","]":"$2#5"}
Options=input("Choose an Option:\n1. Encrypt a file    2. Decrypt a file\n")
print("\n")
File=input("Enter the path to your text file that you want to encrypt/decrypt - please use / backslash when typing in directory path: \nFor Example: C:/Users/antho/Desktop/file_to_encrypt.txt\n")
print("\n")
z=str(File)
u=open(z,"r")
p1=str(u.readlines())
a=(p1[2:-2])

File_2=input("Enter the path where you want to save your encrypted/decrypted text file - please use / backslash when typing in directory path: \nFor Example: C:/Users/antho/Desktop/encrypted_filet.txt\n")
nz=str(File_2)
b=str(input("Please input a 4 digit password: \n This password is the password used to lock/unlock the file: \n"))
#validate if phone number entered is 4 digits and extract one number to be used for list rotation stored under variable "d"
if  len(b)!=4:
    print("please input only last 4 digits")
else:
    c=b[1:3:3]
    d=int(c)

#split input received for message encrypted into a list of individual items        
if Options=="1":

      

    g=[h for h in a]
    
    
   

#rotate the list by moving items x no of spaces. the value of x is the value stored in variable "d"
    f= (g[len(g)-d:len(g)]+ g[0:len(g)-d]) 
    

  
    print("Your File has been encrypted and saved to the path that you provided\n")

#checking if items in list "f" match with values in master  and printing the encrypted message
    for i in f:
        if i in master:
            sys.stdout=open(nz,"a")
            print(master[i],end="")
            sys.stdout.close()
            
          

#Requesting input of encrypted message to be decrypted ( received from the above part of code)
else:
    j=a
        
#k is the interval value by which the encrypted string will be split. In this case we use 4 as len of values in dictionary is equal to 4. 
    k=4

#the list after splitting is stored under variable"m"
    m=[j[l:l+k] for l in range(0, len(j), k)]
   

#rotating the list so it represents the original order as stored in "g"
    s= (m[-(len(m)-d):len(m)]+ m[0:-(len(m)- d)]) 
    

#interchanging keys and values on "master" dictionary 

    rev = dict((v,k) for k,v in master.items())
    print("Your File has been decrypted and saved to the path that you provided\n\n***Kindly note:Every NEW LINE in the decrypted file is denoted by 'n'***")

#checking if items in the list "s" match with values on the reversed dictionary "rev" and printing decrypted message
    for n in s:
        if n in rev:
            sys.stdout=open(nz,"a")
            print(rev[n],end="")
            sys.stdout.close()

           

   

