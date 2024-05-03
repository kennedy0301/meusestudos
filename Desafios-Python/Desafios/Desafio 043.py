t1 = int(input('Qual é seu peso?\n(kg)...'))
t2 = float(input('E a sua altura:\n(m)...'))
imc = t1 / (t2 ** 2)
print('Seu imc é {:.2f} e você está '.format(imc), end=' ')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('no peso ideal.')
elif imc <= 30:
    print('em sobrepeso.')
elif imc <= 40:
    print('Obeso.')
else:
    print('morto.')
