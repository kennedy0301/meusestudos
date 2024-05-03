num = cont = soma = 0
num = int(input('digite um numero(999 parra parar)'))

while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um numero(999 parra parar)'))
print("A soma entre eles é {} e você digitou {} vezes".format(soma, cont))