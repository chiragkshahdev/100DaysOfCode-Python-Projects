import random

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_Letters = int(input("How many letters would you like in your password?\n"))
nr_Symbols = int(input(f"How many symbols would you like?\n"))
nr_Numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order me password: Letters + Symbols + Numbers
# Password = ""
# for char in range(1, nr_Letters):
#     Password += random.choice(Letters)
# for char in range(nr_Symbols):
#     Password += random.choice(Symbols)
# for char in range(nr_Numbers):
#     Password += random.choice(Numbers)
# print(Password)

# Hard Level - random shuffle 
Password_list = []

for char in range(nr_Letters):
    Password_list.append(random.choice(Letters))

for char in range(nr_Symbols):
    Password_list.append(random.choice(Symbols))

for char in range(nr_Numbers):
    Password_list.append(random.choice(Numbers))

random.shuffle(Password_list)

Password = ""
for char in Password_list:
    Password += char

print(f"Your password is: {Password}")