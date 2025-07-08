#!/usr/bin/env python3
"""
AI Helper for Medical Consultations
Listens to doctor-patient conversations and suggests relevant questions to help identify red flags.
"""

import sys
import os
import json
import time
import threading
from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MedicalQuestionSuggester:
    """Suggests relevant medical questions based on conversation analysis."""
    
    def __init__(self):
        self.red_flags = {
            "chest_pain": [
                "On a scale of 1-10, how severe is the chest pain?",
                "Does the pain radiate to your arm, jaw, or back?",
                "Are you experiencing shortness of breath?",
                "Do you have a history of heart problems?",
                "When did the pain start?"
            ],
            "headache": [
                "Is this the worst headache you've ever had?",
                "Are you experiencing any vision changes?",
                "Do you have a fever or neck stiffness?",
                "Are you sensitive to light?",
                "Have you had any recent head trauma?"
            ],
            "abdominal_pain": [
                "Where exactly is the pain located?",
                "Does the pain worsen with movement or pressure?",
                "Are you experiencing nausea or vomiting?",
                "When did you last have a bowel movement?",
                "Are you experiencing any bleeding?"
            ],
            "breathing_difficulty": [
                "Are you having trouble breathing at rest?",
                "Do you have chest pain with breathing?",
                "Are you coughing up blood?",
                "Do you have any leg swelling?",
                "Have you traveled recently?"
            ],
            "dizziness": [
                "Are you experiencing any hearing loss?",
                "Do you have chest pain or palpitations?",
                "Are you taking any new medications?",
                "Have you had any recent falls?",
                "Are you experiencing any weakness?"
            ]
        }
        
        self.general_questions = [
            "Are you currently taking any medications?",
            "Do you have any allergies?",
            "What is your medical history?",
            "Are you experiencing any other symptoms?",
            "When did these symptoms first start?"
        ]
    
    def analyze_conversation(self, conversation_text: str) -> List[str]:
        """Analyze conversation and return suggested questions."""
        conversation_lower = conversation_text.lower()
        suggested_questions = []
        
        # Check for red flag keywords
        for condition, questions in self.red_flags.items():
            keywords = self._get_keywords_for_condition(condition)
            if any(keyword in conversation_lower for keyword in keywords):
                suggested_questions.extend(questions)
                logger.info(f"Red flag detected: {condition}")
        
        # Add general questions if no specific red flags found
        if not suggested_questions:
            suggested_questions.extend(self.general_questions[:3])
        
        return list(set(suggested_questions))  # Remove duplicates
    
    def _get_keywords_for_condition(self, condition: str) -> List[str]:
        """Get keywords associated with each medical condition."""
        keywords_map = {
            "chest_pain": ["chest pain", "chest hurt", "heart pain", "cardiac", "angina"],
            "headache": ["headache", "head pain", "migraine", "head hurt"],
            "abdominal_pain": ["stomach pain", "belly pain", "abdominal", "tummy hurt"],
            "breathing_difficulty": ["breath", "breathing", "shortness", "dyspnea", "wheeze"],
            "dizziness": ["dizzy", "vertigo", "lightheaded", "faint", "spinning"]
        }
        return keywords_map.get(condition, [])

class ConversationListener:
    """Simulates listening to doctor-patient conversations."""
    
    def __init__(self, suggester: MedicalQuestionSuggester):
        self.suggester = suggester
        self.is_listening = False
        self.conversation_buffer = ""
    
    def start_listening(self):
        """Start listening to conversations."""
        self.is_listening = True
        print("🎤 AI Helper is now listening to the conversation...")
        print("Type conversation text or 'quit' to stop:")
        
        while self.is_listening:
            try:
                user_input = input("> ")
                if user_input.lower() == 'quit':
                    self.stop_listening()
                    break
                
                self.conversation_buffer += " " + user_input
                self._process_conversation_chunk(user_input)
                
            except KeyboardInterrupt:
                self.stop_listening()
                break
    
    def _process_conversation_chunk(self, text: str):
        """Process a chunk of conversation and suggest questions."""
        suggestions = self.suggester.analyze_conversation(text)
        
        if suggestions:
            print("\n💡 AI Suggested Questions:")
            for i, question in enumerate(suggestions, 1):
                print(f"  {i}. {question}")
            print()
    
    def stop_listening(self):
        """Stop listening to conversations."""
        self.is_listening = False
        print("🛑 AI Helper stopped listening.")

class AIHelper:
    """Main application class."""
    
    def __init__(self):
        self.suggester = MedicalQuestionSuggester()
        self.listener = ConversationListener(self.suggester)
    
    def run(self):
        """Run the AI Helper application."""
        print("🏥 AI Helper for Medical Consultations")
        print("=====================================")
        print("This application listens to doctor-patient conversations")
        print("and suggests relevant questions to help identify red flags.")
        print()
        
        try:
            self.listener.start_listening()
        except Exception as e:
            logger.error(f"Error running AI Helper: {e}")
            return 1
        
        return 0

def main():
    """Main entry point."""
    app = AIHelper()
    return app.run()

if __name__ == "__main__":
    sys.exit(main())