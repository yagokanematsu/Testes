from abc import ABC, abstractmethod

class transporte(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

        @abstractmethod
        def __str__():
            pass

        @abstractmethod
        def mudar_capacidade(self):
            pass

        @abstractmethod
        def mudar_carga(self):
            pass

class carro(transporte):
    def __init__(self, marca, modelo, ano, capacidade):
        super().__init__(marca, modelo, ano)
        self.capacidade = capacidade

    def __str__(self):
        return f"Um {self.marca} {self.modelo} {self.ano}, com capacidade do tanque de {self.capacidade}"

    def mudar_capacidade(self):
        self.capacidade = int(input())

class caminhao(transporte):
    def __init__(self, marca, modelo, ano, carga):
        super().__init__(marca, modelo, ano)
        self.carga = carga

    def __str__(self):
        return f"Um caminhão {self.marca} {self.modelo}, {self.ano}, carregando {self.carga:.2f} kgs"
    
    def mudar_carga(self):
        self.carga = float(input())
