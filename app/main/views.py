from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function. It returns the index page as its data
    '''
    title = 'Newsbook - Your soon to be official realtime news website'
    return render_template('index.html', title = title)