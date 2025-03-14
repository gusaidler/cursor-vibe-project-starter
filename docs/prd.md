# Product Requirements Document (PRD)

## App Name
AI Project Starter

## App Type
Command-Line Interface (CLI)

## Overview
AI Project Starter is a Python-based tool designed to automate the generation of essential documentation for app development. 
It takes minimal user input—such as the app idea, type (e.g., web, mobile, CLI, game), and optional tech stack—and produces three markdown files: a Product Requirements Document (PRD), a Tech Stack, and Cursor’s Project Rules. 
These files guide an LLM (via Cursor or similar tools) in coding the app. 
By integrating with OpenRouter (docs: https://openrouter.ai/docs/quickstart, use OpenAI SDK), AI Project Starter offers flexibility in choosing LLM models for document generation. 

## Key Features
- **Conversational Interface**: Prompts the user with follow-up questions to refine their app idea and ensure detailed, relevant outputs.
- **Document Generation**: Creates three files:
  - prd.md: Product Requirements Document
  - tech_stack.md: Tech Stack
  - project_rules.mdc: Cursor’s Project Rules
- **LLM Integration**: Leverages OpenRouter to send prompts to an LLM and format responses into markdown.
- **Review and Edit**: Allows users to review and modify generated documents before final use.
- **Scalability**: Built to support future enhancements, like updating documents for ongoing projects.

## Functional Requirements
- **User Input**:
  - Collects the app idea, type (e.g., web, mobile, CLI, game), and optional tech stack via CLI.
  - Asks follow-up questions (e.g., key features, target audience) to refine the input.
- **Document Generation**:
  - PRD: Includes overview, features, requirements, and user stories.
  - Tech Stack: Recommends technologies based on app type and user preferences.
  - Project Rules: Provides guidelines and best practices for LLM-driven development in Cursor (docs: https://docs.cursor.com/context/rules-for-ai#rules-for-ai).

- **LLM Interaction**:
  - Sends structured prompts to OpenRouter’s API for each document.
  - Processes API responses into well-formatted markdown files.
- **Output**:
  - Saves markdown files to a user-specified directory. The PRD file is named `prd.md`, the Tech Stack file is named `tech_stack.md`, and the Project Rules file is named `project_rules.mdc`.
  - The prd and tech stack files are saved in a docs/ folder
  - The project rules file is saved in the .cursor/rules/ folder, starting with this at the beginning of the file:
    ```
    ---
    description: Project Rules for Cursor
    globs: 
    alwaysApply: true
    ---
    ```
  - Displays instructions for reviewing and editing the output.

## Non-Functional Requirements
- **Usability**: Intuitive CLI with clear prompts and minimal complexity.
- **Performance**: Fast OpenRouter API interactions to reduce wait times.
- **Security**: Secure handling of API keys (e.g., via environment variables).
- **Modularity**: Easy to extend with new document types or features.

## User Stories
- As a developer, I want to input a basic app idea and get detailed documentation to guide LLM-based coding.
- As a user, I want follow-up questions to ensure the output matches my vision.
- As a user, I want to select the LLM model via OpenRouter for flexibility.
- As a user, I want to edit generated documents before using them in Cursor.

## Acceptance Criteria
- Generates all three documents based on user input.
- Produces specific, relevant, and well-structured markdown files.
- Handles errors (e.g., invalid input, API issues) with clear feedback.
- Allows easy configuration of the OpenRouter API key.