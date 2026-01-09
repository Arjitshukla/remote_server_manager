from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .database import Base
from datetime import datetime,timezone

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    host = Column(String)
    username = Column(String)
    password = Column(String)


# # Jab bhi koi user SSH command run karta hai, uska record save hona chahiye, jaise:

# Kis user ne command chalayi

# Kis server par chalayi

# Kaunsi command thi

# Output kya aaya

# Error aaya ya nahi

# Kab (timestamp)

# Ye sab cheez CommandLog table me store hoti hai.


class CommandLog(Base):
    __tablename__ = "command_logs"

    id = Column(Integer, primary_key=True, index=True)

    user_email = Column(
        String,
        ForeignKey("users.email"),
        nullable=False
    )

    server_name = Column(
        String,
        ForeignKey("servers.name"),
        nullable=False
    )

    command = Column(String, nullable=False)
    output = Column(String)
    error = Column(String)

    timestamp = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        index=True
    )
