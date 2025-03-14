# Example: Generating Documentation with Cursor Vibe Project Starter

This example demonstrates how to use Cursor Vibe Project Starter to generate documentation for a web application.

## Setup

First, make sure you have the Cursor Vibe Project Starter installed and your OpenRouter API key set in the `.env` file.

```bash
# Install the package
pip install -e .

# Set up the environment
cp .env.example .env
# Edit .env to add your API key
```

## Basic Usage

Run the CLI tool with the `generate` command:

```bash
python -m cursor_vibe_project_starter generate
```

You'll be prompted to enter information about your app, such as:
- App name
- App idea
- App type (web, mobile, cli, game, etc.)
- Tech stack preferences
- Key features
- Target audience

## Example Session

Here's an example interaction:

```
$ python -m cursor_vibe_project_starter generate

What is the name of your app? TaskMaster
Describe your app idea in a few sentences: A task management application that helps users organize their work and personal tasks with smart prioritization and reminders.
What type of app is it? [web/mobile/cli/game/desktop/api/other]: web
Do you have any specific tech stack preferences? (optional): React, Node.js, MongoDB
What are the key features of your app? (comma-separated list): Task creation, Priority sorting, Due dates, Reminders, Categorization
Who is the target audience?: Professionals and students who need to manage multiple tasks
Where would you like to save the documentation? ~/Documents/projects

Generating Product Requirements Document...
Generating Tech Stack document...
Generating Project Rules for Cursor...

✅ Documentation successfully generated!
📄 Product Requirements Document: /Users/username/Documents/projects/taskmaster/docs/prd.md
📄 Tech Stack: /Users/username/Documents/projects/taskmaster/docs/tech_stack.md
📄 Project Rules: /Users/username/Documents/projects/taskmaster/.cursor/rules/project_rules.mdc

Would you like to preview the generated PRD? [Y/n]: y
# Product Requirements Document (PRD)
...
```

## Output Files

The tool will generate three files:

1. `docs/prd.md` - Detailed requirements document
2. `docs/tech_stack.md` - Technology recommendations
3. `.cursor/rules/project_rules.mdc` - Guidelines for Cursor AI

These files can then be used with Cursor to help guide the development process. 