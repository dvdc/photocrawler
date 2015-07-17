import urllib.request
from bs4 import BeautifulSoup
import re

#Set download location
downpath = '[path to download photos to]'

# Grab image url
coreurl = 'http://photography.nationalgeographic.com'
baseurl = '/photography/photo-of-the-day/'

homesoup1 = BeautifulSoup(urllib.request.urlopen("http://photography.nationalgeographic.com%s" % (baseurl)))
for div in homesoup1.find_all("div", class_="primary_photo"):
    for link in div.find_all("img"):
        photo = link['src']
        print(photo)

    url = 'http:%s' % (photo)
    print(url)
    filename = url.split('/')[-1].split('#')[0].split('?')[0]
    #print(filename)
    urllib.request.urlretrieve(url, "%s/%s" % (downpath, filename))
#print("http://photography.nationalgeographic.com%s" % (baseurl))

homesoup = BeautifulSoup(urllib.request.urlopen("http://photography.nationalgeographic.com%s" % (baseurl)))
for h in homesoup.find_all("p", class_="prev first"):
    for pf in h.find_all("a"):
        baseurl = pf['href']

for x in range (0,1000):
    presoup = BeautifulSoup(urllib.request.urlopen("http://photography.nationalgeographic.com%s" % (baseurl)))
    #print("presoup")
    for p in presoup.find_all("p", class_="prev"):
        #print("get prev link")
        for base in p.find_all("a"):
            baseurl = base['href']
            #print(baseurl)
            soup = BeautifulSoup(urllib.request.urlopen("http://photography.nationalgeographic.com%s" % (baseurl)))
            #print("soup")
            for div in soup.find_all("div", class_="primary_photo"):
                #print("get image")
                #print(div)
                for link in div.find_all("img"):
                    photo = link['src']
                    #print(photo)

                url = 'http:%s' % (photo)
                print(url)
                filename = url.split('/')[-1].split('#')[0].split('?')[0]
                #print(filename)
                urllib.request.urlretrieve(url, "%s/%s" % (downpath, filename))
