import requests
from bs4 import BeautifulSoup

urls = [
    #"https://www.nytimes.com/2020/12/20/us/politics/congress-stimulus-deal.html",
    #"https://www.nytimes.com/2020/12/20/sports/football/nfl-scores-results-week-15.html"
    "https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html?action=click&module=Opinion&pgtype=Homepage"
]


def process_urls(url):
    #print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@ working with url:{url}")
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="html.parser")
    head_line_html_elment = soup.find(attrs={"data-test-id": "headline"})
    #print(f"*{head_line_html_elment.string}*") 
    #summary
    article_summary = soup.find("p",id="article-summary")
    #print(article_summary.string)
    article_body = soup.find("section",attrs={"name":"articleBody"})
    #print(article_body)
    article_paragraph_divs = article_body.find_all("div",class_="css-1fanzo5 StoryBodyCompanionColumn")
    for div in article_paragraph_divs:
        article_paragraphs = div.find_all("p",class_="css-axufdj evys1bk0")
        print(f"@@@@@@@:{article_paragraphs}:@@@@@ {type(article_paragraphs)}")
        for paragraph in article_paragraphs:
            print(f"*{paragraph.string}*")


for url in urls:
    process_urls(url)
