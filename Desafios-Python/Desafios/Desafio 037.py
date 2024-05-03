t1 = int(input('Digite um numero:\n...'))
print('''Escolha uma opção de conversão:
[1] Para Binário.
[2] Para Octal.
[3] Para Hexadecimal''')
t2 = int(input('Sua Opção:'))

if t2 == 1:
    print('O seu numero {} em Binário é {}.'.format(t1, bin(t1)[2:]))
elif t2 == 2:
    print('Seu numero é {} e sua conversão é {}.'.format(t1, oct(t1)[2:]))
elif t2 == 3:
    print('seu numero é {} e sua conversão é {}.'.format(t1, hex(t1)[2:]))

