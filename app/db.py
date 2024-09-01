from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)


def fetch_data(start_time=None):
    query = Measurement.query
    if start_time:
        query = query.filter(Measurement.timestamp >= start_time)
    data = query.all()
    return [
        {
            "temperature": d.temperature,
            "humidity": d.humidity,
            "timestamp": d.timestamp
        }
        for d in data
    ]
