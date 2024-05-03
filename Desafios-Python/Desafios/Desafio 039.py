t1 = int(input('Em que ano você nasceu?'))
n1 = 2020 -t1
if n1 < 18:
    print('Você ainda não tem idade o bastante para se alistar.')
    print('Ainda falta {} anos para isso. '.format(18-n1))
elif n1 > 18 :
    print('Seu ano de alistamento ja passou!')
    print('Você devia ter se alistado a {} anos atrás'.format(n1 - 18))
else:
    print('''Seu alistamento é agora!!!
    Vá fazelo rápido!!!''')






