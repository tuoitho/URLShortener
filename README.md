# URL Shortener 🔗
[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-v2.3.3-green.svg)](https://flask.palletsprojects.com/)

## 📋 Overview
Simple URL shortener built with Flask that converts long URLs into memorable short links.

## ⚡ Features
- Generate 6-character short codes
- Copy to clipboard functionality
- SQLite database storage
- Bootstrap 5 responsive UI

## 🔧 Tech Stack
- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, JavaScript, Bootstrap 5
- **Database**: SQLite

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener

# Set up virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python
>>> from app import db
>>> db.create_all()
>>> exit()

# Start server
python app.py