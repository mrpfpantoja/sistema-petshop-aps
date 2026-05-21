class Agendamento:
    def __init__(self, id_agendamento: int, id_pet: int, data: str, status: str):
        self.id_agendamento = id_agendamento
        self.id_pet = id_pet
        self.data = data
        self.status = status