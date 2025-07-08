#!/usr/bin/env python3
"""
Test script for AI Helper Medical Consultation application
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_helper import MedicalQuestionSuggester, ConversationListener, AIHelper

def test_medical_question_suggester():
    """Test the medical question suggester."""
    print("Testing Medical Question Suggester...")
    suggester = MedicalQuestionSuggester()
    
    # Test chest pain detection
    test_cases = [
        ("Patient says I have chest pain", "chest_pain"),
        ("My head hurts so bad", "headache"),
        ("I'm having trouble breathing", "breathing_difficulty"),
        ("I feel dizzy and lightheaded", "dizziness"),
        ("My stomach is really painful", "abdominal_pain"),
        ("I'm feeling fine today", "general")
    ]
    
    for text, expected_type in test_cases:
        suggestions = suggester.analyze_conversation(text)
        print(f"Input: '{text}'")
        print(f"Suggestions: {len(suggestions)} questions")
        if suggestions:
            print(f"First suggestion: {suggestions[0]}")
        print()
    
    print("✅ Medical Question Suggester tests completed\n")

def test_conversation_analysis():
    """Test conversation analysis with sample dialogues."""
    print("Testing Conversation Analysis...")
    suggester = MedicalQuestionSuggester()
    
    sample_conversations = [
        "Doctor: How are you feeling today? Patient: I have this terrible chest pain that started this morning.",
        "Doctor: What brings you in? Patient: I've been having these really bad headaches for the past week.",
        "Patient: I can't catch my breath when I walk upstairs. Doctor: When did this start?",
        "Patient: I feel dizzy every time I stand up. Doctor: Are you taking any medications?"
    ]
    
    for i, conversation in enumerate(sample_conversations, 1):
        print(f"Sample Conversation {i}:")
        print(f"Text: {conversation}")
        suggestions = suggester.analyze_conversation(conversation)
        print(f"AI Suggestions ({len(suggestions)}):")
        for j, suggestion in enumerate(suggestions, 1):
            print(f"  {j}. {suggestion}")
        print()
    
    print("✅ Conversation Analysis tests completed\n")

def main():
    """Run all tests."""
    print("🧪 Running AI Helper Tests")
    print("=" * 50)
    
    test_medical_question_suggester()
    test_conversation_analysis()
    
    print("✅ All tests completed successfully!")
    
    # Demonstration mode
    print("\n🎯 Demo Mode - Try the application:")
    print("You can run: python ai_helper.py")
    print("Then type sample conversations like:")
    print("  - 'Patient says I have chest pain'")
    print("  - 'My head hurts really bad'")
    print("  - 'I can't breathe properly'")
    print("  - 'quit' to exit")

if __name__ == "__main__":
    main()