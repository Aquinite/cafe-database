from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, session
from sqlalchemy import String
from datetime import time

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Makati(db.Model):
    __tablename__ = 'makati'
    id: Mapped[int] = mapped_column(primary_key=True)
    cafe_name: Mapped[str] = mapped_column(String(150), unique=True)
    gmaps_location: Mapped[str] = mapped_column()
    days_open: Mapped[str] = mapped_column()
    opening_time: Mapped[time] = mapped_column()
    closing_time: Mapped[time] = mapped_column()
    coffee_rating: Mapped[str] = mapped_column()
    wifi_rating: Mapped[str] = mapped_column()
    outlet_rating: Mapped[str] = mapped_column()




