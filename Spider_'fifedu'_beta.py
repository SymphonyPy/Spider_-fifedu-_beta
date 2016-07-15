import urllib.request
import urllib.parse
import re
import requests
from bs4 import BeautifulSoup
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
          'Cookie': 'JSESSIONID=621909FFCB71801B737A90A73C886DE2-n1; sel_nav=sy; CNZZDATA1253891395=1568598399-1468215028-http%253A%252F%252Fbjut.fifedu.com%252F%7C1468568527; _webim_cookie_adb9f412a82e40cfb88c8b11ff03b640=%7B%22o%22%3Afalse%2C%22s%22%3A%22available%22%7D'}
url = 'http://bjut.fifedu.com/iplat/bp/student/class/studentList?classId=2811000026000002'
class_number_list = []
for i in range(27,159):
    if (i<100):
        url_final = url + '0'+str(i)
    else:
        url_final = url + str(i)
    request = urllib.request.Request(url_final, headers=header)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response.read())
    pattern = re.compile('.*?<span>(.*?)</span>.*?')
    class_number = re.findall(pattern, str(soup.select('.banji-title')))
    print(class_number[0])
    class_number_list.append(class_number[0])
class_number_list.sort()
file = open('d://class_number.txt','w+')
for i in class_number_list:
    file.write(i+'\n')
file.close()
