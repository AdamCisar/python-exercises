import random
words = ['HENRY', 'MARIA', 'RON', 'GLEN', 'ADAM', 'VERONIKA', 'BRANO', 'MARIANA']
random_word = random.choice(words)

#prazdne polia
word_guess = []
for one in range(0, len(random_word)):
    word_guess.append('_')
for i in word_guess:
    print(i, end=' ')
print()

#zivoty
lives = 6

#hra
while True:
    if '_' not in word_guess:
        print('Vyhral si!')
        break
    guess = input('Uhadni pismeno alebo cele slovo\n').upper()
    if guess == random_word:
        print(random_word)
        print('Vyhral si!')
        break
    else:    
        for index in range(0, len(random_word)):
            if guess == random_word[index]:
                word_guess[index] = guess

        for i in word_guess:
            print(i, end=' ')
        print()
    if guess not in random_word:
        lives -= 1
        print(f'Pocet tvojich zivotov je {lives}')
    if lives == 0:
        print('Dosli ti zivoty. Prehral si.')
        break
    





