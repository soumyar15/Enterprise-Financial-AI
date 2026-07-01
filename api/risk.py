from fastapi import APIRouter

from services.risk_service import RiskService

router = APIRouter()

service = RiskService()


@router.get("/risk")

def risk():

    return service.var()