import os
class Config:
    '''
    General configuration parent class
    '''
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'
    BASE_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = False


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}