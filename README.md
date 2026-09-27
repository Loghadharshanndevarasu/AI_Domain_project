# CloudOps Command Center

A Streamlit-based operations dashboard created as an AI-domain project. The application brings operational metrics, incident triage, cloud-readiness checks, and security/DevOps indicators into a single interface.

## What it demonstrates

- Executive-style operational dashboarding
- Incident prioritization using defined rules
- Cloud readiness assessment
- Security and DevOps KPI visualization
- Interactive charts with Plotly
- Data handling with pandas
- Streamlit application structure

## Important note

The current incident analyzer is **rule-based**. It should not be described as an LLM, generative-AI, or autonomous agent system. The project is useful as a demonstration of how an operations workflow can be structured for future AI-assisted capabilities.

## Tech stack

- Python
- Streamlit
- Pandas
- Plotly

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project perspective

This project can be discussed from a Business Analyst / Project Management perspective: identify operational signals, define decision rules, surface KPIs, and design a dashboard that helps stakeholders prioritize issues.
