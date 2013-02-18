#Filename: q6_find_ascii_char.py
#Author: Tan Di Sheng
#Created: 20130123
#Modified: 20130123
#Description: This application is used to receive an ASCII code
#(an integer between 0 and 127) and display its character.

print("""This application is used to receive an ASCII code
(an integer between 0 and 127) and display its character""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        #Checks if the input is an integer between 0 and 127
        iInput = input("\nPlease input an integer here: ")
        try:
            int(iInput)
        except:
            print("Please input an integer between 0 and 127")
        else:
            break
        
    while True:
        iInput = int(iInput)
        if not 0 <= iInput <= 127:
            print ("Please input an integer between 0 and 127")
        break
        
    iOutput = chr(iInput)    
    print(iOutput)

    #Allows the user to choose whether to continue or stop using
    #the application.
    contorquit = input("Continue? (Type yes or no): ")
    if contorquit == "no":
        quit()
    elif contorquit == "yes":
        continue
        
        
