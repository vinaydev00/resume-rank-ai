"""FastAPI endpoint for resume ranking."""

from fastapi import FastAPI
from pydantic import BaseModel
from src.ranker import ResumeRanker

app = FastAPI(title="Resume Rank AI", version="0.1.0")
ranker = ResumeRanker()

class RankRequest(BaseModel):
    job_description: str
    resumes: dict

@app.post("/rank")
def rank_resumes(request: RankRequest):
    results = ranker.rank(request.job_description, request.resumes)
    return {
        "ranked_candidates": [
            {"rank": r.rank, "name": r.name, "score": r.score, "highlights": r.highlights}
            for r in results
        ]
    }

@app.get("/health")
def health():
    return {"status": "ok", "model": "all-MiniLM-L6-v2"}