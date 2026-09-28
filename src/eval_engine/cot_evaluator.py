"""Chain-of-Thought (CoT) evaluation module for reasoning models."""

from typing import Dict, Any

class CoTEvaluator:
    """Evaluates multi-step logical reasoning and accuracy in LLM responses."""

    def __init__(self, rubric_version: str = "1.0.0"):
        self.rubric_version = rubric_version

    def evaluate_step(self, step_text: str, expected_logic: str) -> Dict[str, Any]:
        """Evaluates a single reasoning step against ground truth."""
        is_valid = expected_logic.strip().lower() in step_text.strip().lower()
        return {
            "step_text": step_text,
            "is_valid": is_valid,
            "score": 1.0 if is_valid else 0.0
        }
