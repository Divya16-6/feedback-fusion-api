from pydantic import BaseModel, Field

class Products(BaseModel):
    id: str = Field(..., alias="_id")
    productId: int
    productName: str
    rate: int
    isAvailable: bool
