"""
Test module for AI Project Starter models.
"""

import pytest
from cursor_vibe_project_starter.models import AppType, AppProject


def test_app_type_enum():
    """Test that the AppType enum has the expected values."""
    assert AppType.WEB.value == "web"
    assert AppType.MOBILE.value == "mobile"
    assert AppType.CLI.value == "cli"
    assert AppType.GAME.value == "game"
    assert AppType.DESKTOP.value == "desktop"
    assert AppType.API.value == "api"
    assert AppType.OTHER.value == "other"


def test_app_project_model():
    """Test that the AppProject model can be created with minimal fields."""
    project = AppProject(
        name="Test App",
        idea="A test app for testing",
        app_type=AppType.WEB,
    )
    
    assert project.name == "Test App"
    assert project.idea == "A test app for testing"
    assert project.app_type == AppType.WEB
    assert project.tech_stack_preference is None
    assert project.key_features == []
    assert project.target_audience is None


def test_app_project_model_with_all_fields():
    """Test that the AppProject model can be created with all fields."""
    project = AppProject(
        name="Test App",
        idea="A test app for testing",
        app_type=AppType.WEB,
        tech_stack_preference="React, Node.js",
        key_features=["Feature 1", "Feature 2"],
        target_audience="Developers",
    )
    
    assert project.name == "Test App"
    assert project.idea == "A test app for testing"
    assert project.app_type == AppType.WEB
    assert project.tech_stack_preference == "React, Node.js"
    assert project.key_features == ["Feature 1", "Feature 2"]
    assert project.target_audience == "Developers" 