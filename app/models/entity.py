from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    entity_type = Column(
        String, index=True
    )  # 'gene', 'disease', 'chemical', 'organism'
    normalized_id = Column(String)  # UMLS, MeSH, NCBI Gene ID, etc.
    source = Column(String)  # 'frank', 'nlp', 'manual'
    metadata = Column(JSON)
    count = Column(Integer, default=1)  # Frequency count
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
