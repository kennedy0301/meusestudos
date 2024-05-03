import random
a1 = str(input('Digite o primeiro nome:\n'))
a2 = str(input('Digite o segundo nome:\n'))
a3 = str(input('Digite agora o terceiro nome:\n'))
a4 = str(input('Digite o ultimo nome:\n'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista)

