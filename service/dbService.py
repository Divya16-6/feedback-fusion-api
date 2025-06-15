from database import configDb, model


def getProductsData():
    products = list(configDb.products_collection.find())
    return products


def addFeedback(feedback: model.feedback):
    configDb.feedback_collection.insert_one(feedback.dict(by_alias=True, exclude_none=True, exclude={"id"}))