# Career Agent Lab

A learning-focused multi-agent system that matches a candidate profile against job offers using a 3-agent LLM pipeline.

---

## What it does

The system takes a structured candidate profile and a list of job offers as input, then runs them through 3 specialized agents:

1. **Profile Agent** — loads and validates the candidate profile (skills, target roles, location, seniority, salary expectations)
2. **Filter Agent** — uses an LLM to reject clearly irrelevant jobs (wrong domain, too senior, no skill overlap)
3. **Ranking Agent** — scores each remaining job from 0 to 10 and categorizes it as `strong_match`, `stretch`, or `rejected`

The final output is a structured result grouping jobs into three categories with scores and justifications.

---

## Architecture

```
data/candidates.json + data/jobs.json
            │
            ▼
    [Profile Agent]       → CandidateProfile
            │
            ▼
    [Filter Agent]        → list of FilterDecision (keep / reject)
            │
            ▼
    [Ranking Agent]       → list of RankedJob (score + category)
            │
            ▼
    [Orchestrator]        → PipelineResult
                              ├── strong_matches
                              ├── stretch_opportunities
                              └── rejected
```

---

## Stack

| Layer | Choice |
|-------|--------|
| Language | Python 3.11+ |
| LLM | Groq — `llama-3.3-70b-versatile` (free tier) |
| LLM client | `openai` SDK (OpenAI-compatible API) |
| Data validation | `pydantic` v2 |
| Secrets | `python-dotenv` |

---

## Project structure

```
multi agent/
├── .env                      ← API key (not committed)
├── .gitignore
├── requirements.txt
├── main.py                   ← entry point
├── orchestrator.py           ← wires all agents together
├── data/
│   └── jobs.json             ← sample job offers
├── models/
│   └── schemas.py            ← all Pydantic models
└── agents/
    ├── llm_client.py         ← Groq client setup
    ├── profile_agent.py
    ├── filter_agent.py
    └── ranking_agent.py
```

---

## Setup

1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file at the root:
```
GROQ_API_KEY=your_groq_api_key_here
```
4. Add your candidate profile in `data/candidates.json` (see schema in `models/schemas.py`)
5. Run:
```bash
python main.py
```

---

## Example output

```json
{
  "strong_matches": [
    {
      "job_id": "job_001",
      "title": "ML Engineer Intern",
      "company": "BNP Paribas",
      "score": 8.5,
      "category": "strong_match",
      "justification": "Skills and domain align well with candidate profile."
    }
  ],
  "stretch_opportunities": [
    {
      "job_id": "job_003",
      "title": "NLP Engineer",
      "company": "Mistral AI",
      "score": 5.0,
      "category": "stretch",
      "justification": "Skills match but seniority required is mid-level, candidate is junior."
    }
  ],
  "rejected": []
}
```

---

## Purpose

This is a **learning project** about multi-agent system design. The goal is to understand:
- how agents communicate through typed interfaces
- how to enforce structured LLM outputs with Pydantic
- how to design modular, debuggable pipelines

> Built as part of an MSc in Artificial Intelligence at CentraleSupélec.
