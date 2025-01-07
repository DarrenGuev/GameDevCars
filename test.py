# if statement 


# conditional test

cars = ['audi', 'bmw', 'subaru', 'honda']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")

# inequakity operator (!=)

requested_topping = 'mushrooms'
if requested_topping != 'onions':
    print("hold the onions!")

print("\n")

# comparison operators in python !=, >, <, ==, <=, >=


# keywords and / or

# and keyword

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

# or keyword

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

# in keyword

requested_toppings = ['mushroom', 'onion', 'pineapple']
'mushroom' in requested_toppings

print("\n")

# not keyword - use to know if a value does not appear
banned_users = ['timothy', 'edcel', 'denmar', 'paul']

user = 'timothy'
if user not in banned_users:
    print(f"Hi, {user.title()} you can post a response if you wish.")
else:
    print(f"Hi, {user.title()} you are BANNED.")

print("\n")

#boolean - true or false

game_active = True
can_edit = False

# kung ang user ay pwede na bumoto o hinde


# odd or even


#if-elif - else chain

age = int(input("Enter YOur age: "))

if age < 4:
    print("Your admission ticket is P0")
elif age < 18:
    print("Your admission ticket is P800")
else:
    print("Your admission ticket is P1000")


# multiple if statement

requested_topping = ['mushrooms', 'extra cheese', 'olives']
if 'mushrooms' in requested_topping:
    print('adding mushrooms')
if 'pepperoni' in requested_topping:
    print('adding pepperoni')
if 'olives' in requested_topping:
    print('adding olives ')
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'extra cheese', 'olives']
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("Available")
else:
    print("Not available")


# checking that a list is not empty

requested_toppings = ['hotdog']
if requested_toppings:
    for requested_topping in requested_toppings:
        print("\nFinished making your pizza")
else:
    print ("\nAre you sure you want a plain pizza?")