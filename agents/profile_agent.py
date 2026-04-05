import json                                                                                                                       
from models.schemas import CandidateProfile                                                                                       

def run(filepath: str) -> CandidateProfile:
    with open(filepath, "r") as f:
        data = json.load(f)
    return CandidateProfile(**data)