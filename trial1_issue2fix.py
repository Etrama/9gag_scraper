from bs4 import BeautifulSoup
import requests

r = requests.get("http://9gag.com")
#to check if you got the page, use comment below
#print r.status_code

s = r.content
soup = BeautifulSoup(s,'html.parser')

imgtags = soup.find_all("img",{"class":"badge-item-img"})

#scraping image urls
imgurls = []
for i in range(0,len(imgtags)):
	imgurls.append(imgtags[i]['src'])

print imgurls

#scraping alt tags
imgalts = []
for i in range(0,len(imgtags)):
	imgalts.append(imgtags[i]['alt'])

print imgalts
