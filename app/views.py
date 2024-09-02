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
    if not data or not data.get('temperature') or not data.get('humidity'):
        return jsonify({'error': 'No measurements provided'}), 400

    measurement = Measurement(
        temperature=data.get('temperature'),
        humidity=data.get('humidity')
    )

    db.session.add(measurement)
    db.session.commit()

    return jsonify({'status': 'success'}), 201


@app.route('/api/status', methods=['GET'])
def get_status():
    data = {'status': 'OK', 'timestamp': datetime.now().isoformat()}
    return jsonify(data), 200
