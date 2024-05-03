contidade = muiemaior = homi = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:[M/F]  ').upper())

    while sexo not in 'MF':
        print("Por favor Digite M para Maculino ou F para Feminino")
        sexo = str(input('Sexo:[M/F]  ').upper())

    if idade >= 18:
        contidade += 1
        if sexo == 'F':
            muiemaior += 1
    if sexo == 'M':
        homi += 1

    t1 = str(input('Deseja continuar?[s/n]').upper())
    while t1 not in 'SN':
        print('Por favor Digite Somente S para Sim e N para Não')
        t1 = str(input('[s/n]').upper())
    if t1 == 'N':
        break

print(f'Teve um total de {homi} homens cadastrados \n{contidade} de pessoas maioridade, sendo {muiemaior} Mulheres')
