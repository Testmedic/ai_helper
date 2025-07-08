# AI Helper for Medical Consultations

## Overview
This application helps doctors during patient consultations by listening to conversations and suggesting relevant questions to help identify medical red flags. The AI analyzes the conversation in real-time and provides contextual questions that doctors might want to ask to ensure they don't miss important diagnostic information.

## Features
- **Real-time conversation analysis**: Listens to doctor-patient conversations
- **Medical red flag detection**: Identifies potential serious conditions based on symptoms
- **Contextual question suggestions**: Provides relevant follow-up questions
- **Multiple medical conditions**: Covers chest pain, headaches, breathing difficulties, dizziness, and abdominal pain
- **Simple interface**: Easy-to-use command-line interface

## Medical Conditions Covered
- **Chest Pain**: Cardiac-related symptoms and questions
- **Headaches**: Neurological warning signs
- **Breathing Difficulties**: Respiratory distress indicators
- **Dizziness**: Balance and cardiovascular concerns
- **Abdominal Pain**: Gastrointestinal emergency signs

## Installation
```bash
# Clone the repository
git clone https://github.com/Testmedic/ai_helper.git
cd ai_helper

# Run the application
python ai_helper/ai_helper.py
```

## Usage
1. Run the application:
   ```bash
   python ai_helper/ai_helper.py
   ```

2. The application will start listening mode
3. Type conversation text as it happens
4. The AI will suggest relevant questions in real-time
5. Type 'quit' to stop

## Example Usage
```
🏥 AI Helper for Medical Consultations
=====================================
This application listens to doctor-patient conversations
and suggests relevant questions to help identify red flags.

🎤 AI Helper is now listening to the conversation...
Type conversation text or 'quit' to stop:
> Patient says I have chest pain
💡 AI Suggested Questions:
  1. On a scale of 1-10, how severe is the chest pain?
  2. Does the pain radiate to your arm, jaw, or back?
  3. Are you experiencing shortness of breath?
  4. Do you have a history of heart problems?
  5. When did the pain start?

> Patient mentions headache
💡 AI Suggested Questions:
  1. Is this the worst headache you've ever had?
  2. Are you experiencing any vision changes?
  3. Do you have a fever or neck stiffness?
  4. Are you sensitive to light?
  5. Have you had any recent head trauma?
```

## Testing
Run the test suite to verify functionality:
```bash
python ai_helper/test_ai_helper.py
```

## Architecture
- **MedicalQuestionSuggester**: Core AI logic for analyzing conversations and suggesting questions
- **ConversationListener**: Handles input processing and user interaction
- **AIHelper**: Main application controller

## Safety Notice
This application is designed to assist medical professionals and should not replace clinical judgment. All suggestions should be evaluated by qualified healthcare providers.

## Future Enhancements
- Audio input processing with speech-to-text
- Integration with medical databases
- Machine learning model for improved accuracy
- Multi-language support
- Mobile application interface
- Integration with electronic health records

## License
This project is intended for educational and research purposes in healthcare technology.