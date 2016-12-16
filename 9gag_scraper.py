from bs4 import BeautifulSoup
import requests
import ftfy

r = requests.get("http://9gag.com")
#to check if you got the page, use comment below
#print r.status_code

s = r.content
soup = BeautifulSoup(s, 'html.parser')

imgtags = soup.find_all("img",{"class":"badge-item-img"})

#scraping image urls
#scraping alt tags
imgurls = []
imgalts = []
count =0 
for i in range(0, len(imgtags)):
	
		imgurls.append(imgtags[i]['src'].encode("utf-8","ignore"))
		imgalts.append(imgtags[i]['alt'].encode("utf-8","ignore"))
		count+=1
	

#print imgurls
#print imgalts

ui = raw_input("Save images? (y/n) ")
if ui == 'y' or ui == "Y":
    from PIL import Image
    from StringIO import StringIO
    from string import maketrans
    print "Saving Images...."
    dirloc = raw_input("Enter the directory to save images in: (format: d: or d:/a/b/c) ")
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

    for i in range(0,count):
        imgalts2.append(imgalts[i].translate(trantab))

    import progressbar
    widgets = [progressbar.Bar('=','[',']'),' ',progressbar.Percentage()]
    bar = progressbar.ProgressBar(widgets = widgets)
    bar.start()
    print("Image download progress: ")
    for i in range(0,count):
        r = requests.get(imgurls[i])
        j = Image.open(StringIO(r.content))
        j.save(dirloc+"/"+imgalts2[i]+".jpeg")
        bar.update(10*(i+1))
    
    print "Images saved."
else:
    print "Images not saved."

ui2 = raw_input("Make collage of downloaded images? (y/n) ")

if (ui == 'y' or ui == 'Y') and (ui2 =='y' or ui2 == 'Y'):
    #collage code goes here
    import PIL
    sizes = []
    
    for i in range(count):
        im = Image.open(dirloc+"/"+imgalts2[i]+".jpeg")
        sizes.append(im.size)

    heights = []
    widths = []
    for j in range(len(sizes)):
        heights.append(sizes[j][1])
        widths.append(sizes[j][0])

    resizedims = []
    for i in range(len(heights)):
        im = Image.open(dirloc+"/"+imgalts2[i]+".jpeg")
        resizedims.append(im.resize((sizes[i][0],min(heights)),PIL.Image.ANTIALIAS))

    new_im = Image.new('RGB',(2*max(widths),5*min(heights)))
    i = 0
    x = 0
    y = 0

    for cols in range(2):
        for rows in range(5):
            #print(i,x,y)
            new_im.paste(resizedims[i],(x,y))
            i = i + 1
            y = y + min(heights)
        x = x + max(widths)
        y = 0

    ui3 = raw_input("Enter location to save collage: ")
    new_im.save(ui3+"Collage.jpeg")
    im = Image.open(ui3+"Collage.jpeg")
    im.show()

else:
    print("If images weren't saved, collage cannot be constructed.")
    print("Or, you chose not to make a collage.")   

  
    