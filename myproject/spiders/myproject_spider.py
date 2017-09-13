import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from myproject.items import MyprojectItem


class MyProjectSpider(scrapy.Spider):
    name = 'myproject'
    allowed_domains = ["23us.so"]
    start_url = "http://www.23us.so/list/"

    def start_requests(self):
        for i in range(1, 2):
            url = self.start_url + "9_" + str(i) + ".html"
            yield Request(url, self.parse,
                          headers={'User-Agent': "your agent string"})

    def parse(self, response):
        # max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        # bashurl = str(response.url)[:-7]
        # for num in range(1, int(max_num) + 1):
        #     url = bashurl + "_" + str(num) + ".html"
        #     yield Request(url, callback=self.get_name, headers={'User-Agent': "your agent string"})

        max_num = response.xpath('//div[@id="pagelink"]/a/text()').extract()[-1]
        bashurl = str(response.url)[:-7]
        for num in range(1, int(max_num) + 1):
            url = bashurl + "_" + str(num) + ".html"
            yield Request(url, callback=self.get_name, headers={'User-Agent': "your agent string"})

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor="#FFFFFF")
        for td in tds:
            novelname = td.find('a').get_text()
            novelurl = td.find('a')['href']
            yield Request(novelurl, callback=self.get_chapterurl, meta={'name': novelname, 'url': novelurl})

    def get_chapterurl(self, response):
        item = MyprojectItem()
        name = response.meta['name']
        url = response.meta['url']
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text()
        serialstatus = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[2].get_text()
        serialnumber = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[4].get_text()
        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
        # print(
        #     "name ; " + name
        #     + " url : " + url
        #     + " category : " + category
        #     + " author : " + author
        #     + " serialstatus : " + serialstatus
        #     + " serialnumber : " + serialnumber
        #     + " bash_url : " + bash_url
        # )

        item['novelurl'] = url
        item['name'] = name
        item['category'] = category
        item['author'] = author
        item['serialstatus'] = serialstatus
        item['serialnumber'] = serialnumber

        return item
