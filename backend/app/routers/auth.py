from fastapi import APIRouter, HTTPException, status
from app.database.db import get_db_connection
from app.schemas.schemas import UsuarioCreate, LoginRequest
import sqlite3

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/cadastro")
def registrar_usuario(user: UsuarioCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Usuarios (nome, email, senha, telefone, tipo_usuario)
            VALUES (?, ?, ?, ?, ?)
        """, (user.nome, user.email, user.senha, user.telefone, user.tipo_usuario))
        id_usuario = cursor.lastrowid

        if user.tipo_usuario == "Cliente":
            cursor.execute("""
                INSERT INTO Clientes (id_usuario, cpf, residencia, dataNascimento)
                VALUES (?, ?, ?, ?)
            """, (id_usuario, user.cpf, user.residencia, user.dataNascimento))
        else:
            cursor.execute("""
                INSERT INTO Funcionarios (id_usuario, cargo, salarios, crmv, dataNascimento)
                VALUES (?, ?, ?, ?, ?)
            """, (id_usuario, user.cargo, user.salarios, user.crmv, user.dataNascimento))
        conn.commit()
        return {"status": "Sucesso", "id_usuario": id_usuario}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Documento ou e-mail duplicado.")
    finally:
        conn.close()

@router.post("/login")
def login(req: LoginRequest):
    conn = get_db_connection()
    cursor = conn.cursor()
    user = cursor.execute(
        "SELECT id, nome, email, tipo_usuario FROM Usuarios WHERE email = ? AND senha = ?",
        (req.email, req.senha)
    ).fetchone()
    conn.close()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Acesso negado.")
    return {"user_id": user["id"], "nome": user["nome"], "role": user["tipo_usuario"]}