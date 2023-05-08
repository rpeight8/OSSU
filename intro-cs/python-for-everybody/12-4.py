from bs4 import BeautifulSoup
import urllib.request

url = "http://www.dr-chuck.com/page1.htm"

html_doc = urllib.request.urlopen(url)
soup = BeautifulSoup(html_doc, "html.parser")

print(f"Amount of <p>: {len(soup.find_all('p'))}")
