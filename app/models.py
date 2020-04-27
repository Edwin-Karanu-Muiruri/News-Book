class NewsSourceModel:
    '''
    structure of the expected news structure from api class
    '''
    def __init__(self,id,source):
        self.id = id
        self.source = source

class NewsArticleModel:
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class NewsGeneralModel:
    def __init__(self,source,source_id,author,title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.source_id = source_id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content