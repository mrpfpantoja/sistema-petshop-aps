from app.database.db import get_db_connection

class PetShopFacade:
    def verificar_trava_dia(self, id_pet: int, data_alvo: str) -> bool:
        """Regra de Negócio: Bloqueia agendamento se o pet tiver cancelamento hoje."""
        conn = get_db_connection()
        cursor = conn.cursor()
        resultado = cursor.execute(
            "SELECT COUNT(*) FROM Agendamentos WHERE id_pet = ? AND data = ? AND status = 'Cancelado'",
            (id_pet, data_alvo)
        ).fetchone()[0]
        conn.close()
        return resultado > 0

    def criar_agendamento_seguro(self, id_cliente: int, id_pet: int, id_funcionario: int, data: str, hora: str, valor_total: float):
        if self.verificar_trava_dia(id_pet, data):
            return {"sucesso": False, "mensagem": "Este animal possui um serviço cancelado hoje. Nova marcação bloqueada."}
            
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Agendamentos (id_cliente, id_pet, id_funcionario, data, hora, status, valor_total)
            VALUES (?, ?, ?, ?, ?, 'Agendado', ?)
        """, (id_cliente, id_pet, id_funcionario, data, hora, valor_total))
        conn.commit()
        conn.close()
        return {"sucesso": True, "mensagem": "Agendamento registrado via Facade!"}

    def calcular_painel_financeiro(self):
        """Regra de Negócio: Faturamento Flutuante em tempo real."""
        conn = get_db_connection()
        cursor = conn.cursor()
        faturamento_atual = cursor.execute("SELECT TOTAL(valor_total) FROM Agendamentos WHERE status = 'Concluido'").fetchone()[0]
        previa_fechamento = cursor.execute("SELECT TOTAL(valor_total) FROM Agendamentos WHERE status != 'Cancelado'").fetchone()[0]
        conn.close()
        return {
            "faturamento_atual": faturamento_atual,
            "previa_fechamento": previa_fechamento,
            "lucro_estimado": previa_fechamento * 0.45
        }