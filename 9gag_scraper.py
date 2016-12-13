from bs4 import BeautifulSoup
import requests

r = requests.get("http://9gag.com")
#to check if you got the page, use comment below
#print r.status_code

s = r.content
soup = BeautifulSoup(s,'html.parser')

imgtags = soup.find_all("img",{"class":"badge-item-img"})

#scraping image urls
#scraping alt tags
imgurls = []
imgalts = []
for i in range(0,len(imgtags)):
	imgurls.append(str(imgtags[i]['src']))
	imgalts.append(str(imgtags[i]['alt']))

#print imgurls
#print imgalts

ui = raw_input("Save images? (y/n) ")
if ui == 'y' or ui == "Y":
	from PIL import Image
	from StringIO import StringIO
	from string import maketrans
	print "Saving Images...."
	dirloc = raw_input("Enter the directory to save images in: ")
	#saving images
	#the problem with saving images 
	#and using imgalts for img names
	#is that we can't have \ / : * ? " < > 
	#in the name.
	#we need to modify imgalts accordingly.
	imgalts2=[]
	i = 0
	j = 0
	s = []
	intab = "\/:*?\"<>|"
	outtab = "         "
	trantab = maketrans(intab,outtab)

	for i in range(0,len(imgalts)):
		imgalts2.append(imgalts[i].translate(trantab))

	
	for i in range(0,len(imgurls)):
		r = requests.get(imgurls[i])
		j = Image.open(StringIO(r.content))
		j.save(dirloc+"/"+imgalts2[i]+".jpeg")
	
	print "Images saved."
else:
	print "Images not saved."
