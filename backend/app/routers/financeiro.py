from fastapi import APIRouter
from app.facade.facade import PetShopFacade

router = APIRouter(prefix="/financeiro", tags=["Financeiro"])
facade = PetShopFacade()

@router.get("/dashboard")
def obter_dashboard():
    return facade.calcular_painel_financeiro()