n = str('S')
n1 = media = contador = maior = menor = 0

while n != 'N':
    n1 = int(input('Digite um Numero:\n'))
    media += n1
    contador += 1
    n =str(input('Você quer continuar ?(S/N)').upper().strip()[0])

    if contador == 1:
        maior = menor = n1
    else:
        if n1 >= maior:
            maior = n1
        if n1 <= menor:
            menor: n1


print('A Media foi {}, o menor sendo {} e o maior {}.'.format(media/contador, menor,maior))
