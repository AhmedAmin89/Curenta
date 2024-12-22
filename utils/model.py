# Define task patterns for intent recognition
from abc import ABC, abstractmethod


# Abstract base class
class NLPModel(ABC):
    INTENT_PATTERNS = {
        "add_patient": ["add a new patient", "register patient"],
        "assign_medication": ["assign medication", "prescribe"],
        "schedule_followup": ["schedule a follow-up", "follow-up"]
    }

    @abstractmethod
    def extract_intent(self, command):
        pass

    @abstractmethod
    def extract_entities(self, command):
        pass
