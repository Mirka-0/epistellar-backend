from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from sqlalchemy.orm import Session

from app.database.postgres import get_db
from app.models.publication import Publication

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/publications")
async def search_publications(
    q: str = Query(..., description="Search query"), db: Session = Depends(get_db)
):
    """Search publications by title, abstract, or authors"""
    results = (
        db.query(Publication)
        .filter(
            Publication.title.ilike(f"%{q}%")
            | Publication.abstract.ilike(f"%{q}%")
            | Publication.authors.ilike(f"%{q}%")
        )
        .all()
    )
    return results


@router.get("/vector")
async def vector_search(
    query: str = Query(..., description="Vector search query"),
    k: int = Query(10, description="Number of results"),
):
    """Vector similarity search (to be implemented with FAISS)"""
    # TODO: Implement FAISS vector search
    return {"message": "Vector search endpoint", "query": query, "k": k}
