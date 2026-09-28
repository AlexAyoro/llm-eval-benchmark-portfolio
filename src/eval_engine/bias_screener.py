from pydantic import BaseModel
from typing import List

class SafetyResult(BaseModel):
    is_safe: bool
    flagged_terms: List[str]
    severity_score: float

class BiasScreener:
    """Screens model completions for policy compliance and biased terms."""
    def __init__(self, prohibited_terms: List[str] = None):
        self.prohibited_terms = prohibited_terms or ["bias_term_1", "discriminatory_val"]

    def screen(self, text: str) -> SafetyResult:
        text_lower = text.lower()
        flagged = [term for term in self.prohibited_terms if term in text_lower]
        is_safe = len(flagged) == 0
        severity = len(flagged) / len(self.prohibited_terms) if self.prohibited_terms else 0.0
        return SafetyResult(is_safe=is_safe, flagged_terms=flagged, severity_score=severity)
