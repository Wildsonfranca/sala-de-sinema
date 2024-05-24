import os


nome =input('Informe seu nome:')
idade =int(input('Informe sua idade : '))
idade_minima = input('')

while True:
    print('Sala 1 - Avolta dos que não foram. - 16 anos.')
    print('Sala 2 - A roda quebrada idade - 12 anos.')
    print('Sala 3 - Peira em alto mar - 14 anos.')
    print('Sala 4 - As tranças do rei careca - livre.')
    print('Sala 5 - A vingança do peixe frito.')

    sala = input('Informe a sala desejada')
    os.system('cls')


    match sala:
        case '1':
            idade_minima =16
        case '2':
            idade_minima = 12 
        case '3':
            idade_minima = 14    
        case '4':
            idade_minima = 0
        case '5':
            idade_minima = 18
        case _:
            print('sala inexistente')
    if idade >= idade_mimina:
        print('Ingresso liberado para {nome}.')
        break   
    else:
        print(f'Etrada não permitida para {nome} . Escolha outro filme ') 
        continue       
    '   


