from pydantic import BaseModel, Field
from typing import Optional

# Candidate Profile

class CandidateProfile(BaseModel):
    """Structured representation of the candidate extracted from CV/LinkedIn."""
    name: str
    target_roles: list[str] = Field(description="Job titles the candidate is targeting")
    skills: list[str] = Field(description="Technical and soft skills")
    preferred_locations: list[str] = Field(description="Cities or countries preferred")
    minimum_salary: Optional[int] = Field(None, description="Minimum acceptable salary in EUR/year")
    domains: list[str] = Field(description="Industries or domains of interest e.g. AI, finance")
    seniority: str = Field(description="e.g. junior, mid, senior")
    years_of_experience: int
    constraints: dict = Field(default_factory=dict, description="Any other constraints e.g. no relocation")
    


# ─── Input: Job Offer ─────────────────────────────────────────────────────────

class JobOffer(BaseModel):
    """A single job offer loaded from the jobs dataset."""
    id: str
    title: str
    company: str
    location: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    domain: str
    required_skills: list[str]
    seniority: str
    description: str


# ─── Output: Filter Agent ─────────────────────────────────────────────────────

class FilterDecision(BaseModel):
    """Decision made by the Filter Agent for a single job offer."""
    job_id: str
    keep: bool = Field(description="True if the job passes the filter, False if rejected")
    reason: str = Field(description="Short explanation of why it was kept or rejected")


# ─── Output: Ranking Agent ────────────────────────────────────────────────────

class JobCategory(str):
    STRONG_MATCH = "strong_match"
    STRETCH = "stretch"
    REJECTED = "rejected"


class RankedJob(BaseModel):
    """A job offer after ranking, with a score and category."""
    job_id: str
    title: str
    company: str
    score: float = Field(ge=0, le=10, description="Match score from 0 to 10")
    category: str = Field(description="strong_match, stretch, or rejected")
    justification: str = Field(description="Why this score and category was assigned")


# ─── Final Output ─────────────────────────────────────────────────────────────

class PipelineResult(BaseModel):
    """Final output of the full multi-agent pipeline."""
    strong_matches: list[RankedJob]
    stretch_opportunities: list[RankedJob]
    rejected: list[RankedJob]

