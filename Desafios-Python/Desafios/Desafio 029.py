t1 = int(input('Qual a velocidade de seu carro???\n...'))
if t1 > 80:
    print('Você estava a {}km/h!? Só pode estar louco!'.format(t1))
    print(' VOCÊ recebera uma multa de R${},00'.format((t1-80)*7))
else:
    print('Você esta no limite. Pode passar!')
