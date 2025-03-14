"""
CLI module for Cursor Vibe Project Starter.

This module contains the command-line interface for the Cursor Vibe Project Starter tool.
"""

import os
import click
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from pathlib import Path
from dotenv import load_dotenv

from cursor_vibe_project_starter.config import Settings
from cursor_vibe_project_starter.generator import DocumentGenerator
from cursor_vibe_project_starter.models import AppProject, AppType

# Load environment variables from .env file
load_dotenv()

console = Console()


@click.group()
@click.version_option()
def cli():
    """Cursor Vibe Project Starter - Generate documentation for your app idea."""
    pass


@cli.command()
def generate():
    """Generate documentation for a new app project."""
    try:
        # Ensure the API key is set
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            console.print(
                "[bold red]Error:[/bold red] OPENROUTER_API_KEY not found in environment variables."
            )
            console.print("Please set it in a .env file or export it to your shell.")
            return

        settings = Settings(
            openrouter_api_key=api_key,
            openrouter_model=str(os.getenv("OPENROUTER_MODEL")),
            openrouter_api_url="https://openrouter.ai/api/v1/chat/completions",
        )

        # Interactive questionnaire
        console.print(
            Panel("[bold green]Welcome to Cursor Vibe Project Starter![/bold green]\n"
                  "I'll help you generate documentation for your app idea.")
        )
        
        # Get app details
        app_name = click.prompt("What is the name of your app?")
        app_idea = click.prompt("Describe your app idea in a few sentences")
        
        # Make app type case insensitive but display as lowercase
        app_type_options = {t.value.lower(): t for t in AppType}
        app_type_choices = list(app_type_options.keys())
        
        app_type_str = click.prompt(
            "What type of app is it?",
            type=click.Choice(app_type_choices, case_sensitive=False),
            default="web"
        ).lower()  # Convert to lowercase to match our keys
        
        app_type = app_type_options[app_type_str]
        
        tech_stack_preference = click.prompt(
            "Do you have any specific tech stack preferences? (optional)", default=""
        )
        
        # Get more details through follow-up questions - make key features mandatory
        key_features = []
        while not key_features:
            features_input = click.prompt(
                "What are the key features of your app? (comma-separated list)"
            )
            key_features = [f.strip() for f in features_input.split(",") if f.strip()]
            
            if not key_features:
                console.print("[bold yellow]Warning:[/bold yellow] At least one key feature is required.")
        
        target_audience = click.prompt("Who is the target audience?", default="")
        
        # Create folder name from app name
        folder_name = app_name.lower().replace(" ", "-")
        
        # Get output directory
        output_dir = click.prompt(
            "Where would you like to save the documentation?",
            type=click.Path(file_okay=False, resolve_path=True)
        )
        
        # Expand user directory (handle ~) and ensure absolute path
        output_dir = os.path.abspath(os.path.expanduser(output_dir))
        
        # Create the full output path with app name as folder
        full_output_path = os.path.join(output_dir, folder_name)
        
        # Create the project directories
        docs_dir = os.path.join(full_output_path, "docs")
        cursor_rules_dir = os.path.join(full_output_path, ".cursor", "rules")
        os.makedirs(docs_dir, exist_ok=True)
        os.makedirs(cursor_rules_dir, exist_ok=True)

        # Create the project object
        project = AppProject(
            name=app_name,
            idea=app_idea,
            app_type=app_type,
            tech_stack_preference=tech_stack_preference,
            key_features=key_features,
            target_audience=target_audience,
        )
        
        # Generate the documents
        generator = DocumentGenerator(settings)
        
        with console.status("[bold green]Generating documentation...[/bold green]"):
            # Generate PRD
            console.print("Generating Product Requirements Document...")
            prd_content = generator.generate_prd(project)
            prd_path = os.path.join(docs_dir, "prd.md")
            with open(prd_path, "w") as f:
                f.write(prd_content)
            
            # Generate Tech Stack
            console.print("Generating Tech Stack document...")
            tech_stack_content = generator.generate_tech_stack(project)
            tech_stack_path = os.path.join(docs_dir, "tech_stack.md")
            with open(tech_stack_path, "w") as f:
                f.write(tech_stack_content)
            
            # Generate Project Rules
            console.print("Generating Project Rules for Cursor...")
            project_rules_content = generator.generate_project_rules(project)
            project_rules_path = os.path.join(cursor_rules_dir, "project_rules.mdc")
            with open(project_rules_path, "w") as f:
                f.write(project_rules_content)
        
        # Success message with file paths
        console.print("\n[bold green]✅ Documentation successfully generated![/bold green]")
        console.print(f"📄 Product Requirements Document: [cyan]{prd_path}[/cyan]")
        console.print(f"📄 Tech Stack: [cyan]{tech_stack_path}[/cyan]")
        console.print(f"📄 Project Rules: [cyan]{project_rules_path}[/cyan]")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        raise


def main():
    """Main entry point for the CLI."""
    cli() 