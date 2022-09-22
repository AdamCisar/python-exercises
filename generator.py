import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

password_sum = []

print('Generartor hesiel!')
password_letters=int((input('Kolko chces znakov?\n')))

for i in range(0,password_letters):
        letters_choice = random.choice(letters)
        password_sum.append(letters_choice)

password_numbers=int(input('Kolko chces cisel?\n'))

for i in range(0,password_numbers):
        numbers_choice = random.choice(numbers)
        password_sum.append(numbers_choice)

password_special_char=int(input('Kolko chces specialnych znakov?\n'))
 
for i in range(0,password_special_char): 
        special_choice = random.choice(special_char)
        password_sum.append(special_choice)

random.shuffle(password_sum)
for x in password_sum:
     print(x,end = '')
    
    
  



