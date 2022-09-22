alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    choice = input('Type if encode or decode\n').lower()
    message_input = input('Type your message\n').lower()
    shift_input = int(input('Type the shift number\n'))
    if choice == 'encode':
        def encode(message, number):
                msg = []
                for index_message in message:
                    for index_encode in range(0,len(alphabet)):
                        if index_message == alphabet[index_encode]:
                            msg.append(index_encode + number)
                for i in msg:
                    if i not in range(0, len(alphabet)):
                        i -= 26   
                        print(alphabet[i], end='')
                    else:
                        print(alphabet[i], end='')
                print()       
        encode(message_input, shift_input)

    elif choice == 'decode':
        def decode(message, number):
            msg = []
            for index_message in message:
                for index_encode in range(0,len(alphabet)):
                    if index_message == alphabet[index_encode]:
                        msg.append(index_encode - number)
            for i in msg:
                print(alphabet[i], end='') 
            print()    
        decode(message_input, shift_input)
    con = input('Do you want to continue yes/no\n')
    if con == 'no':
        break                     