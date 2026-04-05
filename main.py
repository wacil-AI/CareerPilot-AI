import json                                                                                                                       
import orchestrator

result = orchestrator.run(
    candidate_path="data/candidates.json",
    jobs_path="data/jobs.json"
)

print(json.dumps(result.model_dump(), indent=2))