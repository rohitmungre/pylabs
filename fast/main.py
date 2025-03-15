from fastapi import FastAPI
from fast.apis import quotes, jokes, my_ip, palindrome

# Initialize FastAPI app
app = FastAPI()

# Include API routers
app.include_router(quotes.router)
app.include_router(jokes.router)
app.include_router(my_ip.router)
app.include_router(palindrome.router)

# Root Endpoint
def read_root():
    return {"message": "Welcome to the FastAPI Utility API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
