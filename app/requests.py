import urllib.request,json
from .models import NewsSourceModel,NewsArticleModel,NewsGeneralModel


base_url=None

def request_config(app):
    global api_key,base_url,article_url
    article_url = app.config['ARTICLE_URL']
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    print(api_key)
def get_articles(id):
    '''
    function that gets the json response from newsapi
    '''
    news_articles_url=article_url.format(id,api_key)
    print(news_articles_url)
    with urllib.request.urlopen(news_articles_url) as url:
        news_articles_data = url.read()
        news_articles_response = json.loads(news_articles_data)
        
        news_articles_results = None

        if(news_articles_response):
            news_articles_list = news_articles_response['articles']
            news_articles_results = process_results(news_articles_list)
    return news_articles_results

def process_results(news_articles_list):
    '''
    function that processes the revieved data
    '''
    results = [] 
    for news in news_articles_list:
        source_id = news.get('source') 
        source = news.get('source') 
        author = news.get('author') 
        title = news.get('title')
        description = news.get('description')
        url = news.get('url')
        urlToImage = news.get('urlToImage')
        publishedAt = news.get('publishedAt')
        content = news.get('content')

        if(urlToImage == None):
            urlToImage = '/static/images/default_news_image.png'
        news_object = NewsGeneralModel(source,source_id,author,title,description,url,urlToImage,publishedAt,content)
        if content != None:
            results.append(news_object)
    return results

def get_sources(category):
    sources_url = article_url.format(category,api_key,)

    with urllib.request.urlopen(sources_url) as url:
        sources_response = json.loads(url.read())
        
        sources_results = None

        if sources_response:
            sources_list = sources_response['sources']
            sources_results = process_sources(sources_list)
    return sources_results

def process_sources(sources_list):
    '''
    function to generate a python dictionary containing sources
    '''
    sources=[]
    for source in sources_list:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        url=source.get('url')
        category=source.get('category')
        language=source.get('language')
        country=source.get('country')

        source_object = NewsSourceModel(id,name,description,url,category,language,country)
        sources.append(source_object)
    return sources