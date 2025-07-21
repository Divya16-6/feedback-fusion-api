from transformers import pipeline
from config import GEN, MODEL_NAME
from functools import lru_cache

@lru_cache(maxsize=1)
def get_classifier():
    return pipeline(GEN, model=MODEL_NAME)


def classify_feedback(feedback: str) -> str:
    classifier = get_classifier()
    prompt = f"Classify this feedback as Positive or Negative:\n\n{feedback}"
    result = classifier(prompt, max_length=10)[0]['generated_text']
    return result.strip()