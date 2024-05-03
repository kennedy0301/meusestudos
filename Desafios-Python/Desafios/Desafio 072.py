numeros = 'zero', 'Um','Dois', 'Três', 'Quatro',\
          'Cinco', 'seis', 'Sete', 'Oito',\
          'Nove', 'Dez'

while True:
    num = int(input('Escolha um numero de 0 a 10:'))
    if num > 10:
        print('Tente novamente', end=' ')
    else:
        break
print(f'Você digitou o numero {numeros [num]}')



