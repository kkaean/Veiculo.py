from Veiculo import Veiculo

class CarroCorrida(Veiculo):
    def __init__(self, modelo, marca, ano_fabricacao, cor, aerofolio, suspensao_ativa, controle_tracao, velocidade_maxima):
        super().__init__(modelo, marca, ano_fabricacao, cor, 4, 1, ['gasolina'])
        self.aerofolio = aerofolio
        self.suspensao_ativa = suspensao_ativa
        self.controle_tracao = controle_tracao
        self.velocidade_maxima = velocidade_maxima

    def ajusta_aerofolio(self):
        pass

    def mapeamento_motor(self):
        pass

    def veloc_max(self, vel):
        if self.ligado:
            self.velocidade = min(vel, self.velocidade_maxima)
        else:
            print(f"{self.marca} {self.modelo} está desligado. Não pode definir velocidade.")

    def __str__(self):
        str_out = super().__str__()
        str_out += f"Aerofólio   : {'Sim' if self.aerofolio else 'Não'}\n"
        str_out += f"Suspensão   : {'Ativa' if self.suspensao_ativa else 'Padrão'}\n"
        str_out += f"Tração      : {'Com controle' if self.controle_tracao else 'Sem controle'}\n"
        str_out += f"Vel. Máx.   : {self.velocidade_maxima}\n"
        return str_out