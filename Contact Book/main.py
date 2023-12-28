# Here We are create a Contact Book Which is stored people contact details.
# ******* Note : When you create a collection and "insert the document" into the database "after you can see your collections and database" into the mongodb (before this all step if try to watch database or collection throw error like , can't create new thread at interpreter shutdown)

import pymongo as pm

# Create a connection
myclient = pm.MongoClient("mongodb+srv://ronakkantariya2004:Rkmongodb2004@cluster0.mdhea00.mongodb.net/")  

# Create Database into MongoDB
db = myclient["ContactDB"]

# Create Collection into ContactDB
col = db["contacts"]


# Add Contact Number
def AddContact():
    
    name = input("Enter Contact Name : ")
    
    phnumber = input("Enter Phone Number : ")
    while(len(phnumber) != 10 or phnumber.isdigit() == False):
        print("Pls Enter 10 Digits Phone Number !")
        phnumber = input("Enter Phone Number : ")
        
    email = input("Enter Email ID : ")
    while(email.endswith("@gmail.com") == False):
        print("Pls Enter Right Form of Email !")
        email = input("Enter Email ID : ")
        
    address = input("Resident Address : ")
    
    if(col.find_one({"PHnumber" : phnumber})):
        print("Phone Number Alredy Exist !")
    else:
        ContactDict = {
        "Name" : name.title(),
        "PHnumber" : phnumber,
        "Email" : email,
        "Address" : address.title()}
        
        col.insert_one(ContactDict)
        print("")
        print(f"{name.title()}'s Contact Number is Added.....")
        print("")

        
# Show all contacts     
def ShowContacts():
    
    print("Saved Contact List =>>> ")
    for x in col.find():
        print(f'''
              Name  :  {x["Name"]}   
              Phone No : {x["PHnumber"]} 
              Email : {x["Email"]}
              Current Adress : {x["Address"]}
              ''')


# Search perticular contact number
def SearchContact(ufind):
    query = { "$or": [{"Name" : { "$regex": ufind }} ,{"PHnumber": { "$regex": f"^{ufind}" }}]}
    if(col.find_one(query)):
        uI = col.find_one(query)
        print(f'''Contact Info =>>> 
              
              Name : {uI["Name"]}
              Phone No : {uI["PHnumber"]}
              Email : {uI["Email"]}
              Current Address : {uI["Address"]}
              ''')
    else:
        print("")
        print("Contact Number is NotFound Try Again !")
    print("")
        

# Update Contact Number
def UpdateContact(findU):
    query = { "$or": [{"Name" : { "$regex": findU }} ,{"PHnumber": { "$regex": f"^{findU}" }}]}
    if(col.find_one(query)):
        num = (int)(input('''What you need to upade choose =>>>: 
                            1. Name
                            2. Phone Number
                            3. Email Adress
                            4. Current Address
                            =>>>  '''))
        if(num == 1):
            name = input("Enter Contact Name : ")
            col.update_one(query ,{"$set" : {"Name" : name.title()}})
        elif(num == 2):
            phnumber = input("Enter Phone Number : ")
            while(len(phnumber) != 10 or phnumber.isdigit() == False):
                print("Pls Enter 10 Digits Phone Number !")
                phnumber = input("Enter Phone Number : ")
            col.update_one(query ,{"$set" : {"PHnumber" : phnumber}})
        elif(num == 3):
            email = input("Enter Email ID : ")
            while(email.endswith("@gmail.com") == False):
                print("Pls Enter Right Form of Email !")
                email = input("Enter Email ID : ")
            col.update_one(query ,{"$set" : {"Email" : email}})
        elif(num == 4):
            address = input("Resident Address : ")
            col.update_one(query ,{"$set" : {"Address" : address}})
        else:
            print("Pls choose Right number !")
    
        print("\nContact is Updated....\n")
    else:
        print("Contact Number is NotFound Pls Try Again !")       
    print("")    
   
    
# Delete perticular contact number
def DeleteContact(udel):
    query = {"$or" : [{"Name" : {"$regex" : udel}} ,{"PHnumber" : {"$regex" : f"^{udel}" }}]}   # ^{udel} - Represent phone number is check using prefix
    if(col.find_one(query)):
        x = col.find_one(query)
        col.delete_one(query)
        print("")
        print(f"{x["Name"]}'s Contact Number Deleted....")
        print("")
    else:
        print("Contact is NotFound Try Again !")
    
# User Interface or Handle

while(True):
    
    try:
        num = (int)(input(''' Choose Number for use Contact app :
                        1. Add Contact
                        2. Show Contacts
                        3. Search Contact
                        4. Update Contact
                        5. Delete Contact
                        0. Exit
                        =>>>  '''))
        print("")
    
        if(num == 1):
            AddContact()
        elif(num == 2):
            ShowContacts()
        elif(num == 3):
            find = input("Enter Name or Phone number for search contact : ")
            SearchContact(find)
        elif(num == 4):
            findU = input("Enter Name or Phone number for search contact : ")
            UpdateContact(findU)
        elif(num == 5):
            delete = input("Enter Name or Phone number for search contact : ")
            DeleteContact(delete)
        elif(num == 0):
            break
        else:
            print("Pls Choose Right Number !\n")
    except :
        print("Enter Your input in Numeric form !\n")

