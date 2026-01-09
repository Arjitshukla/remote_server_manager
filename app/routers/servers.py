#  Server Router banao
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Server
from app.dependencies import get_current_user
from app.schemas import ServerCreate

router = APIRouter(
    prefix="/servers",
    tags=["Servers"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_server(
    server: ServerCreate,          
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_server = Server(
        name=server.name,
        host=server.host,
        username=server.username,
        password=server.password
    )
    db.add(new_server)
    db.commit()
    return {"message": "Server added successfully"}

@router.get("/")
def list_servers(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Server).all()

@router.delete("/{server_id}")
def delete_server(
    server_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    server = db.query(Server).get(server_id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    db.delete(server)
    db.commit()
    return {"message": "Server deleted"}
