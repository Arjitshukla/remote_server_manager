from fastapi import FastAPI
from app.database import Base, engine
from app.models import User, Server, CommandLog
from app.routers import auth, servers,ssh


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(servers.router)
app.include_router(ssh.router)

@app.get("/")
def root():
    return {"status": "API running"}
