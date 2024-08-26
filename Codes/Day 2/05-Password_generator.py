# letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# l=list(letters)
# print(l)

import random 
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like in your password?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))


password1='';
for char in range(0,nr_letters+1):
    random_letters=random.choice(letters)
    password1+=random_letters
    # print(random_letters)

# print(password1)
password2='';
for char in range(0,nr_symbols+1):
    random_symbols=random.choice(symbols)
    password2+=random_symbols
# print(password2)

password3='';
for char in range(0,nr_numbers+1):
    random_numbers=random.choice(numbers)
    password3+=random_numbers
# print(password3)

password_list=list(password1)+list(password2)+list(password3)
random.shuffle(password_list)
# print(password_list)

password=''
for char in password_list:
    password+=char #converting the above list back to string
print(password)