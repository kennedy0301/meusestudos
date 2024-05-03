n1 = int(input('Primeiro numero:\n...'))
n2 = int(input('Digite o segundo Numero:\n...'))
t1 = 0

while t1 != 5:
    if t1 == 1:
        print("A soma entre {} e {} resulta em {}".format(n1, n2, (n1 + n2)))
    elif t1 == 2:
        print('A multiplicação de {} e {} resulta em {}'.format(n1, n2,(n1 * n2)))
    elif t1 == 3:
        if n1 > n2:
            print("O numero {} é maior que {}".format(n1,n2))
        elif n1 < n2:
            print('O numero {} é maior que {}'.format(n2,n1))
        else:
            print('Não tem maior ou menor, ambos são iguais {} = {}'.format(n1,n2))
    elif t1 == 4:
        n1 = int(input('Primeiro numero:\n...'))
        n2 = int(input('Digite o segundo Numero:\n...'))

    print('=-='*8)
    print('[1] soma \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] acabar o progrma')
    print('=-=' * 8)
    t1 = int(input('Qual opção?'))

print('Obrigado pela preferencia')