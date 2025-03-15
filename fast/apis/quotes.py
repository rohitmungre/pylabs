from fastapi import APIRouter
import random

router = APIRouter(prefix="/quotes", tags=["Quotes"])

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky"
]

@router.get("/")
def get_random_quote():
    return {"quote": random.choice(quotes)}
