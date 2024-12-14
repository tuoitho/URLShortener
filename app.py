from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(6), unique=True, nullable=False)

def generate_short_url():
    chars = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(chars) for _ in range(6))
        if not URL.query.filter_by(short_url=short_url).first():
            return short_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    if not original_url:
        return jsonify({'error': 'No URL provided'}), 400
    
    short_url = generate_short_url()
    new_url = URL(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()
    
    return jsonify({
        'original_url': original_url,
        'short_url': f'{request.host_url}{short_url}'
    })

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url_mapping = URL.query.filter_by(short_url=short_url).first()
    if url_mapping:
        return redirect(url_mapping.original_url)
    return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)