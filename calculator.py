import os
while True:    
    while True:
             
        number1 = float(input('Ake je prve cislo?\n'))


        signs = ['+', '-', '/', '*']
        for i in signs:
            print(i)
        sign_input = input('Vyberte si operaciu ')

        number2 = float(input('Vlozte druhe cislo\n'))

        def result(number1, number2, sign_input):
            if sign_input == '+':
                return number1 + number2
            elif sign_input == '-':
                return number1 - number2
            elif sign_input == '/':
                return number1 / number2
            elif sign_input == '*':
                return number1 * number2
        result_number = result(number1,number2, sign_input)

        print(f'{number1} {sign_input} {number2} = {result_number}')

        choice = input('Napiste "ano", ak chcete pokracovat. Napiste "nie", ak chcete novu kalkulaciu\n')

        if choice == 'ano':
            break
        
        if choice == 'nie':    
            os.system('cls') 
            continue
        
              

    while True:
        number1 = result_number
        signs = ['+', '-', '/', '*']
        for i in signs:
            print(i)
        sign_input = input('Vyberte si operaciu ')

        number2 = float(input('Vlozte druhe cislo\n'))

        def result(number1, number2, sign_input):
            if sign_input == '+':
                return number1 + number2
            elif sign_input == '-':
                return number1 - number2
            elif sign_input == '/':
                return number1 / number2
            elif sign_input == '*':
                return number1 * number2
        result_number = result(number1,number2, sign_input)

        print(f'{number1} {sign_input} {number2} = {result_number}')

        choice = input('Napiste "ano", ak chcete pokracovat. Napiste "nie", ak chcete novu kalkulaciu\n')

    
        if choice == 'ano':
            continue
        elif choice == 'nie':
            break
    os.system('cls')

