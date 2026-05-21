from app.models.usuario import Usuario
# Filha de usuário
class Cliente(Usuario):
    def __init__(self, id: int, nome: str, email: str, id_cliente: int, cpf: str):
        super().__init__(id, nome, email, "Cliente")
        self.id_cliente = id_cliente
        self.cpf = cpf