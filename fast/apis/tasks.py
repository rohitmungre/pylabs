from fastapi import APIRouter, BackgroundTasks
from fast.tasks.email import trigger_email
from fast.tasks.activity import log_user_action
from fast.tasks.cleanup import start_cleanup

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/send-email")
async def send_email(email: str, message: str, background_tasks: BackgroundTasks):
    return await trigger_email(email, message, background_tasks)

@router.post("/log-activity")
async def log_activity(user_id: str, action: str, background_tasks: BackgroundTasks):
    return await log_user_action(user_id, action, background_tasks)

@router.post("/cleanup")
async def cleanup(background_tasks: BackgroundTasks):
    return await start_cleanup(background_tasks)
