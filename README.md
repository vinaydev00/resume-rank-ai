# 🏆 Resume Rank AI

> BERT-powered resume ranking system that scores and ranks multiple candidates against a job description in seconds.

## Problem
HR teams manually sort through hundreds of CVs. It takes days and introduces bias.

## Solution
Resume Rank AI embeds both the JD and CVs using sentence transformers, ranks candidates by semantic similarity, and exposes results via a FastAPI endpoint.

## Quickstart
pip install -r requirements.txt
uvicorn src.api:app --reload

## API
POST /rank
{
  "job_description": "Python developer with ML experience",
  "resumes": {
    "Alice": "Python ML engineer with 5 years experience",
    "Bob": "Marketing manager"
  }
}