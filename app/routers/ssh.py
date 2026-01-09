from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Server, CommandLog
from app.dependencies import get_current_user
from app.ssh_service import execute_ssh_command
from app.email_sender.email_service import send_email

router = APIRouter(
    prefix="/ssh",
    tags=["SSH"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/execute/{server_id}")
def execute_command(
    server_id: int,
    command: str,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    server = db.query(Server).get(server_id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")

    try:
        output, error,exit_status = execute_ssh_command(
            server.host,
            server.username,
            server.password,
            command,
            port=2222
        )
         # Log to DB
        log = CommandLog(
            user_email=user,
            server_name=server.name,
            command=command,
            output=output,
            error=error
        )
        db.add(log)
        db.commit()
        subject = f"Command executed on {server.name}"
        content = f"""
        User: {user}
        Server: {server.name}
        Command: {command}
        Output: {output}
        Error: {error}
        Exit Status: {exit_status}
        """
        send_email(user, subject, content)

        return {
            "output": output,
            "error": error,
            "exit_status": exit_status,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
