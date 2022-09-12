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
while lives != 0:
    guess = input('Uhadni pismeno alebo cele slovo\n').upper()
    if guess == random_word:
        print(random_word)
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
print('Vyhral si!')





