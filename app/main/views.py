from flask import render_template, redirect,url_for,request
from . import main
from ..requests import get_articles

@main.route('/',methods = ['GET','POST'])
def index():
    '''
    View root page function. It returns the index page as its data
    '''
    general = get_articles('top-headlines','category=general',4)
    science = get_articles('top-headlines','category=science',4)
    technology = get_articles('top-headlines','category=technology',4)
    health = get_articles('top-headlines','category=health',4)
    entertainment = get_articles('top-headlines','category=entertainment',4)
    business = get_articles('top-headlines','category=business',4)

    query = request.args.get('query')
    if query:
        return redirect(url_for('main.search',keywords = query))
    else:
        return render_template('index.html', title = 'Home | General', general = general, science = science, technology = technology, health = health,entertainment = entertainment, business = business)

@main.route('/categories/<category_name>')
def search(keywords):
    '''
    A view function to display search results
    '''
    search_keywords = '+'.join(keywords.split(' '))
    search_results = get_articles('everything',f'q={search_keywords}',100)

    query = request.args.get('query')
    if query:
        return redirect(url_for('main.search', keywords = query))
    else:
        return render_template('search.html',results = search_results, title = f 'Search Results for {keywords}')

    