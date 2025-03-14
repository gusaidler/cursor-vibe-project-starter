# Cursor Vibe Project Starter

A CLI tool that automates the generation of essential documentation for app development.

## Overview

Cursor Vibe Project Starter takes minimal user input—such as the app idea, type (e.g., web, mobile, CLI, game), and optional tech stack—and produces three markdown files:
- A Product Requirements Document (PRD)
- A Tech Stack recommendation
- Cursor's Project Rules

These files are designed to guide an LLM (via Cursor or similar tools) in coding the app.

## Installation

```bash
# Clone the repository
git clone [repository-url]
cd cursor-vibe-project-starter

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with your OpenRouter API key:

```
OPENROUTER_API_KEY=your-api-key-here
```

You can get an API key from [OpenRouter](https://openrouter.ai/).

## Usage

```bash
# Run the CLI tool
python -m cursor_vibe_project_starter

# Follow the interactive prompts to generate your project documentation
```

## Features

- Conversational interface to refine your app idea
- Generation of PRD, Tech Stack, and Project Rules documents
- Integration with OpenRouter for flexible LLM model selection
- Review and edit capabilities for generated documents

## License

MIT 