from fastapi import FastAPI
from crud_projeto import router as projeto_router

app = FastAPI(
    title="API ExpoDesign",
    version="1.0.0",
) 

app.include_router(projeto_router, prefix="/expodesign")