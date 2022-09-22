MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.60,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.00,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 2.40,
    }
}
 
resources = {
    "water": 400,
    "milk": 300,
    "coffee": 150,
}


while True:
    choice = input('Co by ste si dali? Espresso/Latte/Cappuccino\n').lower()

    # funkcia report / zobrazuje zostatok surovin
    if choice == 'report':
            for i in resources:
                print(i +': '+ str(resources[i]))
    
    else:
        result_water = resources['water'] - MENU[choice]['ingredients']['water']
        result_milk = resources['milk']- MENU[choice]['ingredients']['milk']
        result_coffee = resources['coffee']- MENU[choice]['ingredients']['coffee']
      
        #zistuje ci ma dostatok surovin
        def finding(result_water,result_milk,result_coffee):
            if result_water >= 0:
                if result_milk >= 0:
                    if result_coffee >= 0:
                        print('Mame dostatok ingrediencii')
                    else:
                        return False
                else:
                    return False
            else:
                return False                
        finding = finding(result_water,result_milk,result_coffee)
        if finding == False:
            print('Nemame dostatok ingrediencii')
            break


        resources['water'] =  result_water
        resources['milk'] = result_milk
        resources['coffee'] = result_coffee
            
        

        #pocet minci / input
        def cost():
            cost5 = round(0.05 * int(input('Kolko 5 cenotivek chcete vlozit?\n')),2)
            cost10 = round(0.10 * int(input('Kolko 10 cenotivek chcete vlozit?\n')),2)
            cost20 = round(0.20 * int(input('Kolko 20 cenotivek chcete vlozit?\n')),2)
            cost50 = round(0.50 * int(input('Kolko 50 cenotivek chcete vlozit?\n')),2)
            cost1 = round(1.00 * int(input('Kolko 1 euroviek chcete vlozit?\n')),2)
            cost2 = round(2.00 * int(input('Kolko 2 euroviek chcete vlozit?\n')),2)
            result_cost = cost5 + cost10 + cost20 + cost50 + cost1 + cost2
            resultcost_rounded = '%.2f' % (result_cost)
            print(f'Celkom ste vlozili: {resultcost_rounded} Eur')
            printchoice = MENU[choice]['cost']
            printchoice = '%.2f' % printchoice
            print(f'{choice.capitalize()} stoji: {printchoice} Eur')
            
            def coins(result_cost,MENU):
                result = result_cost - MENU['cost']
                if result < 0:
                    print('Nevlozili ste dostatok minci. Ak nemate dostatok minci a chcete zrusit program, napiste "exit"')
                    cost()
                elif result > 0:
                    result = '%.2f' % result
                    print (f'Vratene mince: {result}')
                    print('Napoj sa pripravuje.')
                else:
                    print('Napoj sa pripravuje.')    
            coins(result_cost,MENU[choice])    
        cost()
