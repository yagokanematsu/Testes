def marca(self):
    return self.marca 

def mudar_marca(self, nova_marca):
    self.marca = nova_marca

class Transporte:
    def __init__(self, marca, modelo, ano, consumo):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.consumo = consumo
class Passeio(Transporte):
    def __init__(self, marca, modelo, ano, consumo, capacidade):
        super().__init__(marca, modelo, ano, consumo)
        self.capacidade = capacidade
    def calcular_autonomia(self):
        return self.consumo*self.capacidade
    def __str__(self):
        autonomia = self.calcular_autonomia()
        return f"Um {self.marca} {self.modelo} {self.ano}, com consumo médio de {self.consumo} km/l e capacidade do tanque de {self.capacidade} L, tem autonomia de {autonomia} km"
carro = Passeio("Honda", "Civic", 2020, 12, 50)
print(carro)

class Caminhao(Transporte):
    def __init__(self, marca, modelo, ano, consumo, carga):
        super().__init__(marca, modelo, ano, consumo)
        self.carga = carga
    def calcular_custo_viagem(self, distancia, combustivel):
        a = (distancia/self.consumo)*combustivel
        return a
    def __str__(self):
        return f"Um caminhão {self.marca} {self.modelo}, {self.ano}, com consumo de {self.consumo} km/L carregando {self.carga:.2f} kgs"
caminhao1 = Caminhao("Volvo", "FH", 2021, 4, 20000.0000000)
print(caminhao1)
print(marca(caminhao1))
mudar_marca(caminhao1, 'zzzzz')
print(marca(caminhao1))