from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    bots: List["TradingBot"] = Relationship(back_populates="user")
    
class TradingBot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    strategy: str
    is_active: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Foreign keys
    user_id: int = Field(foreign_key="user.id")
    
    # Relationships
    user: User = Relationship(back_populates="bots")
    trades: List["Trade"] = Relationship(back_populates="bot")

class Trade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    symbol: str
    entry_price: float
    exit_price: Optional[float] = None
    quantity: float
    side: str  # "buy" or "sell"
    status: str  # "open", "closed"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    closed_at: Optional[datetime] = None
    
    # Foreign keys
    bot_id: int = Field(foreign_key="tradingbot.id")
    
    # Relationships
    bot: TradingBot = Relationship(back_populates="trades")