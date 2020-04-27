import unittest
from app.models import NewsArticleModel

class TestNewsArticleModel(unittest.TestCase):
    def setUp(self):
        '''
        Setup method that will be run before every test
        '''
        self.new_article =NewsArticleModel('author','title','description','url','urlToImage','publishedAt','content')

    def test_init(self):
        self.assertTrue(isinstance(self.new_article, NewsArticleModel))
