from fastapi import FastAPI
from app.database.db import init_database
from app.routers import auth, pets, agendamentos, financeiro

app = FastAPI(title="Clinica Veterinaria APS v2", version="2.0")

# Inicializa o banco de dados criando as tabelas no boot
init_database()

# Junta os roteadores modulares das subpastas para que fiquem visíveis na API
app.include_router(auth.router)
app.include_router(pets.router)
app.include_router(agendamentos.router)
app.include_router(financeiro.router)