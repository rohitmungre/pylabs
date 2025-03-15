from fastapi import APIRouter
import random

router = APIRouter(prefix="/jokes", tags=["Jokes"])

jokes = [
    "Why don’t programmers like nature? It has too many bugs!",
    "Why do Java developers wear glasses? Because they don’t see sharp!",
    "What is a programmer’s favorite hangout place? The Foo Bar.",
    "How many programmers does it take to change a light bulb? None, that’s a hardware problem!"
]

@router.get("/")
def get_random_joke():
    return {"joke": random.choice(jokes)}
