import time
from fastapi import BackgroundTasks

# Simulate data cleanup task
def cleanup_old_data():
    time.sleep(3)  # Simulate cleanup delay
    print("🗑️ Old data cleaned up!")

# Usage in API
async def start_cleanup(background_tasks: BackgroundTasks):
    background_tasks.add_task(cleanup_old_data)
    return {"message": "Cleanup task started in the background!"}
