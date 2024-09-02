# HomeMonitor

Server-side application built with Flask that supports an ESP32 microcontroller in monitoring and displaying temperature and humidity data. The data collected by the ESP32 is transmitted to this server, where it is stored in a SQLite database and visualized using Dash. This repository contains the server code, while the ESP32 sketch responsible for data collection can be found in the [ESP32-Projects](https://github.com/Vekeryk/esp32-projects) repository.

## Features

- Microcontroller measurements monitoring.
- Data storage in SQLite.
- Dashboard for visualizing data over various time periods.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Create a .env file in the project root:

```
FLASK_DEBUG=1
API_KEY=YOUR_API_KEY
TIME_ZONE=Europe/Kyiv
```

## Running the Application

```bash
flask run -h 0.0.0.0
```

## Running with Docker

```bash
docker build -t home-monitor .
docker run -d -p 5000:5000 -v $(pwd)/instance:/app/instance --restart unless-stopped --name home-monitor home-monitor
```

Access the dashboard at http://localhost:5000/dashboard/.
