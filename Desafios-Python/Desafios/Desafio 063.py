n = int(input('Quantod termos você deseja ver?'))
t1 = 0
t2 = 1
t3 = 0
cont = 1
while cont <= n:
    t3 = t1 + t2
    print(t1, end= " -> ")
    t1 = t2
    t2 = t3
    t3 = t1
    cont += 1

print('Fim')
