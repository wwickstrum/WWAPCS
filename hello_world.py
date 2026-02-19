print("hello world")

age1 = 25
print(age1)

first_name = "William"
last_name = "Wickstrum"
print(first_name)
print(last_name)

x = 10
y = 5
print(x+y)
print(x-y)
print(x*y)
print(x/y)

tempature = 75
if tempature > 65:
    print(tempature)

a = 8
b = 12
if a <= b:
    print(a)

score = 85
if score >= 90:
    print(a)

is_raining= True
print(is_raining)

has_ticket= True
has_id= False
print(has_ticket and has_id)
print(has_ticket or has_id)

is_closed = True
print(not has_ticket)

name = "Alice"
age2 = 30
print(name, "is", age2, "years old")
print(f"{name} is {age2} years old")

price = 19.99
quantity= 3
print(f"total cost: {price*quantity}")

radius= 5
print(f"The area is {3.14*radius*radius}")

celsius=25
fahrenheit= 32+ celsius*1.8
print(f"{celsius}C is {fahrenheit}F")

d=15
e=4
f=2
print(d+e*f)
print((d+e)*f)

is_weekend= True
is_sunny= True
if (is_weekend and is_sunny):
    print("Go to the beach")
else:
    print("Do not go to the beach")

age3= 16
has_license=True
if (age3>=16 and has_license):
    print("You can drive")
else:
    print("You cannot drive")

hour=14
if (hour<12):
    print("Good Morning")
elif (12<=hour<18):
    print("Good Afternoon")
else:
    print("Good Evening")

password = "password"
confirm = "password"
if len(password)>=8:
    print (password and confirm)

x=7
y=14
z=21
if (x%y and x%z):
    print("x divides evenly into y and z")

name2= "Jordan"
grade=88
is_passing= grade>=60
improvemnt=12
print(f"Student {name2} scored {grade} (passing: {is_passing}) with {improvemnt} points improvement)")