from fastapi import APIRouter, HTTPException
from app.schemas.schemas import AgendamentoCreate
from app.facade.facade import PetShopFacade

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])
facade = PetShopFacade()

@router.post("")
def criar_agendamento(agendamento: AgendamentoCreate):
    res = facade.criar_agendamento_seguro(
        id_cliente=agendamento.id_cliente, id_pet=agendamento.id_pet,
        id_funcionario=agendamento.id_funcionario, data=agendamento.data,
        hora=agendamento.hora, valor_total=agendamento.valor_total
    )
    if not res["sucesso"]:
        raise HTTPException(status_code=400, detail=res["mensagem"])
    return res