import requests

r=requests.get("http://www.thomascook.in/tcportal/india-holidays/Karnataka-holiday-packages?hldplace=Kerala")
c=r.content
print(c)
