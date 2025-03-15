import random

numeros = ['1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9']
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','A','B','C','D','E','F','G','W','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char_a = [':',';','!','@','#','%','-','_','/','.',':',';','!','@','#','%','-','_','/','.']
print('gerador de senhas')

quantidade = int(input('O número de caracteres da senha: '))
x = int(input('Se quiser caracteres especiais digite 1: '))
senha = ''

caracteres = numeros+letras+char_a if x == 1 else numeros+letras
random.shuffle(caracteres)

for _ in range(quantidade):
    a = random.choice(caracteres)
    senha+=a

print(senha)