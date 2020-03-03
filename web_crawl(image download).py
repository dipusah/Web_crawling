import requests
from bs4 import BeautifulSoup #bs4- html parser(only image tag)
def download_file(url):
    local_filename =url.split('/')[-1]
    r= requests.get(url)
    with open(local_filename,'wb') as f:  #'wb' - write binary (Image is binary file)
        for chunk in r.iter_content(chunk_size=1024): #divides the image(file) into chunks so that when larger file is to be download the system doesnot hang or prvent crashing.
            if chunk: #filter out keep-alive new chunks
                f.write(chunk)
    return

BASE_URL = 'http://www.santabanta.com/wallpapers/nature/21/'

html_data = requests.get(BASE_URL)
parsed_data = BeautifulSoup(html_data.text,'html.parser')

img_tags = parsed_data.find_all('img') #'img' tag (image are kept inside)

for img in img_tags:
    download_file(img['src']) #src -attribute of img tag.