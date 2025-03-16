from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fast.apis import quotes, jokes, my_ip, palindrome, health, status, tasks

# Initialize FastAPI app
app = FastAPI(
    title="Rohit's API",
    description="A simple FastAPI project with multiple endpoints.",
    version="1.0.0",
    docs_url="/api/docs",  # Custom path for Swagger UI
    redoc_url="/api/redoc",  # Custom path for ReDoc
)

# Include API routers
app.include_router(status.router)
app.include_router(health.router)
app.include_router(quotes.router)
app.include_router(jokes.router)
app.include_router(my_ip.router)
app.include_router(palindrome.router)
app.include_router(tasks.router)

# Root Endpoint
def read_root():
    return {"message": "Welcome to the FastAPI Utility API!"}

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Oops! Something went wrong.", "details": exc.detail},
    )


@app.get("/openapi.json")
def get_openapi():
    return app.openapi()


@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down FastAPI...")
    

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"error": "This route does not exist! Check API docs."},
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
