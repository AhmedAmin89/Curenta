from utils.model import NLPModel
import spacy


class SpaCyModel(NLPModel):

    def __init__(self):
        self.spacy_model = spacy.load("en_core_web_sm")

    def extract_intent(self, command):
        for intent, patterns in self.INTENT_PATTERNS.items():
            if any(pattern in command.lower() for pattern in patterns):
                return intent
        return None

    def extract_entities(self, command):
        doc = self.spacy_model(command)
        entities = {}
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entities["name"] = ent.text
            elif ent.label_ == "DATE":
                entities["date"] = ent.text
            elif ent.label_ == "AGE":
                entities["age"] = int(ent.text.replace("years old", "").strip())
            elif "medication" in command.lower() and "mg" in ent.text:
                entities["medication"] = ent.text

        # Handle gender and conditions via keyword extraction
        if "male" in command.lower() or "female" in command.lower():
            entities[
                "gender"] = "male" if "male" in command.lower() else "female"
        if "diabetes" in command.lower():
            entities["condition"] = "diabetes"

        return entities
