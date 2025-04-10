import numpy as np
import random

#Cria uma matriz de números aleatórios
def matriz_aleatoria(linhas, colunas):
    mat = [[0 for _ in range(colunas)] for _ in range(linhas)]

    for l, x in enumerate(mat):
        for i in range(len(x)):
            mat[l][i] = random.randint(0,99)

    return np.array(mat)

linha = int(input("Número de linhas:\n"))
coluna = int(input("Número de colunas:\n"))
par, impar, nulo = 0, 0, 0
matriz = matriz_aleatoria(linha,coluna)

for i in matriz:
    for j in i:
        if j == 0:
            nulo+=1
        elif j%2==0:
            par+=1
        else:
            impar+=1
            
print(matriz)
print(f'\nTotal: {coluna*linha}\nPar(es): {par}\nÍmpar(es): {impar}\nNulo(s): {nulo}\n')

a=''
while a != 's' and a != 'n':
    a = input('Quer procurar algum elemento na matriz (s/n)?\n').lower()

if a == 's':
    while a != 'n':
        elemento = int(input("\nDigite o elemento que deseja encontrar na matriz:\n"))
        localizacao = np.where(matriz == elemento)
        if len(localizacao[0]) > 0:
            print(f"\nO elemento {elemento} foi encontrado nas seguintes posições:")
            for i in range(len(localizacao[0])):
                print(f"Linha {localizacao[0][i]}, Coluna {localizacao[1][i]}")
        else:
            print(f"\nO elemento {elemento} não foi encontrado na matriz.")
        a=''
        while a!= 's' and a!='n':
            a = input('\nAinda quer procurar algum elemento na matriz (s/n)?\n').lower()
    print('\nEncerrado.')
else:
    print('\nEncerrado.')