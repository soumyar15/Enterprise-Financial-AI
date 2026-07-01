from fastapi import APIRouter

router = APIRouter()


@router.get("/portfolio")

def portfolio():

    return {

        "Portfolio Value": "$150 Million",

        "Technology": "42%",

        "Healthcare": "18%",

        "Financials": "15%"
    }