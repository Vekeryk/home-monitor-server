from .db import db
from datetime import datetime, timezone


def get_utc_timestamp():
    return datetime.now(timezone.utc)


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=get_utc_timestamp)
