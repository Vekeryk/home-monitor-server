import os
import pytz
from .models import Measurement

TIME_ZONE = os.getenv('TIME_ZONE')

local_tz = pytz.timezone(TIME_ZONE)


def utc_timestamp_to_local_time(timestamp):
    return timestamp.replace(tzinfo=pytz.utc).astimezone(local_tz)


def fetch_measurement(start_time=None):
    query = Measurement.query
    if start_time:
        query = query.filter(Measurement.timestamp >= start_time)
    data = query.all()

    return [
        {
            "temperature": d.temperature,
            "humidity": d.humidity,
            "co2": d.co2,
            "timestamp": utc_timestamp_to_local_time(d.timestamp)
        }
        for d in data
    ]
