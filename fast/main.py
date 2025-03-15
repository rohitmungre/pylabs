from fastapi import FastAPI
from fast.apis import quotes, jokes, my_ip, palindrome, health, status

# Initialize FastAPI app
app = FastAPI(title="Rohit's API", version="1.0.0")

# Include API routers
app.include_router(status.router)
app.include_router(health.router)
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
