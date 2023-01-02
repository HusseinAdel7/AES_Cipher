import os.path
from sys import platform
import os 
import string
from termcolor import colored
from Crypto.Cipher import DES3
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random 
from Crypto.Cipher import DES3


os.system('clear') 

print ("\n\n\t\t\t    ------------------")
print(colored('\t\t\t      Cryptography ', 'yellow'))
print ("\t\t\t    ------------------")
print(colored('\n\t\t     * Written by : ', 'green'),end="")
print(colored(' Hussein Adel', 'white'),end="")
print ("\n\t\t\t\t     ------------\n")
print (" ===========================================================================\n")
print (colored('\t\t\t\t  ------------','white'))
print(colored('\t\t\t\t    Hello \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ------------\n','white'))

#------------------------------------------------------------------------  
#========================================================================
# Auto Key Cipher 

def AES_cipher(data):     
    Key=Random.new().read(16)
    iv= Random.new().read(16)
    # Mode CBC (Cipher Block Chain)
    print("\n")
    print("*********AES CBC Mode************")
    encrm=AES.new(Key,AES.MODE_CBC,iv)
    padding=lambda s: s + (16 - len(s) % 16) * "*"
    encrypted_message=encrm.encrypt(padding(data).encode("ascii"))
    print(encrypted_message)
    decrm=AES.new(Key,AES.MODE_CBC,iv)
    decrypted_message = decrm.decrypt(encrypted_message)
    NewData = decrypted_message.decode("ascii")
    VeryNew=NewData.strip("*")
    print(VeryNew)
    # Mode OFB (Output FeedBack)
    print("========================")
    print("\n")
    print("*********AES OFB Mode************")
    enc = AES.new(Key,AES.MODE_OFB,iv)
    enc_Mess = enc.encrypt(data.encode("ascii"))
    print(enc_Mess)
    dec = AES.new(Key,AES.MODE_OFB,iv) 
    dec_Mess = dec.decrypt(enc_Mess)
    AAfData = dec_Mess.decode("ascii")
    print(AAfData)
    # Mode CTR 
    print("========================")
    print("\n")
    print("*********AES CTR Mode************")
    counter = Counter.new(128)
    encc=AES.new(Key,AES.MODE_CTR,counter=counter)
    encrypted_m=encc.encrypt(padding(data).encode("ascii"))
    print(encrypted_m)
    decc=AES.new(Key,AES.MODE_CTR,counter=counter)
    decrypted_m =decc.decrypt(encrypted_m)
    AfData = decrypted_m.decode("ascii")
    ANew=AfData.strip("*")
    print(ANew)




plain_Text =str(input(colored("\nEnter Your Message That You Wanna encrypt :  " , 'green')))
AES_cipher(plain_Text)

#---------------------------------------------------------------------------------------
print (colored('\n\n\t\t\t\t  ----------','white'))
print(colored('\t\t\t\t    Done \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ----------\n','white'))

