import json
from models.schemas import JobOffer, PipelineResult
from agents import profile_agent, filter_agent, ranking_agent

def run(candidate_path: str, jobs_path: str) -> PipelineResult:
    profile = profile_agent.run(candidate_path)

    with open(jobs_path) as f:
        jobs = [JobOffer(**item) for item in json.load(f)]

    decisions = filter_agent.run(profile, jobs)

    ranked = ranking_agent.run(profile, jobs, decisions)

    strong_matches   = [r for r in ranked if r.category == "strong_match"]
    stretch          = [r for r in ranked if r.category == "stretch"]
    rejected         = [r for r in ranked if r.category == "rejected"]

    return PipelineResult(
        strong_matches=strong_matches,
        stretch_opportunities=stretch,
        rejected=rejected
    )
