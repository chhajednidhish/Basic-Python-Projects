# Introducing my dictionary to users
print("Nidhish Dictionary".center(40,"-"))

#Creating a dictionary
NidhishDictionary = {
"Narcotics":"A substance used to treat moderate to severe pain", "Religious":"Connected with religion",
"Terrific":"Extremely nice or good", "Trust":"The belief that somebody is good, honest or sincere", 
"Humble":"Not proud", "Auspicious":"That seems likely to be succesful in future" }

#Printing the words available in dictionary
print("\nWords available in our dictionary are ...")
for key in NidhishDictionary:
    print(key)

# While loop to find words as many times as user wants to 
continuation = "Y"
while continuation == "Y":
    #Taking user input of the word 
    UserInput = input("\nEnter the word you want to know the meaning of: ")
    UserInput = UserInput.capitalize()

    #Printing meaning of the word
    try:  
        if(NidhishDictionary[UserInput]):
            print("Meaning of ",UserInput," is as follows: ",NidhishDictionary[UserInput])
        else:
            raise KeyError

    #Accepting error if the user enters any word that is non existent in my dictionary
    except KeyError:
        print("The following word does not exist!")

    continuation = input("\nDo you want to continue knowing meaning of the word?\nPress Y to continue or press any other key.")
    continuation = continuation.upper()

#Adding new words to my dictionary provided by user
Contri = input("\nDo you want to contribute in my dictionary?\nPress y to continue or press any other key.")
while Contri == "y":
    KeyValue = input("Enter the word that you know the meaning of: ")
    MeaningUser = input("Enter meaning for the following word: ")
    NidhishDictionary[KeyValue] = MeaningUser
    Contri = input("\nDo you want to contribute in my dictionary?\nPress y to continue or press any other key.")
    Contri = Contri.upper()

#Printing dictionary after the user contribution
print("\nDictionary after your contribution looks like this ...")
for key,meaning in NidhishDictionary.items():
    print(key,meaning,sep=" : ")


print("\n\tThank you for using my dictionary!")
