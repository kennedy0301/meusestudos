somador = cont = 0

print("Digite um numero")
while True:
    n1 = int(input('[999 para parar]...'))
    if n1 == 999:
        break
    cont += 1
    somador += n1


print(f'Você digitou {cont} numeros que somados são {somador}')