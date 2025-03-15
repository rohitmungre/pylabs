from fastapi import APIRouter

router = APIRouter(prefix="/palindrome", tags=["Palindrome"])

@router.get("/{word}")
def check_palindrome(word: str):
    is_palindrome = word.lower() == word.lower()[::-1]
    return {"word": word, "is_palindrome": is_palindrome}
