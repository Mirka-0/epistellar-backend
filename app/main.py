from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

app = FastAPI(
    title="Epistellar API",
    description="Backend para análisis de datos espaciales de la NASA",
    version="1.0.0",
    debug=settings.DEBUG
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Epistellar API funcionando!", 
        "version": "1.0.0",
        "environment": settings.APP_ENV
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "service": "epistellar-backend",
        "database": "postgresql+neo4j"
    }

# Import routes (los crearemos después)
# from app.routes import nasa, documents