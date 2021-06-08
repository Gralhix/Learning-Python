# This will request user for a Portuguese post code and then check if it meets the requirements.
# Postcodes in Portugal have the following structure: 1234-123
# The program will then look for 4 digits, followed by a dash and then 3 last digits.

           
print("The following program will ask you for a Portuguese postcode to check if it follows the correct structure")
question = input("Do you have a Portuguese postcode? (y/n)\n> ")

if question != "y":
    print("I don't think I can help you.")

else:
    postcode = input("Please enter the post code, including the dash. E.g. 1234-123 \n> ")

if question == "y":
   
    if len(postcode) != 8:
        print("Error: You have entered too many or too few digits")
        exit()
        
    elif postcode[4] != "-":
        print("Error: The dash is missing.")
        exit()
    for i in range (0,4):
        if not postcode[i].isdecimal():
            print("Error: The first 4 characters are not digits. Please only enter numbers.")
            exit()
            
    for i in range (5,7):
        if not postcode[i].isdecimal():
            print("Error: The last 3 characters must be digits.")
            exit()   

    print("Thank you. That is indeed a Portuguese postcode.")
   
