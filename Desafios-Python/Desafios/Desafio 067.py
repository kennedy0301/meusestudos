
while True:
    cont = 0
    n1 = int(input('Qual Numero você quer ver a tabuada?'))
    if n1 <= 0 :
        break
    while cont <= 10:
        print(f'{n1} x {cont} = {n1 * cont}')
        cont += 1

print('OBRIGADO!!!')
