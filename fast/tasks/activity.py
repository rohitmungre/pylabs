import time
from fastapi import BackgroundTasks

# Simulate logging user activity
def log_activity(user_id: str, action: str):
    time.sleep(1)  # Simulate log writing delay
    print(f"📝 Log: User {user_id} performed action: {action}")

# Usage in API
async def log_user_action(user_id: str, action: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(log_activity, user_id, action)
    return {"message": "User action logged asynchronously!"}
