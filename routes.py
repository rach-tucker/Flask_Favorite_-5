from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    foods = ['pho', 'donuts', 'dark chocolate', 'various fruit smoothies', 'spinach/artichoke dip']
    return render_template('favorites.html', foods=foods)