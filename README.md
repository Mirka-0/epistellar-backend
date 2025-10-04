# Epistellar Backend  
Building a Space Biology Knowledge Engine  

---

## The Problem  
Space biology research faces a critical challenge:  
- Experimental data is scattered across disparate sources, fragmented, and poorly accessible.  
- This fragmentation hinders researchers' ability to understand how organisms respond to space conditions.  
- As a result, hypothesis generation and decision-making for future missions are delayed.  

---

## The Solution  
Epistellar Backend addresses this challenge by transforming dispersed space biology data into actionable knowledge through:  

- **Automated Data Integration**: Unified processing of NASA publications and experimental data.  
- **Knowledge Graph Construction**: Neo4j-powered relationship mapping between biological entities.  
- **Semantic Search**: FAISS-powered vector similarity search across the research corpus.  
- **RESTful API**: FastAPI endpoints for data access and analysis.  

---

## Architecture  

├── app/ # FastAPI application
│ ├── core/ # Database connections & security
│ ├── models/ # Pydantic models
│ ├── routes/ # API endpoints
│ ├── services/ # Business logic & data processing
│ └── utils/ # Utilities & helpers
├── data/ # Data storage & processing pipelines
├── docker/ # Containerization setup
├── docs/ # API documentation
├── scripts/ # Data processing utilities
└── tests/ # Test suite

---

## Quick Start  

### Prerequisites  
- Python 3.11+  
- PostgreSQL 15+  
- Neo4j 5.15+  
- Docker & Docker Compose  

### Installation  

```bash
# Clone repository
git clone https://github.com/Mirka-0/epistellar-backend.git
cd epistellar-backend

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your database credentials

# Start services
docker-compose -f docker/docker-compose.yml up --build
API Access
Once running, access the API documentation:
Swagger UI: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc
Core Features
Data Processing Pipeline
PDF Extraction: Automated text extraction from NASA publications.
Entity Recognition: spaCy-based NER for biological entities.
Text Embeddings: Sentence transformers for semantic search.
Graph Population: Automated Neo4j knowledge graph construction.
API Endpoints
GET /search/semantic → Vector-based semantic search.
GET /publications/ → Research publication management.
GET /graph/entities → Knowledge graph entity exploration.
POST /admin/process-csv → CSV data integration (for Franklin's data).
Tech Stack
Backend Framework: FastAPI, Python 3.11
Databases: PostgreSQL, Neo4j
Search Engine: FAISS, Sentence Transformers
NLP Processing: spaCy, NLTK
Containerization: Docker, Docker Compose
Testing: Pytest (async tests)
Data Flow
Ingestion → NASA APIs, PDF processing, CSV imports
Processing → Text cleaning, entity extraction, embedding generation
Storage → Structured data in PostgreSQL, relationships in Neo4j
Query → REST API with semantic search capabilities
Development
  pip install -r requirements-dev.txt
  pytest
  black app/ tests/
  mypy app/
## License
MIT License - see LICENSE for details.
