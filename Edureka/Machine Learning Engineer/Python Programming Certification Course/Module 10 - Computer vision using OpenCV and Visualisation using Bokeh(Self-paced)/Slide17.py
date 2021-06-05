import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.thomascook.in/tcportal/india-holidays/Karnataka-holiday-packages?hldplace=Kerala")
c=r.content
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())
