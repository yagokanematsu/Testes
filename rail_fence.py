def rail_fence(mensagem, chave):
    padrao = list(range(chave[0])) + list(range(chave[0] - 2, 0, -1))
    matriz = [[] for _ in range(chave[0])]
    for i in range(len(mensagem)):
        linha_atual = padrao[i % len(padrao)]
        matriz[linha_atual].append(mensagem[i])
    mensagem_codificada = ''.join([''.join(linha) for linha in matriz])
    return mensagem_codificada
print("Olá! Bem-vindo ao nosso codificador Python usando a cifra Rail Fence.")
mensagem = input("Escreva a mensagem que você deseja codificar: ")
chave = list(map(int, input("Sua chave numérica: ").split()))
mensagem_criptografada = rail_fence(mensagem, chave)
print(f"A mensagem codificada é: {mensagem_criptografada}")
print(f"A mensagem original era: {mensagem}")
