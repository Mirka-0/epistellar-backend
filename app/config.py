import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # NASA API Configuration
    NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
    NASA_API_BASE_URL = "https://api.nasa.gov"
    
    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/Epistellar_backend")
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "myhVup-9jajqu-hyvpoc")
    
    # Application Settings
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    
    # File Paths
    DATA_RAW_PATH = "data/raw"
    DATA_PROCESSED_PATH = "data/processed"
    DATA_EMBEDDINGS_PATH = "data/embeddings"

settings = Settings()