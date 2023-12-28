import random 

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
    
flag = 1

compWin=0
userWin=0
count=1

f = open("Game.txt" ,"a")
name = input("Enter your name : ")

while(flag != 0):
    
    comp = random.randint(1 ,3)
    user = (int)(input("Pls Guess =>>> 1. Rock , 2. Paper , 3. Scissors : "))

    print(f"Comp Guess : {compChoise(comp)} and User Guess: {userChoise(user)}")

    if(comp == 1 and user == 1):
        print("Match Tie!")
    elif(comp == 1 and user == 2):
        print(f"{name}'s Win The Game!")
        userWin=userWin+1
    elif(comp == 1 and user == 3):
        print(f"{name} Lose The Game!")
        compWin=compWin+1
    elif(comp == 2 and user == 1):
        print(f"{name} Lose The Game!")
        compWin=compWin+1
    elif(comp == 2 and user == 2):
        print("Match Tie!")
    elif(comp == 2 and user == 3):
        print(f"{name} Win The Game!")
        userWin=userWin+1
    elif(comp == 3 and user == 1):
        print(f"{name} Win The Game!")
        userWin=userWin+1
    elif(comp == 3 and user == 2):
        print(f"{name} Lose The Game!")
        compWin=compWin+1
    elif(comp == 3 and user == 3):
        print("Match Tie!")
    else:
        continue
    
    print("")
    print(f'''Round - {count} Score is =>>>
            Computer Score : {compWin}
            {name} Score : {userWin}
          ''')
    count=count+1
    flag = (int)(input("Want to play game ? (1-Continue & 0-Exit)\n"))


f.write("---------------------------------------------------------------------------\n")
f.write(f"*** {name} VS Computer ***")
f.write("\n")
f.write(f"{name} Score is : {userWin}  <-->  Computer Score is : {compWin}")
f.write("\n")
f.write("---------------------------------------------------------------------------\n")
f.write("\n")







