from app.models.usuario import Usuario
# Filha de usuário
class Funcionario(Usuario):
    def __init__(self, id: int, nome: str, email: str, id_funcionario: int, cargo: str):
        super().__init__(id, nome, email, "Funcionario")
        self.id_funcionario = id_funcionario
        self.cargo = cargo