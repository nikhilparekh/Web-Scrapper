from html.parser import HTMLParser
from urllib import parse

class linkFinder(HTMLParser):

    def __init__(self, home_page_url, page_url):
        super().__init__()
        self.home_page_url = home_page_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self,tag, attrs):
        if tag == 'a':
            for(attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.home_page_url, value)
                    self.links.add(url)
    
    def page_links(self):
        return self.links

    def error(self, message):
        pass