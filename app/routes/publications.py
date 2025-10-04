from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from sqlalchemy.orm import Session

from app.database.postgres import get_db
from app.models.publication import Publication
from app.models.enriched_data import EnrichedPublication

router = APIRouter(prefix="/publications", tags=["publications"])


@router.get("/")
async def get_publications(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """Get all publications with pagination"""
    publications = db.query(Publication).offset(skip).limit(limit).all()
    return publications


@router.get("/{publication_id}")
async def get_publication(publication_id: str, db: Session = Depends(get_db)):
    """Get a specific publication by ID"""
    publication = db.query(Publication).filter(Publication.id == publication_id).first()
    if not publication:
        raise HTTPException(status_code=404, detail="Publication not found")
    return publication


@router.get("/{publication_id}/enriched")
async def get_enriched_publication(publication_id: str, db: Session = Depends(get_db)):
    """Get enriched data for a publication"""
    enriched = (
        db.query(EnrichedPublication)
        .filter(EnrichedPublication.publication_id == publication_id)
        .first()
    )
    if not enriched:
        raise HTTPException(status_code=404, detail="Enriched data not found")
    return enriched
