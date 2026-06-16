import pytest
from src.ranker import ResumeRanker, RankedCandidate

@pytest.fixture
def ranker():
    return ResumeRanker()

@pytest.fixture
def sample_data():
    jd = "Looking for a Python developer with machine learning and SQL experience."
    resumes = {
        "Alice": "Python developer with 5 years ML experience and SQL expertise.",
        "Bob": "Marketing manager with Excel and PowerPoint skills.",
        "Charlie": "Data scientist with Python, TensorFlow and SQL background.",
    }
    return jd, resumes

def test_rank_returns_list(ranker, sample_data):
    jd, resumes = sample_data
    results = ranker.rank(jd, resumes)
    assert isinstance(results, list)

def test_rank_correct_count(ranker, sample_data):
    jd, resumes = sample_data
    results = ranker.rank(jd, resumes)
    assert len(results) == 3

def test_ranks_assigned(ranker, sample_data):
    jd, resumes = sample_data
    results = ranker.rank(jd, resumes)
    ranks = [r.rank for r in results]
    assert sorted(ranks) == [1, 2, 3]

def test_top_candidate_has_highest_score(ranker, sample_data):
    jd, resumes = sample_data
    results = ranker.rank(jd, resumes)
    assert results[0].score >= results[1].score