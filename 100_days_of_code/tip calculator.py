#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator!") #Welcome message
bill = input("What was the total bill?$ " ) #Total bill input by user
amount_to_give = input("How much tip would you like to give? 10, 12 or 15? ") # Percentage of tip to be given
no_of_people = input("How many people to split the bill? ") #Number of people to share the bill

bill_int = float(bill) #Converted bill to int
amount_int = int(amount_to_give) #Converted amount to int
people_int = int(no_of_people) #Converted people to int
percent = amount_int/100 #Divided to get percent
final = percent + 1 #Added percent to one

a = (bill_int/ people_int) * final #Calculated tip
print (f"Each person is to pay ${round(a, 2)}")
