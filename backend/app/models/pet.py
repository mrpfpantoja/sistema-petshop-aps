class Pet:
    def __init__(self, id_pet: int, id_cliente: int, nome: str, especie: str, observacoes: str):
        self.id_pet = id_pet
        self.id_cliente = id_cliente
        self.nome = nome
        self.especie = especie
        self.observacoes = observacoes