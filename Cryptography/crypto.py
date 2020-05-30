####sample scrypt to encrypt and decrypt


#ask for user input
a=input("please enter your top secret message: \n")

b=str(input("last 4 diguts of your phone number: \n"))

#validate if phone number entered is 4 digits and extract one number to be used for list rotation stored under variable "d"
if  len(b)!=4:
    print("please input only last 4 digits")
else:
    c=b[1:3:3]
    d=int(c)  
    
#split input received for message encrypted into a list of individual items
g=[h for h in a]


#rotate the list by moving items x no of spaces. the value of x is the value stored in variable "d"
f= (g[len(g)-d:len(g)]+ g[0:len(g)-d]) 

#master reference list 
master={'A':'Jkbj','B': 'kbsi', 'C':'hnwf','D':'j’ix','E':'zfcx','F':'zasx','G':'degt','H':'u6ku','I':',j,a','J':'rfgu','K':'iln/','L':'jklj','M':'io89','N':'7y6g','O':'uj/;','P':'Kagg','Q':'yUJJ','R':'YI8I','S':'hyui','T':'uuKU','U':'Uujh','V':'yg^y','W':'tffd','X':'dgy&','Y':'8okk','Z':'&*nj',"a":"gtfd","b":"$32g", "c":"fgsd", "d":"8&89","e":"cfjl","f":"0h^g","g":"dh#7","h":")J(5","i":"hadj"," ":"uhty","j":"nb6d","k":"!8f#","l":"4jaj","m":"tg4p","n":"&6gh","o":"^98$","p":"bt98","q":"b438","r":"89h6","s":"oijh","t":"87#t","u":"NIHT","v":"&15b","w":"Stg^","x":"87H6","y":"gdfh","z":"8&%^","0":"ikgt","1":"fgty","2":"ThGt","3":"&^hj","4":"POlk","5":"mnjh","6":"^&%j","7":"mijh","8":"789j","9":"yh{o","!":"kjnb","@":"trFb","#":"nilo","$":"Pl*&","%":"5875","^":"kjhy","&":"tr46","*":"yt0&","(":"JH>k",")":"mnh7",":":"freh",";":"bhyt","'":"plki",'"':"7hgt","/":"Ft5r","?":"po8s",",":"7*9^",".":"yh4&"}
print("Your encrypted message is:\n")


#checking if items in list "f" match with values in master  and printing the encrypted message
for i in f:
    if i in master:
        print( master[i],end="")
print("\n")
print("\n")
print("\n")


#Requesting input of encrypted message to be decrypted ( received from the above part of code)
j=input("please enter the message you want to decrypt: \n " )

#k is the interval value by which the encrypted string will be split. In this case we use 4 as len of values in dictionary is equal to 4. 
k=4

#the list after splitting is stored under variable"m"
m=[j[l:l+k] for l in range(0, len(j), k)]

#rotating the list so it represents the original order as stored in "g"
s= (m[-(len(m)-d):len(m)]+ m[0:-(len(m)- d)]) 

#interchanging keys and values on "master" dictionary 

rev = dict((v,k) for k,v in master.items())
print("your decrypted message is :\n ")

#checking if items in the list "s" match with values on the reversed dictionary "rev" and printing decrypted message
for n in s:
    if n in rev:
        print(rev[n],end="")
