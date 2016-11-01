#!/usr/bin/python
import bs4 
import re
import os
import requests
import urllib2
def search(query):
    DIR="."
    img_name = query
    counter = 0
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    

    header = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url,verify=False,
                                headers={'User-agent': 'Mozilla/5.0 (Windows NT '
                                                       '6.2; WOW64) AppleWebKit/'
                                                       '537.36 (KHTML, like '
                                                       'Gecko) Chrome/37.0.2062.'
                                                       '120 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    images=[tag['src']for tag in soup.find_all('img', {'src': re.compile('gstatic.com')})]
    
    if images:
        for pic in images:
            raw_img = urllib2.urlopen(pic).read()
            
            counter = len([i for i in os.listdir(DIR) if img_name in i]) + 1
            fdata = open(DIR + img_name + "_"+ str(counter)+".jpg", 'wb')
            print fdata
            print str(counter) +' images found for '+query+'...'
            fdata.write(raw_img)
            fdata.close()
    else:
        print 'No Images Found'
        
    print 'Total '+ str(counter) +' images downloaded in '+DIR
    # 20 images limitation is due to depreciated google search image API,will update more in future

if __name__ == "__main__":
    query = input("Enter yousearch for?  eg: 'Dolphin' ")
    product_list = search(query)
        


  
     
