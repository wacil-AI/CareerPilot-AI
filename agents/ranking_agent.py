import json
from models.schemas import CandidateProfile, JobOffer, FilterDecision, RankedJob
from agents.llm_client import client

def run(profile: CandidateProfile, jobs: list[JobOffer], decisions: list[FilterDecision]) -> list[RankedJob]:
    ranked = []

    kept_jobs = [job for job in jobs if any(d.job_id == job.id and d.keep for d in decisions)]

    for job in kept_jobs:
        prompt = f"""
You are a job ranking agent.

Candidate profile:
{profile.model_dump_json(indent=2)}

Job offer:
{job.model_dump_json(indent=2)}

Score this job for the candidate from 0 to 10 and assign a category using these strict rules:

- strong_match (score 7-10): skills largely match, seniority matches, domain matches, location matches
- stretch (score 4-6): some skills match but candidate is under-qualified, seniority is higher, or domain is not ideal
- rejected (score 0-3): clear mismatch on skills, seniority far too high, or wrong domain entirely

Be honest and strict. Do not give strong_match to jobs where the candidate is clearly under-qualified.

Reply in JSON with exactly:
{{"job_id": "...", "title": "...", "company": "...", "score": 7.5, "category": "strong_match", "justification": "..."}}
"""
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        data = json.loads(response.choices[0].message.content)
        ranked.append(RankedJob(**data))

    return ranked
