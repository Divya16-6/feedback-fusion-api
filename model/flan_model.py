from transformers import pipeline
from config import GEN, MODEL_NAME

# Load the free LLM
classifier = pipeline(GEN, model=MODEL_NAME)

def classify_feedback(feedback: str) -> str:
    prompt = f"Classify this feedback as Positive or Negative:\n\n{feedback}"
    result = classifier(prompt, max_length=10)[0]['generated_text']
    return result.strip()