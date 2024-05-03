import random
t1 = random.randint(1,10)
print(t1)
cont1 = 0
t2 = int(input('Estou pensando em um número de 0 a 10, adivinhe qual é:\n...'))
if t2 != t1:
    print("Tente de novo...")
    while t2 !=  t1:
        cont1 = cont1 + 1
        if  t2 < t1:
            t2 = int(input('...Mas agora um pouco mais alto:'))
        elif t2 > t1:
            t2 = int(input('Agora um pouco menos:'))
print('Você pensa como um computador, Parabens!')
print('O numero que pensei foi', t1 )
print("Você tentou: \n{}".format(cont1+1))

''''Esse é o jogo da aula 28 só que melhorado, usando as novas mecanicas...'''

