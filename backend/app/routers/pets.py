from fastapi import APIRouter
from app.database.db import get_db_connection
from app.schemas.schemas import PetCreate

router = APIRouter(prefix="/pets", tags=["Pets"])

@router.post("")
def cadastrar_pet(pet: PetCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Pets (id_cliente, nome, idade, especie, raca, observacoes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (pet.id_cliente, pet.nome, pet.idade, pet.especie, pet.raca, pet.observacoes))
    conn.commit()
    conn.close()
    return {"status": "Pet cadastrado com sucesso!"}