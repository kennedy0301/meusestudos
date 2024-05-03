t1 = float(input('Qual é o seu sálario?\nR$...'))
if t1 > 1250.00:
    print('Você recebera R$ {:.2f}, parabens!'.format(t1 + (t1*10/100)))
else:
    print('Você recebara R$ {:.2f}, parabens!'.format(t1 + (t1*15/100)))

