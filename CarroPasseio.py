from Veiculo import Veiculo, ABERTA, FECHADA, TRAVADA, DESTRAVADA

class CarroPasseio(Veiculo):
    def __init__(self, modelo, marca, ano_fabricacao, cor, qtd_rodas, qtd_lugares, tipo_combustivel, qtd_portas, ar_condic, radio):
        super().__init__(modelo, marca, ano_fabricacao, cor, qtd_rodas, qtd_lugares, tipo_combustivel)
        self.qtd_portas = qtd_portas
        self.ar_condic = ar_condic
        self.radio = radio
        self.portas = [FECHADA] * qtd_portas

    def abre_porta(self, porta):
        if porta < 0 or porta >= self.qtd_portas:
            raise ValueError('Porta inválida')
        else:
            self.portas[porta] = ABERTA

    def fecha_porta(self, porta):
        if porta < 0 or porta >= self.qtd_portas:
            raise ValueError('Porta inválida')
        else:
            self.portas[porta] = FECHADA

    def trava_porta(self, porta):
        if porta < 0 or porta >= self.qtd_portas:
            raise ValueError('Porta inválida')
        else:
            self.portas[porta] = TRAVADA

    def destrava_porta(self, porta):
        if porta < 0 or porta >= self.qtd_portas:
            raise ValueError('Porta inválida')
        else:
            self.portas[porta] = DESTRAVADA

    def __str__(self):
        str_out = super().__str__()
        str_out += f"Portas      : {self.qtd_portas}\n"
        str_out += f"Ar Cond.    : {'Sim' if self.ar_condic else 'Não'}\n"
        str_out += f"Rádio       : {'Sim' if self.radio else 'Não'}\n"
        for i, estado in enumerate(self.portas):
            str_out += f"  Porta {i} : {['ABERTA', 'FECHADA', 'TRAVADA', 'DESTRAVADA'][estado]}\n"
        return str_out