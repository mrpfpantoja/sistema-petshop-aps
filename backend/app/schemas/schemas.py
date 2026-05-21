from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    telefone: Optional[str] = None
    tipo_usuario: str # 'Cliente', 'Funcionario', 'Veterinario'
    cpf: Optional[str] = None
    residencia: Optional[str] = None
    dataNascimento: Optional[str] = None
    cargo: Optional[str] = None
    salarios: Optional[float] = 0.0
    crmv: Optional[str] = None

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

class PetCreate(BaseModel):
    id_cliente: int
    nome: str
    idade: Optional[int] = None
    especie: str
    raca: Optional[str] = None
    observacoes: str

class AgendamentoCreate(BaseModel):
    id_cliente: int
    id_pet: int
    id_funcionario: Optional[int] = None
    data: str
    hora: str
    valor_total: float