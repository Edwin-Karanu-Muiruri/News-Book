import urllib.request,json
from models import NewsSourceModel,NewsArticleModel,NewsGeneralModel

api_key=None
base_url=None

def request_config(app):
    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    
def get_articles(endpoint,query,maximum):
    '''
    function that gets the json response from newsapi
    '''
    news_articles_url=base_url.format(endpoint,api_key,query)
    with urllib.request.urlopen(news_articles_url) as url:
        news_articles_data = url.read()
        news_articles_response = json.loads(news_articles_data)
        
        news_articles_results = None

        if(news_articles_response):
            news_articles_list = news_articles_response['articles']
            news_articles_results = process_results(news_articles_list,maximum)
    return news_articles_results

def process_results(news_articles_list,maximum):
    '''
    function that processes the revieved data
    '''
    results = [] 
    i=0
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
        i+=1
        if i <= maximum:
            if(urlToImage == None):
                urlToImage = 'static/images/default_news_image.png'
            news_object = NewsGeneralModel(source,source_id,author,title,description,url,urlToImage,publishedAt,content)
            if content != None:
                results.append(news_object)
    return results
