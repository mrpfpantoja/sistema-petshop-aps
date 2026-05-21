from abc import ABC
# Classe Abstrata Mãe (Nível 1 de herança)
class Usuario(ABC):
    def __init__(self, id: int, nome: str, email: str, tipo_usuario: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo_usuario = tipo_usuario