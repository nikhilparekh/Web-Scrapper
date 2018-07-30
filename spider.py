from urllib.request import urlopen
from linkFinder import linkFinder
from func import *

class spider:
    domain_name = ''
    project_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled_file = set()


    def __init__(self, project_name, home_page_url, domain_name):
         spider.project_name = project_name
         spider.home_page_url = home_page_url
         spider.domain_name = domain_name
         spider.queue_file = spider.project_name + '/queue.txt'
         spider.crawled_file = spider.project_name + '/crawled.txt'
         self.boot()
         self.crawl_page("First Spider", spider.home_page_url)

    @staticmethod
    def boot():
        create_project_directory(spider.project_name)
        create_data_files(spider.project_name, spider.home_page_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in spider.crawled:
            print(thread_name+ ' now crawling '+page_url)
            print('Queue '+str(len(spider.queue)+' | Crawled '+str(len(spider.crawled))))
            spider.addLinksToQueue(spider.gatherLinks(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.updateFiles()

    @staticmethod
    def gatherLinks(page_url):
        html_string =''
        try:
            response = urlopen(page_url)
            if response.getheader('content-type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = linkFinder(spider.home_page_url, page_url)
            finder.feed(html_string)
        except:
            print("Error, Unable to crawl page")
            return set()
        return finder.page_links()

    @staticmethod
    def addLinksToQueue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                    continue
            if spider.domain_name not in url:
                    continue
            spider.queue.add(url)   
    
    @staticmethod
    def updateFiles():
        set_to_file(spider.queue,spider.queue_file)
        set_to_file(spider.crawled, spider.crawled_file)
                
            