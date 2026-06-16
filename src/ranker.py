"""
Resume Ranker - Ranks multiple CVs against a job description
using BERT embeddings and cosine similarity.
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class RankedCandidate:
    name: str
    resume_text: str
    score: float
    rank: int
    highlights: list

class ResumeRanker:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = None
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(model_name)
            print("[ResumeRanker] Model loaded.")
        except ImportError:
            print("[ResumeRanker] Install sentence-transformers.")

    def rank(self, job_description: str, resumes: dict) -> list[RankedCandidate]:
        """
        Rank resumes against a job description.
        Args:
            job_description: JD text
            resumes: dict of {candidate_name: resume_text}
        Returns:
            Sorted list of RankedCandidate
        """
        if not self.model:
            return self._fallback_rank(job_description, resumes)

        jd_embedding = self.model.encode([job_description], normalize_embeddings=True)
        results = []

        for name, text in resumes.items():
            cv_embedding = self.model.encode([text], normalize_embeddings=True)
            score = float(np.dot(jd_embedding, cv_embedding.T)[0][0])
            highlights = self._extract_highlights(text, score)
            results.append(RankedCandidate(
                name=name,
                resume_text=text,
                score=round(score, 3),
                rank=0,
                highlights=highlights
            ))

        results.sort(key=lambda x: x.score, reverse=True)
        for i, r in enumerate(results):
            r.rank = i + 1

        return results

    def _extract_highlights(self, text: str, score: float) -> list:
        highlights = []
        keywords = ["python", "machine learning", "leadership", "sql", "aws", "docker"]
        for kw in keywords:
            if kw.lower() in text.lower():
                highlights.append(kw.title())
        return highlights[:5]

    def _fallback_rank(self, jd: str, resumes: dict) -> list[RankedCandidate]:
        jd_words = set(jd.lower().split())
        results = []
        for name, text in resumes.items():
            cv_words = set(text.lower().split())
            score = len(jd_words & cv_words) / max(len(jd_words), 1)
            results.append(RankedCandidate(name, text, round(score, 3), 0, []))
        results.sort(key=lambda x: x.score, reverse=True)
        for i, r in enumerate(results):
            r.rank = i + 1
        return results