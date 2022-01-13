''' 
HEALTH MANAGEMENT SYSTEM
Problem statement: 
    1. You have 3 clients namely; Nidhish, Mann, Karan
    2. You will make 3 files to log their food and 3 files to log their excercises
       Write a function that wehn executed takes an input as client name and the thing he wants to log
       that is excercise/food.
       Use getDate function and use it as 
       example - [time using getdate] Food eaten
    3. Make one more function to retrieve data from the given files
'''

# Initializing variables
clientList = {1:"Nidhish", 2:"Mann", 3:"Karan"}
dataList = {1:"Food", 2:"Excercise"}

# To get the current time of the system
def getDate():
    import datetime
    return datetime.datetime.now()

# Defining the function to log data
def logData():
    # Displaying clients list to the user
    print("\nWhom do you want to log data for?")
    print("\nClients list...")
    for key,clientName in clientList.items():
        print(key, clientName, sep=":")
    # Selecting the client from client's list
    try:
        clientChoice = int(input("Enter your choice: "))
        if clientChoice == 1: # If user wants to log data for Nidhish
            # Displaying things which can be logged
            print("What do you want to log?\nOptions are...")
            for key,things in dataList.items():
                print(key, things, sep=":")
            try:
                thingsChoice = int(input("Enter your choice: "))
                if thingsChoice == 1: # If user wants to log food data
                    with open("Nidhish's Food Log.txt","a") as fileInstance:
                        food = input("What did you eat?: ")
                        fileInstance.write(f"[{getDate()}] = {food} \n")
                elif thingsChoice == 2: # If user wants to log excercise data
                    with open("Nidhish's Excercise Log.txt","a") as fileInstance:
                        exc = input("What did you excercise?: ")
                        fileInstance.write(f"[{getDate()}] = {exc} \n")
                else:
                    print("Please enter a valid input!")
            except Exception:
                print("Please enter a valid input!")
        elif clientChoice == 2: # If user wants to log data for Mann
            print("What do you want to log?\nOptions are...")
            for key,things in dataList.items():
                print(key, things, sep=":")
            try:
                thingsChoice = int(input("Enter your choice: "))
                if thingsChoice == 1: # If user wants to log food data
                    with open("Mann's Food Log.txt","a") as fileInstance:
                        food = input("What did you eat?: ")
                        fileInstance.write(f"[{getDate()}] = {food} \n")
                elif thingsChoice == 2: # If user wants to log excercise data
                    with open("Mann's Excercise Log.txt","a") as fileInstance:
                        exc = input("What did you excercise?: ")
                        fileInstance.write(f"[{getDate()}] = {exc} \n")
                else:
                    print("Please enter a valid input!")
            except Exception:
                print("Please enter a valid input!")
        elif clientChoice == 3: # If user wants to log data for Karan
            print("What do you want to log?\nOptions are...")
            for key,things in dataList.items():
                print(key, things, sep=":")
            try:
                thingsChoice = int(input("Enter your choice: "))
                if thingsChoice == 1: # If user wants to log food data
                    with open("Karan's Food Log.txt","a") as fileInstance:
                        food = input("What did you eat?: ")
                        fileInstance.write(f"[{getDate()}] = {food} \n")
                elif thingsChoice == 2: # If user wants to log excercise data
                    with open("Karan's Excercise Log.txt","a") as fileInstance:
                        exc = input("What did you excercise?: ")
                        fileInstance.write(f"[{getDate()}] = {exc} \n")
                else:
                    print("Please enter a valid input!")
            except Exception:
                print("Please enter a valid input!")
        else:
            print("Please enter a valid input!")
    except Exception:
        print("Please enter a valid input!")

# Defining the function to retrieve data
def retrieveData():
    # Displaying clients list to the user
    print("\nWhom do you want to retrieve data for?")
    print("\nClients list...")
    for key,clientName in clientList.items():
        print(key, clientName, sep=":")
    # Selecting the client from client's list
    try:
        clientChoice = int(input("Enter your choice: "))
        if clientChoice == 1: # If user wants to retrieve data for Nidhish
            print("\nWhat do you want to retrieve?\nOptions are...")
            for key,things in dataList.items():
                print(key, things, sep=":")
            try:
                thingsChoice = int(input("Enter your choice: "))
                if thingsChoice == 1: # If user wants to retrieve food data
                    with open("Nidhish's Food Log.txt","r") as fileInstance:
                        print("Food log...")
                        print(fileInstance.read())
                elif thingsChoice == 2: # If user wants to retrieve excercise data
                    with open("Nidhish's Excercise Log.txt","r") as fileInstance:
                        print("Excercise log...")
                        print(fileInstance.read())
                else:
                    print("Please enter a valid input!")
            except Exception:
                print("Please enter a valid input!")
        elif clientChoice == 2: # If user wants to retrieve data for Mann
            print("\nWhat do you want to retrieve?\nOptions are...")
            for key,things in dataList.items():
                print(key, things, sep=":")
            try:
                thingsChoice = int(input("Enter your choice: "))
                if thingsChoice == 1: # If user wants to retrieve food data
                    with open("Mann's Food Log.txt","r") as fileInstance:
                        print("Food log...")
                        print(fileInstance.read())
                elif thingsChoice == 2: # If user wants to retrieve excercise data
                    with open("Mann's Excercise Log.txt","r") as fileInstance:
                        print("Excercise log...")
                        print(fileInstance.read())
                else:
                    print("Please enter a valid input!")
            except Exception:
                print("Please enter a valid input!")               
        elif clientChoice == 3: # If user wants to retrieve data for Karan
            print("\nWhat do you want to retrieve?\nOptions are...")
            for key,things in dataList.items():
                print(key, things, sep=":")
            try:
                thingsChoice = int(input("Enter your choice: "))
                if thingsChoice == 1: # If user wants to retrieve food data
                    with open("Karan's Food Log.txt","r") as fileInstance:
                        print("Food log...")
                        print(fileInstance.read())
                elif thingsChoice == 2: # If user wants to retrieve excercise data
                    with open("Karan's Excercise Log.txt","r") as fileInstance:
                        print("Excercise log...")
                        print(fileInstance.read())
                else:
                    print("Please enter a valid input!")
            except Exception:
                print("Please enter a valid input!")
        else:
            print("Please enter a valid input!")
    except Exception:
        print("Please enter a valid input!")

def main():
    # Introducing system to the user
    print("""\t\t\t\t\t\tWelcome to Nidhish's Health Management System!
\n\t\t\t\tHere you can manage your client's food and excercise data according to the time. 
\t\t\tYou have two options! Either you can log your client's data or you can retrieve your client's data.""")

    contVar = 'y' # Variable to decide if the user wants to continue the process
    while contVar == 'y' or contVar == 'Y':
        try:
            # Taking input for what the user wants to do first
            print("\nWhat do you want to do?\n1. Log data\n2. Retrieve data")
            dataChoice = int(input("Enter your choice: "))
            if dataChoice == 1:
                logData()
            elif dataChoice == 2:
                retrieveData()
            else:
                print("Please enter a valid input!")
        except Exception as e:
            print("Please enter a valid input!")
        contVar = input("Do you want to continue? y or n?: ")
        contVar.lower()

if __name__ == "__main__":
    main()

