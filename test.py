import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
pattern = re.compile('<div class="content">\n\n(.*?)\n\n</div>', re.S)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
file = open('d://text.txt','w+',encoding='utf-8')
for i in range(1,51):
    url = 'http://www.qiushibaike.com/'+'8hr/page/'+str(i)+'/'
    request = urllib.request.Request(url,headers=headers)
    html = urllib.request.urlopen(request,timeout=1000)
    soup = BeautifulSoup(html)
    print('\nPage %d'%i)
    file.write('\nPage %d' % i)
    for item in soup.select('.content'):
        items = re.findall(pattern, str(item))
        print(items[0])
        file.write('\n')
        file.write(str(items[0]))
file.close()

