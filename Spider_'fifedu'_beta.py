import urllib.request
import urllib.parse
import re
import requests
from bs4 import BeautifulSoup
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
          'Cookie': 'JSESSIONID=F20490CB26A2282FFEB3EF143ACAB86F-n1; CNZZDATA1253891395=1568598399-1468215028-http%253A%252F%252Fbjut.fifedu.com%252F%7C1468737423; sel_nav=sy'}
class_url = 'http://bjut.fifedu.com/iplat/bp/student/class/studentList?classId=2811000026000002'
userdetail_url = 'http://bjut.fifedu.com/iplat/bp/teacher/class/userDetail'
class_number_list = []
for i in range(27,159):
    for page in range(1,3):
        if (int(i)<100):
            url_final = class_url + '0' + str(i)+'&curPage='+str(page)
        else:
            url_final = class_url + str(i)+'&curPage='+str(page)
        request = urllib.request.Request(url_final, headers=header)
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response.read())
        if(page==1):
            pattern_for_class_number = re.compile('.*?<span>(.*?)</span>.*?')
            class_number = re.findall(pattern_for_class_number, str(soup.select('.banji-title')))
            class_number_list.append(class_number[0])
            print('当前班级：'+str(class_number[0]))
        pattern_for_studentlist = re.compile('.*?<span class="gray" id="ud_areacode1_(.*?)">.*?')
        studentlist = re.findall(pattern_for_studentlist, str(soup.select('.huoban_td')))
        for student in studentlist:
            data = {'userid': str(student)}
            data = urllib.parse.urlencode(data).encode(encoding='UTF8')
            request = urllib.request.Request(userdetail_url, data=data, headers=header)
            response = urllib.request.urlopen(request)
            soup = BeautifulSoup(response.read())
            pattern_for_student_pictureurl = re.compile('.*?"note":"","avator":"(.*?)".*?')
            student_picture_url = 'http://bjut.fifedu.com/iplat/' + re.findall(pattern_for_student_pictureurl, str(soup))[0]
            pattern_for_userName = re.compile('.*?"userName":"(.*?)","gender":".*?')
            student_userName = re.findall(pattern_for_userName, str(soup))[0]
            try:
                picture = urllib.request.urlopen(student_picture_url).read()
                pattern_for_student_idCardNo = re.compile(
                    'http://bjut.fifedu.com/iplat//upload/bjut/2.*?/(.*?).jpg')
                student_idCardNo = re.findall(pattern_for_student_idCardNo, student_picture_url)[0]
                print('当前学生：' + student_idCardNo + '成功')
                file = open('d:\spider_picture/' + str(class_number[0]) + student_userName + student_idCardNo + '.jpg', 'wb')
                file.write(picture)
                file.close()
            except:
                pass



