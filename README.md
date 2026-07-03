# 🤖 AI Code Collaboration Crew

A multi-agent AI system built with **CrewAI** that simulates how a real software engineering team collaborates to build software.

Instead of relying on a single AI model, this project assigns different responsibilities to specialized AI agents. Together, they generate code, review its quality, and create test cases to produce reliable, production-ready solutions.

---

## 📖 Overview

Building software is a collaborative process. Developers write code, reviewers improve it, and QA engineers test it before release.

This project recreates that workflow using AI agents.

Each agent has a dedicated responsibility, allowing them to work together just like members of a real engineering team.

The result is a structured AI workflow that demonstrates how multi-agent collaboration can improve software development.

---

## ✨ Key Features

- 🤖 Multi-agent collaboration powered by CrewAI
- 💻 Generates production-ready code
- 🔍 Reviews and improves generated code
- 🧪 Creates comprehensive test cases
- 🧠 Memory-enabled workflows
- 🏗️ Modular and maintainable architecture
- 🔌 Easily extensible with additional tools (e.g., code execution)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **CrewAI** | Multi-agent orchestration |
| **OpenAI** | AI-powered reasoning and code generation |
| **Python 3.11** | Core programming language |
| **uv** | Fast dependency and environment management |

---

## 🏗️ Architecture

The project follows a simple three-stage workflow.

```text
Feature Request
      │
      ▼
👨‍💻 Backend Engineer
      │
      ▼
🔍 Code Reviewer
      │
      ▼
🧪 QA Engineer
      │
      ▼
✅ Production-Ready Code + Test Cases
```

### Agent Responsibilities

| Agent | Responsibility |
|-------|----------------|
| 👨‍💻 Backend Engineer | Implements the requested feature by generating production-ready code. |
| 🔍 Code Reviewer | Reviews the generated code, identifies improvements, and suggests best practices. |
| 🧪 QA Engineer | Generates comprehensive test cases to validate the implementation. |

---

# 🚀 Getting Started

## 1. Install `uv`

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

---

## 2. Set Up the Project

Create a virtual environment.

```bash
uv venv --python 3.10
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install the project dependencies.

```bash
uv add -r pyproject.toml
```

---

## 3. Configure Your API Key

Copy the example environment file.

```bash
cp .env.example .env
```

Open the `.env` file and add your OpenAI API key.

---

## 4. Run the Project

```bash
python main.py --feature "Create a function to validate email addresses"
```

---

## 💡 Example Workflow

Suppose you request the following feature:

```text
Create a function to validate email addresses
```

The AI agents collaborate as follows:

```text
Backend Engineer
        │
        ▼
Generates the Implementation
        │
        ▼
Code Reviewer
        │
        ▼
Reviews & Optimizes the Code
        │
        ▼
QA Engineer
        │
        ▼
Generates Test Cases
```

---

## 📂 Why This Project?

This project demonstrates how multiple AI agents can collaborate to solve software engineering tasks more effectively than relying on a single agent.

It serves as a practical example for learning:

- CrewAI
- Multi-agent AI systems
- AI-assisted software engineering
- Collaborative AI workflows

---

## 🔮 Future Improvements

- GitHub Pull Request automation
- Code execution validation
- Interactive UI dashboard

---

## 🙌 Acknowledgements

Built with:

- CrewAI
- OpenAI
- Python
- uv

Special thanks to the open-source community for building the tools and frameworks that make projects like this possible.
