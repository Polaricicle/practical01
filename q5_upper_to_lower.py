#Filename: q5_upper_to_lower.py
#Author: Tan Di Sheng
#Created: 20130123
#Modified: 20130123
#Description: This program is used to convert an uppercase letter
#from standard input to a lowercase letter by making use of its ASCII value
#or vice versa

print("""This application is used to convert an uppercase letter to a
lowercase letter and vice versa""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    #Converts the input to its ACSII value
    lInput = ord(input("Please input a letter here: "))
    sOutput = chr(lInput + 32)
    uOutput = chr(lInput - 32)
    
    #After converting the letter to its ACSII value, the value is then
    #compared to see whether it is a uppercase letter or a lowercase
    #letter, before proceeding to printing the appropriate output
    if 64 < lInput < 91:
        print(sOutput)
    elif 96 < lInput < 123:
        print(uOutput)

    #Allows the user to choose whether to continue or stop using
    #the application.
    contorquit = input("Continue? (Type yes or no): ")
    if contorquit == "no":
        quit()
    elif contorquit == "yes":
        continue
        
        
