# NLP Assistant Prototype

## Overview
This project implements an NLP-based assistant to parse natural language commands related to nursing tasks, identify intent, and extract relevant entities. The assistant provides structured JSON output representing the parsed tasks.

### Key Features
- **Intent Recognition:** Identifies the type of task (e.g., `add_patient`, `assign_medication`, `schedule_followup`).
- **Entity Extraction:** Extracts relevant entities such as patient name, age, medication details, and dates.
- **Modular Design:** Uses `SpaCy` and `BERT` models for NLP tasks, encapsulated within a factory pattern for extensibility.
- **FastAPI Integration:** Provides a REST API endpoint to parse commands and return JSON responses.

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the SpaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

### Run the FastAPI Server
Start the FastAPI server to expose the `parse_command` endpoint:
```bash
uvicorn main:app --reload
```

### API Endpoint
- **Endpoint:** `/parse_command`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "command": "Add a new patient John Doe, male, 45 years old, with diabetes."
  }
  ```
- **Response:**
  ```json
  {
    "intent": "add_patient",
    "entities": {
      "name": "John Doe",
      "gender": "male",
      "age": 45,
      "condition": "diabetes"
    }
  }
  ```

### Testing Example
For local testing, you can use the following Python script:
```python
import requests

url = "http://127.0.0.1:8000/parse_command"
command = {"command": "Assign medication Paracetamol 500mg twice a day for John Doe."}
response = requests.post(url, json=command)
print(response.json())
```

## File Structure
- **`main.py`**: Contains the FastAPI application and the `NLPManager` class.
- **`requirements.txt`**: Lists project dependencies.
- **`README.md`**: Provides an overview, installation, and usage instructions.

## Project Architecture
```
project-folder/
|
├── main.py            # Core FastAPI application
├── nlp_manager.py     # Factory pattern implementation to manage NLP models
├── models/
│   ├── spacy_model.py # Implementation of NLPModel using SpaCy
│   ├── bert_model.py  # Implementation of NLPModel using BERT
│   └── base_model.py  # Abstract base class for NLP models
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

## Extensibility
- Add new models by extending the `NLPModel` abstract base class.
- Modify or add intent patterns in the `INTENT_PATTERNS` dictionary.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

