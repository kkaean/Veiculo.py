from Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, modelo, marca, ano_fabricacao, capacidade_carga_toneladas):
        super().__init__(modelo, marca, ano_fabricacao, "prata", 6, 2, ["diesel"])
        self.capacidade_carga_toneladas = capacidade_carga_toneladas
        self.carga_atual = 0

    def carregar(self, peso):
        if self.carga_atual + peso <= self.capacidade_carga_toneladas:
            self.carga_atual += peso
            print(f"Caminhão {self.modelo} carregado com {peso} toneladas. Carga atual: {self.carga_atual} ton.")
        else:
            print(f"Capacidade máxima excedida! Carga atual: {self.carga_atual} ton.")

    def __str__(self):
        str_out = super().__str__()
        str_out += f"Capacidade   : {self.capacidade_carga_toneladas} ton\n"
        str_out += f"Carga Atual : {self.carga_atual} ton\n"
        return str_out