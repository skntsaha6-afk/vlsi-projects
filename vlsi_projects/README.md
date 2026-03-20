# VLSI AI Tools — EDA Automation with GPT-4

AI-powered EDA tools built by a Senior EDA Tools & Hardware Engineer at Intel.
Combining 5+ years of VLSI domain expertise with modern LLM technology.

## Problem This Solves
EDA engineers spend hours manually reading DRC reports, timing logs,
and synthesis outputs. These tools automate that analysis using GPT-4
and return structured, actionable fix recommendations in seconds.

## Projects

### Project 1 — DRC Analyzer Agent (In Progress)

**Status:** Week 3 of 8 complete

Automatically analyzes Calibre/Synopsys DRC violation reports
and suggests specific fixes using GPT-4.

**Tech Stack:**
- Python 3.11 — OOP, type hints
- OpenAI GPT-4.1-mini — analysis and fix suggestions
- JSON output — structured and parseable
- uv — package management

**How It Works:**
1. Reads DRC report file from disk
2. Extracts and counts violations by rule name using OOP
3. Sends structured summary to GPT-4 with expert system prompt
4. Returns validated JSON with severity, fix, and priority order

**Real Output:**
```json
{
  "violations": [
    {
      "rule": "METAL2_SPACING",
      "severity": "High",
      "count": 5,
      "fix": "Increase spacing between Metal2 wires to meet
              minimum design rule requirements"
    },
    {
      "rule": "METAL1_SPACING",
      "severity": "Medium",
      "count": 2,
      "fix": "Increase spacing between Metal1 wires"
    },
    {
      "rule": "VIA_OVERLAP",
      "severity": "Medium",
      "count": 2,
      "fix": "Ensure vias are properly aligned with metal layers"
    }
  ],
  "priority_fix": "METAL2_SPACING",
  "estimated_fix_time": "2-4 hours"
}
```

**Files:**
```
vlsi_projects/
├── analyzers/
│   ├── drc_analyzer_OOP.py              # Week 1 — OOP DRC parser
│   ├── gpt_drc_analyzer.py              # Week 2 — GPT-4 integration
│   └── gpt_drc_analyzer_with_prompt.py  # Week 3 — Prompt engineering
├── utils/
│   └── parser_utils.py                  # File reading utilities
└── data/
    └── drc_report.txt                   # Sample DRC report
```

**Run It:**
```bash
git clone https://github.com/your-username/AI_Projects
cd AI_Projects
uv sync
cp .env.example .env
# Add your OpenAI API key to .env
uv run python python_practice/vlsi_projects/analyzers/gpt_drc_analyzer_with_prompt.py
```

**Roadmap for Project 1:**
- [x] Week 1 — DRC Analyzer OOP class
- [x] Week 2 — OpenAI GPT-4 integration
- [x] Week 3 — Prompt engineering, structured JSON output
- [ ] Week 4 — GitHub organisation and documentation
- [ ] Week 5 — LangChain chain integration
- [ ] Week 6 — LangChain agent with tools
- [ ] Week 7 — Streamlit web UI
- [ ] Week 8 — FastAPI backend — PROJECT 1 COMPLETE

## Coming Soon

| Project | Description | Timeline |
|---|---|---|
| PDK Documentation AI | RAG system for PDK rule search | Month 3-4 |
| EDA Debug Agent | Multi-agent timing debug system | Month 4 |
| EDA Flow Automation | Full RTL-to-GDS flow orchestrator | Month 5 |

## Setup

**Requirements:**
- Python 3.11+
- uv package manager
- OpenAI API key

**Install:**
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone https://github.com/your-username/AI_Projects
cd AI_Projects
uv sync
```

**Environment:**
```bash
# Create .env file
OPENAI_API_KEY=your_key_here
```

## About
Senior EDA Tools and Hardware Engineer at Intel.
6-month journey to become an Agentic AI Engineer
specialising in VLSI/EDA domain automation.

Stack being learned: Python | LangChain | CrewAI |
LangGraph | OpenAI | RAG | ChromaDB | Streamlit | FastAPI
