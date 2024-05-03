sexo = str(input("Sexo:\n(M/F)...")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados incorretos, Digite Novamente:\n...")).strip().upper()[0]
print('sucess ({})'.format(sexo))







