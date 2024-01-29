import sys
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from models import db
from models import Hero, Power, HeroPower
from app import app

current_datetime = datetime.utcnow()


def seed_data():
    powers = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    with app.app_context():
        for power_info in powers:
            power = Power(**power_info, created_at=current_datetime, updated_at=current_datetime)
            db.session.add(power)
            db.session.commit()

        heros_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
            {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
            {"name": "Janet Van Dyne", "super_name": "The Wasp"},
            {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
            {"name": "Carol Danvers", "super_name": "Captain Marvel"},
            {"name": "Jean Grey", "super_name": "Dark Phoenix"},
            {"name": "Ororo Munroe", "super_name": "Storm"},
            {"name": "Kitty Pryde", "super_name": "Shadowcat"},
            {"name": "Elektra Natchios", "super_name": "Elektra"}
        ]

        for heros_info in heros_data:
            hero = Hero(**heros_info, created_at=current_datetime, updated_at=current_datetime)
            db.session.add(hero)
            db.session.commit()

        hero_power_data = [
            {"strength": "Weak", "power_id": 1, "hero_id": 1},
            {"strength": "Strong", "power_id": 2, "hero_id": 2},
            {"strength": "Average", "power_id": 3, "hero_id": 3},
            {"strength": "Strong", "power_id": 4, "hero_id": 4},
            {"strength": "Weak", "power_id": 1, "hero_id": 5},
            {"strength": "Average", "power_id": 2, "hero_id": 6},
            {"strength": "Strong", "power_id": 3, "hero_id": 7},
            {"strength": "Weak", "power_id": 4, "hero_id": 8},
            {"strength": "Strong", "power_id": 1, "hero_id": 9},
            {"strength": "Average", "power_id": 2, "hero_id": 10},
        ]

        for hero_power in hero_power_data:
            new_hero_power = HeroPower(**hero_power, created_at=current_datetime, updated_at=current_datetime)
            db.session.add(new_hero_power)
            db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_data()
