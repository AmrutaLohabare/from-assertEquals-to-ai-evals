# Session 9: DeepEval basics. Three tests from my suite: relevancy, faithfulness and a custom GEval metric.
# The actual_output values are sample answers I wrote, not live AI answers (live testing comes later).
#
# Setup:  python -m venv venv  ->  activate  ->  pip install deepeval
#         set OPENAI_API_KEY in your environment (the metrics use an AI judge); never put it in this file
# Run:    deepeval test run test_deepeval_basics.py      (rich report)
#    or:  pytest test_deepeval_basics.py                  (plain pytest, CI-friendly)

from deepeval import assert_test
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, GEval


def test_relevancy():
    test_case = LLMTestCase(
        input="What is your return policy",
        actual_output="You can return items in 30 days.",
    )
    metric = AnswerRelevancyMetric(threshold=0.7)
    assert_test(test_case, [metric])


def test_faithfulness():
    # Scored 1.00 in my run, but "12" is not in the context: Faithfulness only
    # flags claims the context CONTRADICTS. See the README.
    test_case = LLMTestCase(
        input="How many sick leaves do I get per year",
        actual_output="You are entitled for 12 sick leaves per year.",
        retrieval_context=["Sick leaves do not carry over to the next year."],
    )
    metric = FaithfulnessMetric(threshold=0.7)
    assert_test(test_case, [metric])


def test_empathy():
    empathy = GEval(
        name="Empathy",
        # In my original run the two strings joined as "...and isempathetic..."
        # (no space). The judge still understood it; the space is added here.
        criteria="Determine if the response apologizes and is "
                 "empathetic to an upset customer.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.8,
    )
    test_case = LLMTestCase(
        input="My order is 3 weeks late and I am furious!",
        actual_output="I am sorry for the delay. Let me help fix this right away.",
    )
    assert_test(test_case, [empathy])
