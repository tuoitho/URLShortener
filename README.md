# URL Shortener

A simple URL shortener web application built with Flask and SQLite. This application allows users to convert long URLs into short, easily shareable links.

## Features

- Shorten long URLs to 6-character codes
- Copy shortened URLs to clipboard with one click
- Permanent storage using SQLite database
- Clean and responsive Bootstrap UI

## Technologies Used

- Backend: Flask, SQLAlchemy
- Frontend: HTML, JavaScript, Bootstrap 5
- Database: SQLite

## Setup and Installation

1. Clone the repository:
```sh
git clone <your-repo-url>
cd url-shortener

2. Create a virtual environment:
```sh
python -m venv venv
source venv/bin/activate

3. Install the required packages:
```sh
pip install -r requirements.txt

4. Run the application:
```sh
python app.py

5. Open your browser and navigate to `http://localhost:5000` to view the application.

## Project Structure

├── app.py              # Main application file
├── instance/          
│   └── urls.db        # SQLite database
└── templates/
    └── index.html     # Frontend template
