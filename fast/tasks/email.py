import time
from fastapi import BackgroundTasks

# Simulate sending an email
def send_email(email: str, message: str):
    time.sleep(2)  # Simulate delay
    print(f"📧 Email sent to {email} with message: {message}")

# Usage in API
async def trigger_email(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message)
    return {"message": "Email is being sent in the background!"}
