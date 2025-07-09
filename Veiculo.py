# Constantes para o estado das portas
ABERTA = 0
FECHADA = 1
TRAVADA = 2
DESTRAVADA = 3

class Veiculo:
    def __init__(self, modelo, marca, ano_fabricacao, cor, qtd_rodas, qtd_lugares, tipo_combustivel):
        self.modelo = modelo
        self.marca = marca
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor
        self.qtd_rodas = qtd_rodas
        self.qtd_lugares = qtd_lugares
        self.tipo_combustivel = tipo_combustivel
        self.velocidade = 0
        self.ligado = False

    def liga(self):
        if not self.ligado:
            self.ligado = True

    def desliga(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0

    def acelera(self, aceleracao):
        if self.ligado:
            self.velocidade += aceleracao
        else:
            print(f"{self.marca} {self.modelo} está desligado. Não pode acelerar.")

    def freia(self, aceleracao):
        if self.ligado:
            self.velocidade -= aceleracao
            if self.velocidade < 0:
                self.velocidade = 0
        else:
            print(f"{self.marca} {self.modelo} está desligado. Não pode frear.")

    def vira_direita(self):
        print('>')

    def vira_esquerda(self):
        print('<')

    def __str__(self):
        str_out = f"Modelo       : {self.modelo}\n"
        str_out += f"Marca        : {self.marca}\n"
        str_out += f"Ano         : {self.ano_fabricacao}\n"
        str_out += f"Cor         : {self.cor}\n"
        str_out += f"Rodas       : {self.qtd_rodas}\n"
        str_out += f"Lugares     : {self.qtd_lugares}\n"
        str_comb = 'Flex (' + ', '.join(self.tipo_combustivel) + ')' if len(self.tipo_combustivel) > 1 else self.tipo_combustivel[0]
        str_out += f"Combustível : {str_comb}\n"
        str_out += f"Velocidade  : {self.velocidade}\n"
        str_out += f"Ligado      : {'Sim' if self.ligado else 'Não'}\n"
        return str_out