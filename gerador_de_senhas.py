import random

numeros = ['1','2','3','4','5','6','7','8','9']
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','A','B','C','D','E','F','G','W','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char_a = [':',';','!','@','#','%','-','_','/','[',']','.']
print('gerador de senhas')
x = int(input('O número de caracteres da senha: '))
x1 = int(input('Se quiser caracteres especiais digite 1: '))
senha = ''
if x1 == 1:
    caracteres = numeros + letras + char_a
    for _ in range(x):
        a = random.choice(caracteres)
        senha+=a
else:
    caracteres = numeros + letras
    for _ in range(x):
        a = random.choice(caracteres)
        senha+=a
print(senha)
