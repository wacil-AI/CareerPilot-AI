import json                                                                                                                       
from models.schemas import CandidateProfile, JobOffer, FilterDecision
from agents.llm_client import client
                                                                                                                                
def run(profile: CandidateProfile, jobs: list[JobOffer]) -> list[FilterDecision]:
    decisions = []

    for job in jobs:
        prompt = f"""
You are a job filter agent.

Candidate profile:
{profile.model_dump_json(indent=2)}

Job offer:
{job.model_dump_json(indent=2)}

Should this candidate apply to this job?
Keep the job (keep: true) if there is ANY reasonable fit — even partial. This includes stretch opportunities where the candidate is slightly under-qualified.
Only reject (keep: false) if there is clearly no overlap at all (wrong domain, completely missing skills, or way too senior).
Reply in JSON with exactly:
{{"job_id": "...", "keep": true or false, "reason": "..."}}
"""
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        data = json.loads(response.choices[0].message.content)
        decisions.append(FilterDecision(**data))

    return decisions

