"""
Document generator module for Cursor Vibe Project Starter.

This module handles the generation of documentation using OpenRouter API.
"""

from openai import OpenAI
from typing import Dict, Any

from cursor_vibe_project_starter.config import Settings
from cursor_vibe_project_starter.models import AppProject


class DocumentGenerator:
    """
    A class that generates documentation using LLMs via OpenRouter.
    """

    def __init__(self, settings: Settings):
        """
        Initialize the DocumentGenerator with settings.
        
        Args:
            settings: Application settings including API keys and model info
        """
        self.settings = settings
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.openrouter_api_key
        )

    def _generate_content(self, prompt: str) -> str:
        """
        Generate content using the OpenRouter API.
        
        Args:
            prompt: The prompt to send to the LLM
            
        Returns:
            The generated content as a string
        """
        try:
            completion = self.client.chat.completions.create(
                model=self.settings.openrouter_model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates detailed and well-formatted markdown documentation for software projects."},
                    {"role": "user", "content": prompt}
                ]
            )
            content = completion.choices[0].message.content
            if content is None:
                return "Error: No content was generated."
            return content
        except Exception as e:
            raise Exception(f"Error generating content: {str(e)}")

    def generate_prd(self, project: AppProject) -> str:
        """
        Generate a Product Requirements Document.
        
        Args:
            project: The app project details
            
        Returns:
            The generated PRD content as a string
        """
        prompt = f"""
        Create a comprehensive Product Requirements Document (PRD) for the following app:
        
        # App Information
        - Name: {project.name}
        - Type: {project.app_type.value}
        - Description: {project.idea}
        - Key Features: {', '.join(project.key_features) if project.key_features else 'Not specified'}
        - Target Audience: {project.target_audience or 'Not specified'}
        
        The PRD should include the following sections:
        1. Overview
        2. Key Features (detailed descriptions)
        3. Functional Requirements
        4. Non-Functional Requirements
        5. User Stories
        6. Acceptance Criteria
        
        Format the document as Markdown with appropriate headers, lists, and formatting.
        Start the document with "# Product Requirements Document (PRD)" followed by "## App Name" with the app name.
        Be specific, detailed, and comprehensive.
        """
        
        return self._generate_content(prompt)

    def generate_tech_stack(self, project: AppProject) -> str:
        """
        Generate a Tech Stack document.
        
        Args:
            project: The app project details
            
        Returns:
            The generated Tech Stack content as a string
        """
        prompt = f"""
        Create a comprehensive Tech Stack document for the following app:
        
        # App Information
        - Name: {project.name}
        - Type: {project.app_type.value}
        - Description: {project.idea}
        - Key Features: {', '.join(project.key_features) if project.key_features else 'Not specified'}
        - Tech Stack Preferences: {project.tech_stack_preference or 'Not specified'}
        
        The Tech Stack document should include the following sections:
        1. Programming Language(s)
        2. Key Libraries and Frameworks
        3. Database (if applicable)
        4. Frontend Technologies (if applicable)
        5. Backend Technologies (if applicable)
        6. DevOps/Deployment
        7. Rationale for technological choices
        
        Format the document as Markdown with appropriate headers, lists, and formatting.
        Start the document with "# Tech Stack for [App Name]".
        Consider modern, well-maintained, and appropriate technologies for the type of app.
        If there are specific tech stack preferences mentioned, incorporate them if they're appropriate.
        Be specific, detailed, and provide rationale for your recommendations.
        """
        
        return self._generate_content(prompt)

    def generate_project_rules(self, project: AppProject) -> str:
        """
        Generate Project Rules for Cursor.
        
        Args:
            project: The app project details
            
        Returns:
            The generated Project Rules content as a string
        """
        prompt = f"""
        Create a set of Project Rules for Cursor AI for the following app:
        
        # App Information
        - Name: {project.name}
        - Type: {project.app_type.value}
        - Description: {project.idea}
        
        The Project Rules should include:
        1. General Guidelines for code style and organization
        2. Best Practices specific to the app type and technologies
        3. Documentation Instructions
        4. Example Rules (3-5 concrete examples of rules)
        
        The rules file should follow this exact format:
        
        ```
        ---
        description: Project Rules for Cursor
        globs: 
        alwaysApply: true
        ---
        
        ## General Guidelines
        [content here]
        
        ## Best Practices for [App Type]
        [content here]
        
        ## Documentation Instructions
        [content here]
        
        ## Example Rules
        [content here]
        ```
        
        Make the rules specific to the app type and purpose.
        Be concise but complete.
        """
        
        return self._generate_content(prompt) 