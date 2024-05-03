n1 = int(input('Digite um número:\n...'))
cont = 0
multi = 1
while cont != n1:
    cont += 1
    multi = multi * cont

    if cont == n1 :
        print("{} = {}".format(n1, multi))
    else:
        print(cont, end=' x ')
