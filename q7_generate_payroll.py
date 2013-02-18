#Filename: q7_generate_payroll.py
#Author: Tan Di Sheng
#Created: 20130123
#Modified: 20130123
#Description: This application is used to read the information that is
#input by the user to print a payroll statement

print("""This application is used to read the information that is
input by the user to print a payroll statement\n""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        nameInput = input("Enter name: ")
        hoursInput = input("Enter number of hours worked weekly: ")
        payInput = input("Enter hourly pay rate: ")
        cpfInput = input("Enter CPF contribution rate(%): ")
        try:
            float(hoursInput) and float(payInput) and float(cpfInput)
        except:
            print("""\nPlease input numbers for the number of hours worked
weekly, hourly pay rate and CPF contribution rate\n""")
        else:
            break
        
    hoursInput = int(hoursInput)
    payInput = int(payInput)
    cpfInput = int(cpfInput)
    
    grossOutput = payInput * hoursInput
    grossOutput = int(grossOutput)
    
    cpfOutput = grossOutput / 5
    netOutput = grossOutput - cpfOutput

    print("\nPayroll statement for " + str(nameInput))
    print("Number of hours worked in a week: " + str(hoursInput))
    print("Hourly pay rate: $" + str(payInput))
    print("Gross pay = $" + str(grossOutput))
    print("CPF contribution at 20% = $" + str(cpfOutput))
    print("\nNet pay = $" + str(netOutput))

    #Allows the user to choose whether to continue or stop using
    #the application.
    contorquit = input("Continue? (Type yes or no): ")
    if contorquit == "no":
        quit()
    elif contorquit == "yes":
        continue
        
        
