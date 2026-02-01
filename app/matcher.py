def match_score(resume_text: str, job_description: str) -> int:
    r = set(resume_text.split())
    j = set(job_description.lower().split())

    overlap = r.intersection(j)
    score = int((len(overlap) / max(len(j), 1)) * 100)

    return score
