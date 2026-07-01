from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Enterprise Financial AI Platform",
    description="Enterprise Multi-Agent AI Platform for Portfolio Analytics and Risk Management",
    version="1.0.0"
)


@app.get("/")
def home():
    return JSONResponse(
        {
            "application": "Enterprise Financial AI Platform",
            "version": "1.0.0",
            "status": "Running",
            "author": "Soumya Ranjan Mishra"
        }
    )


@app.get("/health")
def health():
    return JSONResponse(
        {
            "status": "Healthy"
        }
    )

from api.chat import router

app.include_router(router)