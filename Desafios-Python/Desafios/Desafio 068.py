import random
contador = 0
print(('=-=' * 5),"VAMOS JOGAR",('=-=' * 5))
while True:
    recebe = 0
    produt = random.randint(1, 10)
    n2 = int(input('Escolha um numero de 1 a 10 :'))
    n1 = str(input('Par ou impar?'))
    logica = (n2 + produt) % 2
    print(f'A soma de {n2}(seu numero) com {produt} (numero do computador) é {n2 + produt} que é', end=' ')
    if logica == 0:
        recebe = "par"
    else:
        recebe = "impar"
    print(recebe)
    if n1 != recebe:
        break
    contador += 1

print(f'Você perdeu ;-; \nPorem  Você acertou {contador} vez(es).')







