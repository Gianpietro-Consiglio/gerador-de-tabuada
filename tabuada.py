import time
while True:
    c = 0
    tabuada = int(input('Tabuada a ser gerada: '))
    print('')
    while c < 10:
        c += 1
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('')  
    time.sleep(2)
    x = int(input('[1- Continuar / 2- Sair]: '))
    print('')
    if x == 2:
        print('Obrigado por utilizar o programa!')
        time.sleep(2)
        break    
