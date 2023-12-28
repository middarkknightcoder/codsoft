# Here we are create the application which is create the todolist and also user can upadate list

import datetime as dt
import pymongo
import pwinput as pi # This pacage is used for the show user input into the star form.


# Here we are connect over proram with moongodb databse
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Add database into mongoDB localhost using myclient conection
mydb = myclient["todolistDatabase"]

# Now create collection into database 
mycol = mydb["userdb"]

TDL = []

num = (int)(input('''Choose what are you doing =>>> 
                  1. login
                  2. create new account
                  =>> '''))

if(num == 1):
    uname = input("Enter Your UserName : ")
    flag = 0
    while(flag == 0):
        if(mycol.find_one({"UserName" : uname})):
            password = pi.pwinput(prompt="Enter Your Password : " ,mask="*")
            if(mycol.find_one({"UserName" : uname})["Password"] == password):
                flag = 1
            else:
                print("Wrong Password ! Try Again ")
        else:
            uname = input("User name is not found , Enter Again : ")  
    # Here we are transfer before added task
    TDL = mycol.find_one({"UserName" : uname})["TDlist"]     
elif(num == 2):
    name = input("Enter Your full name : ")
    uname = input("Enter Your UserName : ")
    flag = 0
    while(flag == 0):
        if(mycol.find_one({"UserName" : uname})):
            flag = 0
            uname = input("Pls Choose another UserName This userName is already Taken  : ")
        else:
            flag = 1
    password = pi.pwinput(prompt="Set Your Pssword : " ,mask="*")
else:
    print("Pls choose right number !")


def addWork(work):
    TDL.append(work)
    if(mycol.find_one({"UserName" : uname})):
        mycol.update_one({"UserName" : uname} , {"$set" : {"TDlist" : TDL}})
    else:
        userDict = {
            "Name" : name,
            "UserName" : uname,
            "Password" : password,
            "   TDlist" : TDL
        }           
        mycol.insert_one(userDict)
        

def removeWork(work):
    TDL.remove(work)
    if(mycol.find_one({"UserName" : uname})):
        mycol.update_one({"UserName" : uname} , {"$set" : {"TDlist" : TDL}})  # mycol.update_one(query ,newvalue)
    

def showTDL():
    print(f"{dt.date.today()} To-Do-List Tasks =>>> ")
    print("")
    if(mycol.find_one({"UserName" : uname})):
        count=0
        for i in mycol.find_one({"UserName" : uname})["TDlist"]:
            print(f"{count} - {i}")
            count=count+1
    
while(True):
    
    try:
        num = (int)(input('''To-Do-List Fetures:
            1. Add Task
            2. Remove Task
            3. Show ToDoList
            4. Exit
            =>>>>
            '''))
        print("")
        if(num == 1):
            addwork = input("Enter Your Task for Add : ")
            addWork(addwork)
            print("")
        elif(num == 2):
            try:
                rnum = (int)(input("Enter Number of completed task : "))
                removeWork(TDL[rnum])
                print("")
            except IndexError:
                print("Enter Right Task Number ! \n")
        elif(num == 3):
            showTDL()
            print("")
        elif(num == 4):
            break
        else:
            print("Choose right number for working with ToDoList !")
    except: 
        print("Pls Enter Input in Numerical Form !")
