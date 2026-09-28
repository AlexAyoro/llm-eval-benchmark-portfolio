from pydantic import BaseModel
from typing import List

class EvaluationResult(BaseModel):
    score: float
    passed: bool
    feedback: str

class CoTEvaluator:
    """Evaluates multi-step reasoning outputs against target requirements."""
    def __init__(self, min_steps: int = 2):
        self.min_steps = min_steps

    def evaluate(self, reasoning_steps: List[str], final_answer: str, expected_answer: str) -> EvaluationResult:
        if len(reasoning_steps) < self.min_steps:
            return EvaluationResult(
                score=0.0,
                passed=False,
                feedback=f"Insufficient reasoning steps. Expected at least {self.min_steps}."
            )
        is_correct = final_answer.strip().lower() == expected_answer.strip().lower()
        score = 1.0 if is_correct else 0.5
        return EvaluationResult(
            score=score,
            passed=is_correct,
            feedback="Evaluation passed with valid step counts." if is_correct else "Reasoning structured well, but answer mismatched."
        )
