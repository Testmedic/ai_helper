"""
AI Helper for Medical Consultations

This package provides tools for listening to doctor-patient conversations
and suggesting relevant questions to help identify medical red flags.
"""

from .ai_helper import AIHelper, MedicalQuestionSuggester, ConversationListener

__version__ = "1.0.0"
__author__ = "AI Helper Team"
__email__ = "support@aihelper.com"

__all__ = [
    "AIHelper",
    "MedicalQuestionSuggester", 
    "ConversationListener"
]