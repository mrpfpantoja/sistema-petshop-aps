from app.models.funcionario import Funcionario
# Filha de Funcionário (Nível 2 de herança)
class Veterinario(Funcionario):
    def __init__(self, id: int, nome: str, email: str, id_funcionario: int, cargo: str, crmv: str):
        super().__init__(id, nome, email, id_funcionario, cargo)
        self.tipo_usuario = "Veterinario"
        self.crmv = crmv