n1 = int(input('Digite o Número:'))
n2 = int(input('Difite o seguimento'))
calc = n1
c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print(calc, end=" -> ")

        calc = calc + n2
        c += 1
    print('Pausa')
    mais = int(input('Quantos mais você que ver?'))
print('FIm')
print('Total:',total)