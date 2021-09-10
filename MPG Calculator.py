#Created on 5 September 2021
#This is a calculator that takes tripometer data divided by gallons of fuel to tell the user
#how efficient their car is and how much it cost to fill up their tank

#Declare variables
miles = float(input("Enter in the number of miles on your tripometer before you reset: "))
gals = float(input("Enter the amount, in gallons, of fuel that you added at the last fillup: "))
price = float(input("Enter the price of gas per gallon to three decimal places (x.xx9): "))

#Do the math!
mpg = miles/gals

print("*********************************************************")
#Print results
print("Your average fuel efficiency is (MPG):", round(mpg, 2))

#Now calculate the price per gallon
ppg = price*gals
print("Your total price per gallon was approximately: $", round(ppg, 2))

if(mpg < 20):
    print("\nIn-town driving just doesn't cut it!")
elif(mpg >= 20):
    print("\nDo you live on the highway or are you just efficient?")
    
print("\nPlease save this for your records")