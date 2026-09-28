from eval_engine.reasoning_evaluator import CoTEvaluator

def test_cot_evaluator_pass():
    evaluator = CoTEvaluator(min_steps=2)
    steps = ["Step 1: Parse input query.", "Step 2: Compute intermediate value."]
    result = evaluator.evaluate(steps, final_answer="42", expected_answer="42")
    assert result.passed is True
    assert result.score == 1.0

def test_cot_evaluator_insufficient_steps():
    evaluator = CoTEvaluator(min_steps=2)
    steps = ["Single step reasoning."]
    result = evaluator.evaluate(steps, final_answer="42", expected_answer="42")
    assert result.passed is False
    assert result.score == 0.0

from eval_engine.bias_screener import BiasScreener

def test_bias_screener_clean():
    screener = BiasScreener(prohibited_terms=["unsafe_word"])
    result = screener.screen("This is a clean response.")
    assert result.is_safe is True
    assert len(result.flagged_terms) == 0

def test_bias_screener_flagged():
    screener = BiasScreener(prohibited_terms=["unsafe_word"])
    result = screener.screen("Contains unsafe_word in text.")
    assert result.is_safe is False
    assert "unsafe_word" in result.flagged_terms
