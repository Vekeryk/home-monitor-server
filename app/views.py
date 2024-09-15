from flask import request, jsonify
from datetime import datetime
from . import app, API_KEY
from .db import db
from .models import Measurement


@app.route('/api/measurements', methods=['POST'])
def post_temperature():
    if request.headers.get('X-API-KEY') != API_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.json
    if not data:
        return jsonify({'error': 'Invalid JSON payload'}), 400

    temperature = data.get('temperature')
    humidity = data.get('humidity')
    co2 = data.get('co2')

    if not temperature or not humidity or not co2:
        return jsonify({'error': 'No measurements provided'}), 400

    measurement = Measurement(
        temperature=data.get('temperature'),
        humidity=data.get('humidity'),
        co2=data.get('co2')
    )

    db.session.add(measurement)
    db.session.commit()

    return jsonify({'status': 'success'}), 201


@app.route('/api/status', methods=['GET'])
def get_status():
    data = {'status': 'OK', 'timestamp': datetime.now().isoformat()}
    return jsonify(data), 200
