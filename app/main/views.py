from flask import render_template, redirect,url_for,request
from . import main
from ..requests import get_articles,get_sources

@main.route('/',methods = ['GET','POST'])
def index():
    '''
    View root page function. It returns the index page as its data
    '''
    general = get_articles('general')
    science = get_articles('science')
    technology = get_articles('technology')
    health = get_articles('health')
    entertainment = get_articles('entertainment')
    business = get_articles('business')

    query = request.args.get('query')
    if query:
        return redirect(url_for('main.search',keywords = query))
    else:
        return render_template('index.html', title = 'Home | General', general = general, science = science, technology = technology, health = health,entertainment = entertainment, business = business)

@main.route('/search/<keywords>')
def search(keywords):
    '''
    A view function to display search results
    '''
    search_keywords = '+'.join(keywords.split(' '))
    search_results = get_articles(f'q={search_keywords}')

    query = request.args.get('query')
    if query:
        return redirect(url_for('main.search', keywords = query))
    else:
        return render_template('search.html',results = search_results, title = '{keywords}')

    
@main.route('/categories/<category_name>')
def categories(category_name):
    '''This function renders the categories.html to display news according to the selected category
    '''
    category = get_articles(f'category={category_name}')

    query = request.args.get('query')
    if query:
        return redirect(url_for('main.search',keywords = query))
    else:
        return render_template('categories.html',category = category, title = f'Categories | {category_name}',category_name = category_name)

@main.route('/sources')
@main.route('/sources/<source_name>')
def sources(source_name=None):
    '''
    function that renders the sources page
    '''
    sources = get_sources(1000000)
    from_source = get_articles(f'sources={source_name}')

    query = request.args.get('query')
    if source_name:
        return render_template('sources.html',source_name = source_name,title=f'Sources | {source_name}',from_source=from_source)
    elif query:
        return redirect(url_for('main.search',keywords = query))
    else:
        return render_template('sources.html',title='Sources | All',sources=sources)