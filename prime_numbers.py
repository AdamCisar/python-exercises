
number = int(input('zadaj cislo a zisti ci je to prvocislo\n'))


def first(number1):
    listofn = []
    final_result = []
    for i in range(1, (number1)+1):
       result = number1 % i
       listofn.append(result)
    for x in listofn:
        if x == 0:
            final_result.append(x)
    if len(final_result) >= 3:
        print('Nie je to prvocislo')
    else:
        print('Je to prvocislo')    
       
first(number)