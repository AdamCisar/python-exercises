auction_logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''






import os
print(auction_logo)
print('Vitajte v programu pre tichu drazbu')

buyers = {

}
highest_offer = []

while True:
    
    name = input('Ake je vase meno\n')
    offer = int(input('Aka je vasa ponuka?\n'))
    #pridavanie do slovnika
    buyers[name] = offer
    
    #zastavenie alebo pokracovanie
    decision = input('Su dalsi kupujuci? Napiste "ano" alebo "nie"\n')
        
    if decision == 'nie':
        break
    
os.system('cls||clear')

#najvacsia ponuka
number = 0
for key in buyers:
    if number < buyers[key]:
        number = buyers[key]


#hladanie vitaza
for winner in buyers:
    if number == buyers[winner]:
        print(f'Vitazom je {winner} s ponukou {number}')

