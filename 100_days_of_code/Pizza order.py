# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    bill += 3

elif add_pepperoni == "N":
    bill += 0

if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is ${bill}")
elif extra_cheese == "N":
    bill += 0
    print(f"Your final bill is ${bill}")