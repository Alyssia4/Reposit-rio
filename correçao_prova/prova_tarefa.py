from datetime import datetime
class Tarefa:
    def __init__(self,descricao, data_inicio, duracao):
        self.set_descricao(descricao)
        self.set_data_inicio(data_inicio)
        self.set_duracao(duracao)
    def set_descricao(self,descricao):
        