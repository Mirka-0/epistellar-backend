from sqlalchemy import Column, Integer, String, Text, JSON, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Relationship(Base):
    __tablename__ = "relationships"

    id = Column(Integer, primary_key=True, index=True)
    source_entity_id = Column(Integer, ForeignKey("entities.id"))
    target_entity_id = Column(Integer, ForeignKey("entities.id"))
    relationship_type = Column(
        String, index=True
    )  # 'interacts_with', 'causes', 'treats'
    publication_id = Column(String, ForeignKey("publications.id"))
    confidence = Column(Integer)
    evidence_text = Column(Text)
    metadata = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    source_entity = relationship("Entity", foreign_keys=[source_entity_id])
    target_entity = relationship("Entity", foreign_keys=[target_entity_id])
    publication = relationship("Publication")
