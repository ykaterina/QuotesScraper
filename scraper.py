import requests
from bs4 import BeautifulSoup
import json

URL = "http://quotes.toscrape.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find("div", {"class":"quote"})
job_elements = soup.find_all("div", {"class":"quote"})

quotes = []
for job_element in job_elements:
      quote = job_element.find("span", itemprop="text")
      author = job_element.find("small", itemprop="author")
      tags = job_element.find_all("a", class_="tag")

      tags_text = []
      for tag in tags:
            tags_text.append(tag.text.strip())
      item = {
            "quote": quote.text.replace("“","").replace("”","").strip(),
            "author": author.text.strip(),
            "tags": tags_text
      }
      quotes.append(item)

with open('data.json', 'w') as f:
    json.dump(quotes, f)