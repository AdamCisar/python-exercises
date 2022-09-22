import random
import os
print('Vitajte v hre "The Guessing Game"')
print('Myslim si cislo od 1 do 100')

def recursion():
    # zivoty
    difficulty = input('Vyberte si obtiaznost. Napiste "easy" alebo "hard"\n')
    if difficulty == 'easy':
        lives = 10
        print(f'Pocet vasich zivotov je {lives}')
    elif difficulty == 'hard':
        lives = 5
        print(f'Pocet vasich zivotov je {lives}')
    
    # tipovanie
    random_number = random.randint(1,100)
    while True:
        if lives == 0:
            print('Prehral si!')

            break
        tip = int(input('Tipnite si cislo: '))

        if tip == random_number:
            print('Vyhrali ste!')
            break

        elif tip < random_number:
            lives -= 1
            print(f'Prilis nizke cislo. Pocet vasich zivotov je {lives}')


        elif tip > random_number:
            lives -= 1
            print(f'Prilis vysoke cislo. Pocet vasich zivotov je {lives}')
    contin = input('Chcete pokracovat yes/no?\n')
    if contin == 'yes':
        os.system('cls')
        recursion()
        

recursion()     
    


