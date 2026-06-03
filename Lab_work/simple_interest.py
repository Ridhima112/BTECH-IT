# Program to calculate Simple Interest with validation
#input the principle,rate,time

    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Rate of Interest (%): "))
    time = float(input("Enter Time (years): "))
#--------------------------------------------------------

    #validate the input values
    if (principal <= 0):
        print("Principal should be greater than 0")
#-------------------------------------------------------
    elif ( rate < 0):
        print("rate cannot be negative")
#--------------------------------------------------
    elif I(time <= 0):
        print("Time must be greater than 0")
#------------------------------------------------
        #displaying the interest
    else:
        si = (principal * rate * time) / 100
        print("Simple Interest =", si)

