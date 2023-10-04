from urllib.request import urlopen
import requests
from urllib.request import Request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
headers = {
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'#每个爬虫必备的伪装
          }
base = 'https://pmt.physicsandmathstutor.com/wp-content/uploads/'

def clean_url(url):
    # Use a regular expression to replace '/..', if it appears in the URL, with an empty string
    return re.sub(r'/\.\.', '', url).replace('//', '/').replace(':/', '://')

def download_file(url,save_path):

    session = requests.Session()
    session.headers = headers

    response = session.get(url)
    bs = BeautifulSoup(response.content, 'html.parser')

    for link in bs.find('div', {'id': 'content'}).find_all('a'):  
        if link.get('href'):
            if link.get('href').endswith('pdf'):
                link_new = link.get('href').replace("/wp-content/uploads/../..", "").replace(" ","%20")
              
 

                string = link.get_text()
                #print(string)
            
                f = open(save_path+"\\"+link.get_text() + '.pdf', 'wb')
            
           
                req = Request(link_new,headers=headers)
                f.write(urlopen(req).read())
    
            

