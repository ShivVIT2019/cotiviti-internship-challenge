# Agentic AI for Clinical Decision Making
### Cotiviti Internship Challenge — Topic 2
**Sivasai Atchyut Akella | MS CS AI, Binghamton University**

---

## Overview

This repository contains all deliverables for the Cotiviti Internship Challenge — Topic 2: Clinical Decision Making and Pattern Recognition in Healthcare using Agentic Generative AI.

---

## Repository Structure

```
cotiviti-internship-challenge/
├── README.md
├── report/
│   └── Agentic_AI_Clinical_Decision_Making_Report.docx
├── poc/
│   ├── cotiviti_poc.py
│   └── requirements.txt
├── presentation/
│   └── Cotiviti_Agentic_AI_Presentation.pptx
└── video/
    └── cotiviti_demo.mp4
```

---

## Deliverables

| File | Description |
|------|-------------|
| `report/` | 2-page Word report + bibliography on Agentic AI for Clinical Decision Making |
| `poc/` | Python POC — 3-agent clinical decision pipeline powered by Gemini API |
| `presentation/` | 8-slide PowerPoint presentation |
| `video/` | Video walkthrough of presentation and live POC demo |

---

## POC Demo: 3-Agent Clinical Decision Pipeline

**Agent 1 — Care Gap Detection**
Ingests patient record, analyzes against HEDIS guidelines, identifies care gaps.

**Agent 2 — Drug Interaction Check**
Reviews medications for CKD Stage 3 patient, flags contraindications and dosing concerns.

**Agent 3 — Clinical Recommendation**
Synthesizes outputs into prioritized care coordinator actions and prior auth flags.

**Human-in-the-Loop Checkpoint**
Care coordinator must approve before any action is taken.

---

## Setup & Run

### Install dependencies
```
pip3 install google-generativeai
```

### Add your Gemini API key
Open `poc/cotiviti_poc.py` and replace:
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```
Get a free key at: https://aistudio.google.com/apikey

### Run
```
python3 poc/cotiviti_poc.py
```

---

## Key Findings

- Agentic AI compresses prior authorization from 3-5 days to under 1 hour
- HEDIS-aligned care gap detection can be fully automated
- Human-in-the-loop design is essential for responsible clinical AI deployment
- Cotiviti's claims data and quality measurement assets create a unique competitive advantage

---

## Tech Stack

- Python 3.9+
- Google Gemini API (gemini-3.1-flash-lite)
- Multi-agent pipeline architecture
- HEDIS quality measure framework

---

## Contact

**Sivasai Atchyut Akella**
MS CS  AI Concentration | Binghamton University
sakella@binghamton.edu
[Portfolio](https://portfolio-nine-rho-36.vercel.app) | [GitHub](https://github.com/ShivVIT2019)
