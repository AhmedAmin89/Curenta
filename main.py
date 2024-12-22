from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from utils.nlp_manager import NLPManager

# FastAPI app
app = FastAPI()

# Initialize NLP Manager with default model (SpaCy)
nlp_manager = NLPManager(model_type="bert")


# Request schema
class CommandRequest(BaseModel):
    command: str


@app.post("/parse_command")
async def parse_command(request: CommandRequest):
    command = request.command
    if not command:
        raise HTTPException(status_code=400, detail="Command is missing.")

    # Extract intent and entities
    intent = nlp_manager.extract_intent(command)
    entities = nlp_manager.extract_entities(command)

    if not intent:
        raise HTTPException(status_code=400,
                            detail="Unable to determine intent.")

    return {
        "intent": intent,
        "entities": entities
    }


# Example testing in interactive mode
if __name__ == "__main__":
    test_command = "Add a new patient John Doe, male, 45 years old, with diabetes."
    intent = nlp_manager.extract_intent(test_command)
    entities = nlp_manager.extract_entities(test_command)
    print(json.dumps({"intent": intent, "entities": entities}, indent=2))
