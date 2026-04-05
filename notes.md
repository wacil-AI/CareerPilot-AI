# Career Agent Lab

---

## Progress — Session 1 (2026-04-05)

### Done
- Project structure created: `data/`, `models/`, `agents/`
- `.env`, `.gitignore`, `requirements.txt` set up
- Stack: Groq (free LLM) + `openai` SDK + `pydantic`
- `models/schemas.py` — all Pydantic models defined
- `data/candidates.json` — real candidate profile from CV
- `data/jobs.json` — 6 sample jobs (mix of matches, stretches, rejects)
- `agents/llm_client.py` — Groq client via OpenAI-compatible API
- `agents/profile_agent.py` — reads and validates candidate JSON
- `agents/filter_agent.py` — LLM filters jobs per candidate
- `agents/ranking_agent.py` — LLM scores and categorizes kept jobs
- `orchestrator.py` — wires all 3 agents together
- `main.py` — entry point, pipeline runs successfully

### First result
Pipeline ran end-to-end. Correctly identified `job_001` (BNP ML Intern) and `job_002` (Inria DL Research) as strong matches.

### V1 status: COMPLETE ✅

All agents work correctly. Final output example:
- strong_match: BNP Paribas ML Intern, Inria DL Research Intern
- stretch: Mistral AI NLP Engineer, Airbus AI Research Intern
- filtered out: SG Quant Analyst (too senior), Leboncoin Backend Dev (wrong domain)

---

## Project name
Career Agent Lab

## Project purpose
This project is a learning-first multi-agent system designed to help a user find and rank relevant job opportunities based on:
- CV
- LinkedIn profile
- optionally GitHub projects

The long-term vision is to evolve this into a reusable multi-agent business system that could later be adapted for other enterprise workflows.

However, the current goal is **not** to build a full production platform.
The current goal is to:
1. learn how to design multi-agent systems,
2. build a small but clean MVP,
3. understand orchestration, tool usage, structured outputs, and evaluation.

---

## Core philosophy
Keep the system:
- small,
- modular,
- easy to reason about,
- easy to debug,
- strongly typed,
- based on structured outputs.

Do **not** over-engineer the first version.
Do **not** add too many agents too early.
Prefer a simple and understandable architecture over a “fancy” one.

---

## High-level product idea
The system takes as input:
- a CV,
- a LinkedIn profile summary or exported text,
- optionally GitHub profile/project data,
- user preferences.

The system then helps identify relevant job opportunities according to:
- target roles,
- geography,
- minimum salary,
- domain,
- prestige,
- career value,
- realistic fit.

The system must separate:
- strong matches,
- stretch opportunities,
- rejected opportunities with reasons.

---

## Important constraint for this project
This is primarily a **learning project about multi-agent systems**.

So every architecture decision should favor:
- clarity,
- observability,
- modularity,
- simplicity,
- educational value.

When in doubt, reduce complexity.

---

## Scope for V1
The first version should be intentionally small.

### V1 goal
Build a minimal multi-agent workflow that:
1. reads a structured candidate profile,
2. reads a small set of job offers from local JSON or CSV,
3. filters them based on user preferences,
4. ranks the remaining offers,
5. returns structured results.

### V1 must NOT include
- real web scraping,
- LinkedIn automation,
- browser control,
- full UI,
- authentication,
- databases,
- email sending,
- CV rewriting,
- outreach automation.

Those can come later.

---

## Why V1 is small
The goal of V1 is to learn:
- how agents communicate,
- how to design state,
- how to define responsibilities,
- how to enforce JSON outputs,
- how to evaluate agent behavior.

It is better to have a tiny system that works well than a large fragile prototype.

---

## Recommended architecture for V1
Use a very small multi-agent system:

### Agent 1: Profile Agent
Responsibility:
- take CV / LinkedIn / GitHub-derived information,
- normalize it into a structured candidate profile.

Output:
```json
{
  "target_roles": [],
  "skills": [],
  "preferred_locations": [],
  "minimum_salary": null,
  "domains": [],
  "seniority": "",
  "constraints": {}
}