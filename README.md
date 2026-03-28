# AI Code Collaboration Crew

A multi-agent AI system built using CrewAI that simulates a collaborative software engineering workflow.

## Overview

This project demonstrates how specialized AI agents can work together to:

* Generate production-ready code
* Review and optimize it
* Create comprehensive test cases

## Tech Stack

* CrewAI
* OpenAI
* Python 3.11
* uv (fast dependency manager)

## Architecture

Backend Engineer → Code Reviewer → QA Engineer

## Getting Started

### 1. Install uv

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

### 2. Setup project

```bash
uv venv --python 3.10
source .venv/bin/activate
uv add -r pyproject.toml
```

### 3. Add API Key

```bash
cp .env.example .env
```

### 4. Run

```bash
python main.py --feature "Create a function to validate email addresses"
```

## Key Features

* Multi-agent collaboration
* Memory-enabled workflows
* Modular architecture
* Extensible with tools (e.g., code execution)

## Future Improvements

* GitHub PR automation
* Code execution validation
* UI dashboard

## Resources
GROQ API Key: https://console.groq.com/keys
OPENAI API Key: https://platform.openai.com/login
GITHUB Access Token: https://github.com/settings/tokens
