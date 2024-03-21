from cryptography.fernet import Fernet
import os

def write_key(n):
    key = Fernet.generate_key()
    with open("key" + str(n) +".key", "wb") as key_file:
        key_file.write(key)
        n = n+1
        return n

def new_user():
    print("Please Enter All The User Name Only Once At The Beginning")
    username = input("Enter Your Name: ")
    master = input("Enter Your Master Key: ")
    with open("User.txt","a") as f:
        f.write("Name: " + username + "////" +"Master_Key: " + master + "\n")

    os.system('attrib +h User.txt')
def old_user():
    with open("User.txt","r") as p:
        n=1
        for line in p.readlines():
            data =line.rstrip()
            nam, k = data.split("////")

            print(str(n) + ")" + nam)
            n = n+1

def old_user_no():
    with open("User.txt","r") as p:
        n=1
        for line in p.readlines():
            data =line.rstrip()
            nam, k = data.split("////")
            n = n+1
        return n

def load_key(m):
    file = open("key"+str(m)+".key", "rb")
    key = file.read()
    file.close()
    return key

def show(q,bc):
    try:
      with open('passwords'+str(q)+'.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            acc, user, pasd = data.split(",,,,")
            print("Account: ", acc,"\n" + "User:", user, "\n" + "Password:",
                  bc.decrypt(pasd.encode()).decode())
            print("\n")
    except FileNotFoundError:
        print("Please Add A Password First")

def add(j,ab):
    account = input("Account Name: ")
    username = input("Username: ")
    password = input("Password: ")

    with open('passwords'+str(j)+'.txt', 'a') as p:
        p.write(account + ",,,," + username + ",,,," + ab.encrypt(password.encode()).decode() + "\n")

def mode(x):
   while True:
    u1=input("Do You Want To Continue?(Y/N) ").lower()
    if u1 == "y":
     old_user()
     u1 = int(input("Select User Number Or Enter 00 To Exit: "))

     if u1 == 00:
         break
     elif u1 < x :
        mode = input(
            "Do You Want To Add a New Password Or View The Existing Password? Please Enter(View or Add) , press e to quit? ").lower()
        master_key = input("Enter The Master Key: ")
        print('\n')
        key = load_key(u1) + master_key.encode()
        fer = Fernet(key)

        if mode == "e":
            break
        if mode == "view":
            show(u1,fer)
        elif mode == "add":
            add(u1,fer)
        else:
            print("Invalid mode.")
            continue
     else:
        print("Enter Valid Number")
        continue
    else:
        break

def read():
    with open('iter.txt','r') as ms:
        for line in ms.readlines():
            dat = line.rstrip()
            h = dat.split("\n")
            return int(h[-1])

def iter():
    with open("iter.txt",'a') as d:
        a= read() + 1
        d.write(str(a) + "\n")

with open("iter.txt",'a') as g:
    g.write(str(1))
i=read()
iter()
while True:
     user = input("Are You A New User Or An Old User? (New/Old). Enter 'e' To exit ").lower()
     
     if user == "new":
         new_user()

         i = write_key(i)


     elif user == "old":
         a = old_user_no()
         mode(a)
     elif user == "e":
         break
     else:
         print("Invalid Mode")
         continue








