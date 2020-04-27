from flask import render_template, redirect,url_for,request
from . import main
from ..requests import get_articles

@main.route('/',methods = ['GET','POST'])
def index():
    '''
    View root page function. It returns the index page as its data
    '''
    