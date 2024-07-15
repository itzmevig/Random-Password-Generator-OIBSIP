# Random Password Generator

import random
ltrs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symb = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\t\tRANDOM PASSWORD GENERATOR!\n")
l = int(input("\nLength of password: "))
num_ltrs= int(input("\nNumber of letters required: "))
num_symb = int(input("\nNumber of symbols required: "))
num_numbrs = int(input("\nNumber of numbers required: "))

password = []
for i in range(0, num_ltrs):
    password.append(random.choice(ltrs))

for i in range(0, num_symb):
    password.append(random.choice(symb))

for i in range(0, num_numbrs):
    password.append(random.choice(num))

random.shuffle(password)
print(f"The randomly generated password is: {''.join(password)}")