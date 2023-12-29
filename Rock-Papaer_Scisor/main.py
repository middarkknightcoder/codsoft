import random 
import pwinput as pi
import pymongo as pm 

myclient = pm.MongoClient("mongodb://localhost:27017/")

db = myclient["GameDB"]

col = db["userProf"]
    
GameWins = 0
GamePlayedCount = 0

# f = open("Game.txt" ,"a")
num = (int)(input('''Choose what you want to do =>>> 
                  1. login
                  2. create new account
                  =>> '''))

if(num == 1):
    uname = input("Enter Your UserName : ")
    flag = 0
    while(flag == 0):
        if(col.find_one({"UserName" : uname})):
            password = pi.pwinput(prompt="Enter Your Password : " ,mask="*")
            if(col.find_one({"UserName" : uname})["Password"] == password):
                flag = 1
            else:
                print("Wrong Password ! Try Again ")
        else:
            uname = input("User name is not found , Enter Again : ")  
        # Here we are transfer the previews data
        user = col.find_one({"UserName" : uname})
        GameWins = user["GameWins"]
        GamePlayedCount = user["GamePlayedCount"]
        
elif(num == 2):
    name = input("Enter Your full name : ")
    uname = input("Enter Your UserName : ")
    flag = 0
    while(flag == 0):
        if(col.find_one({"UserName" : uname})):
            flag = 0
            uname = input("Pls Choose another UserName This userName is already Taken  : ")
        else:
            flag = 1
    password = pi.pwinput(prompt="Set Your Pssword : " ,mask="*")
    userDict = {
            "Name" : name,
            "UserName" : uname,
            "Password" : password,
            "GameWins" : GameWins,
            "GamePlayedCount" : GamePlayedCount
        }           
    col.insert_one(userDict)
else:
    print("Pls choose right number for enter into the Game !")

# Game Functions

def compChoise(comp):
    if(comp == 1):
        return "Rock"
    elif(comp == 2):
        return "Paper"
    elif(comp == 3):
        return "Scissor" 

def userChoise(uesr):
    if(user == 1):
        return "Rock"
    elif(user == 2):
        return "Paper"
    elif(user == 3):
        return "Scissor"
    
def ShowGameProfile():
    user = col.find_one({"UserName" : uname})
    print(" ")
    print(f'''{user["Name"]}'s Game Profile =>>>
          
            Player UserName : {user["UserName"]}
            Number of playing Games : {user["GamePlayedCount"]}
            Game Win : {user["GameWins"]}
            ''')

def CheckAnotherProfile(pname):
    query = {"$or" : [{"Name" : {"$regex" : pname}} ,{"UserName" : {"$regex" : pname}}]}
    if(col.find_one(query)):
        user = col.find_one(query)
        print(" ")
        print(f'''{user["Name"]}'s Game Profile =>>>
          
            Player UserName : {user["UserName"]}
            Number of playing Games : {user["GamePlayedCount"]}
            Game Win : {user["GameWins"]}
            ''')
    else:
        print("Player is not found !")
        
def PlayGame(GameWins ,GamePlayedCount):
        count=1
        userWin=0
        compWin=0
        flag = 1
        while(flag != 0):
            x = col.find_one({"UserName" : uname})
            comp = random.randint(1 ,3)
            user = (int)(input("Pls Guess =>>> 1. Rock , 2. Paper , 3. Scissors : "))

            print(f"Comp Guess : {compChoise(comp)} and User Guess: {userChoise(user)}")

            if(comp == 1 and user == 1):
                print("Match Tie!")
            elif(comp == 1 and user == 2):
                print(f"{x["Name"]}'s Win The Game!")
                userWin=userWin+1
            elif(comp == 1 and user == 3):
                print(f"{x["Name"]} Lose The Game!")
                compWin=compWin+1
            elif(comp == 2 and user == 1):
                print(f"{x["Name"]} Lose The Game!")
                compWin=compWin+1
            elif(comp == 2 and user == 2):
                print("Match Tie!")
            elif(comp == 2 and user == 3):
                print(f"{x["Name"]} Win The Game!")
                userWin=userWin+1
            elif(comp == 3 and user == 1):
                print(f"{x["Name"]} Win The Game!")
                userWin=userWin+1
            elif(comp == 3 and user == 2):
                print(f"{x["Name"]} Lose The Game!")
                compWin=compWin+1
            elif(comp == 3 and user == 3):
                print("Match Tie!")
            else:
                continue
    
            print("")
            print(f'''Round - {count} Score is =>>>
            Computer Score : {compWin}
            {x["Name"]} Score : {userWin}
            ''')
            count=count+1
            flag = (int)(input("Want to play game ? (1-Continue & 0-Exit)\n"))
        count = count -1
        GameWins = GameWins + userWin
        GamePlayedCount = GamePlayedCount + count
        col.update_one({"UserName" : uname},{"$set" : {"GameWins" : GameWins}})
        col.update_one({"UserName" : uname},{"$set" : {"GamePlayedCount" : GamePlayedCount}})
  
  
# User Interface 
  
while(True):
    
    inp = (int)(input('''Choose What you want to do :
                    1. Playing Game
                    2. Show Game Profile
                    3. Check Other Game Profile
                    4. Exist into the Game
                    =>>>  '''))
    
    if(inp == 1):
        user = col.find_one({"UserName" : uname})
        GameWins = user["GameWins"]
        GamePlayedCount = user["GamePlayedCount"]
        PlayGame(GameWins ,GamePlayedCount)
        
    elif(inp == 2):
        ShowGameProfile()
    
    elif(inp == 3):
        name = input("Enter Player name which you want to check profile : ")
        CheckAnotherProfile(name)
    
    elif(inp == 4):
        break
    
    else:
        print("Pls Choose Right Number")
             