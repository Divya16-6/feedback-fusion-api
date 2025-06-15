from fastapi import FastAPI, HTTPException
from model import flan_model
from database.model.products import Products
from database.model.feedback import FeedbackModel, UserFeedback
from service import dbService
from typing import List
import random

app = FastAPI()

@app.get("/products", response_model=List[Products])
def getProducts():
    products = dbService.getProductsData()
    for p in products:
        p["_id"] = str(p["_id"])
    return products


@app.post("/model/generation")
def modelDeclaration(input: UserFeedback):
    try:
        if (input.text is not None):
            result = flan_model.classify_feedback(input.text)
            if result:
                number = random.randint(0, 100)
                user = f"user{number:02d}"

                feedback_data = FeedbackModel(
                    productId= input.productId,
                    userId= user,
                    text=input.text,
                    feedback= result
                )
            dbService.addFeedback(feedback=feedback_data)
            if result == "Positive":
                return { "sentiment": result, "message": "Thank you! We're glad you had a good experience." }
            else:
                return { "sentiment": result, "message": "We're sorry to hear that. We'll work on improving." }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))