from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite : Mapped[List["Favorite"]] = relationship(
        back_populates="user"
    )
    

    
class Planet(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    film_appearance: Mapped[str] = mapped_column(String(120), nullable=False)
    exploted: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    population: Mapped[int] = mapped_column(Integer(), nullable=False)
    favorite : Mapped[List["Favorite"]] = relationship(
        back_populates="planet"
    )
    people : Mapped[List["People"]] = relationship(
        back_populates="planet"
    )


class People(db.Model):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    person_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    coalition: Mapped[str] = mapped_column(String(120), nullable=False)
    race: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    favorite : Mapped[List["Favorite"]] = relationship(
        back_populates="people"
    )
    planet_id : Mapped[int] = mapped_column (ForeignKey("planets.id"),nullable=True)
    planet : Mapped['Planet'] = relationship(
        back_populates="people"
    )


class Favorite(db.Model):
    __tablename__="favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column (ForeignKey("users.id"),nullable=False)
    planet_id : Mapped[int] = mapped_column (ForeignKey("planets.id"),nullable=True)
    people_id : Mapped[int] = mapped_column (ForeignKey("people.id"),nullable=True)
    user : Mapped['User'] = relationship(
        back_populates="favorite"
    )
    planet : Mapped['Planet'] = relationship(
        back_populates="favorite"
    )
    people : Mapped['People'] = relationship(
        back_populates="favorite"
    )

