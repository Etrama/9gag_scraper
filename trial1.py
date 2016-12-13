import requests

r = requests.get("http://9gag.com/")

s = r.content

print r.status_code


#remember to initialize all these variables
k1 = 0
k2 = 0
l1 = 0
l2 = 0
i1 = [0]
i2 = [0]

#while i1[-1]>=0:
#	l1 = s.find("badge-item-img",k1)
#	l2 = s.find(".jpg\" alt",k2)
#	k1 = l1+2
#	k2 = l2+2
#	i1.append(l1)
#	i2.append(l2)
#check i1, i2 now
#updated code since usin above while finds only jpg
while i1[-1]>=0:
	l1 = s.find("badge-item-img",k1)
	l2 = s.find("alt",l1)
	k1 = l1+2
	i1.append(l1)
	i2.append(l2)
#in i1 we now have 'b' of "bade-item-img"
#in i2 we have the 'a' of the first alt after "badge-item-img"
#verified.


#no need to initialize i3
for i3 in range(1,len(i1)-1):
    i1[i3] = i1[i3] + 21
    i2[i3] = i2[i3] - 3

print i1
print i2


#now in i1 we have the 'h' of the http
#in i2 we have the 'g' of jpg
#in the new i2 we have the ending of the image url,which is 'g' 
#if image is in jpg format


#there is a constant difference of 52 between i1 and i2.
#makes life a lot easier.
#the above is null and void as this logic only works for images
#gifs have a longer url.
#count = 1

dicturl = {}
for a in range(1,len(i1)-1):
	key = a
	value=[]
	for b in range(0,i2[a]-i1[a]+1):
		#the i2[a]-i1[a]+1, the +1 is 
		#here because we need the first character as well
		value.append(s[i1[a]+b])
	dicturl[a] = value

for i in dicturl:
    print "".join(dicturl[i])

#creating a list with the urls.
images=[]
for i in dicturl:
	images.append("".join(dicturl[i]))

#now images list has all the urls as alements

r=[]

for i in range(0,len(images)):
	r.append(requests.get(images[i]))
   
print r
#this should return an array of <Response [200]>s

#for i in range(0,len(images)):
#	print r[i].headers

#this prints some object name value pairs.

#r.content will have the image itself and not the url
#we need stringIO to read the string and store it as a string buffer
#now we can display the image.
from PIL import Image
from StringIO import StringIO
for i in range(0,len(r)):
	imageact = r[i].content
	img = Image.open(StringIO(imageact))
	img.show()
	

