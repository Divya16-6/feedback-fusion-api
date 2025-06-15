# Feedback Fusion API

A FastAPI-based backend service that receives user feedback, stores it in MongoDB, and evaluates sentiment using a pre-trained LLM (Flan-T5-base). Designed to work seamlessly with the Feedback Fusion UI built in Streamlit.

# Features

- Accepts and stores product feedback from users.
- Evaluates feedback sentiment using Flan-T5-base model.
- Exposes REST API endpoints for frontend integration.
- Easily extensible for future ML model upgrades.


# Tech Stack

- **Backend**: FastAPI (Python)
- **Model**: Flan-T5-base (Hugging Face Transformers)
- **Database**: MongoDB (via PyMongo)
- **Dev Tools**: Uvicorn, Pydantic

# Project Structure

feedback-fusion-backend/
├── main.py                 # FastAPI entry point
├── database/model/
|   |__ products.py
│   └── feedback.py    # Pydantic data models
|__ model
|   |__ flan_model.py  # LLM sentiment evaluation logic
├── service/
|   └── dbService.py               # MongoDB connection
└── README.md


# Installation

Clone the repository

Install the dependencies
- pip install uvicorn fastapi pydantic pymongo transformers

Run the application
- uvicorn main:app --reload