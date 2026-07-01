from fastapi import APIRouter

from services.portfolio_service import PortfolioService

router = APIRouter()

service = PortfolioService()


@router.get("/portfolio/summary")

def summary():

    return service.get_summary()


@router.get("/portfolio/holdings")

def holdings():

    return service.get_top_holdings()