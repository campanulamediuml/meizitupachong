#coding=utf-8
import urllib2
import os
import re
import time

def url_open(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',"HeJingjing's Browser") 
    response = urllib2.urlopen(req)
    return response.read()

def get_page(url):
    html = url_open(url).decode('utf-8')
    pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>' #regular expression to get url
    page = int(re.findall(pattern,html)[0])
    return page

def find_imgs(page_url):
    pattern = r'<img src="(.*?\.jpg)"'
    html = url_open(page_url).decode('utf-8')
    img_addrs = re.findall(pattern,html)
    return img_addrs

def save_imgs(img_addrs,page_num,folder):
    
    
    for i in img_addrs:
        pattern = r'sinaimg.cn/mw600/(.*?).jpg'
        filename = i.split('/')[-1]
        image = url_open('http:'+i)
        print 'Downloading',i
        with open(filename,'wb') as f:
            f.write(image)
            f.close()

def download_mm(folder,pages):
    os.mkdir(folder) #creat a new document
    os.chdir(folder) #jump to the document
    folder_top = os.getcwd() #get into the document
    url = 'http://jandan.net/ooxx/'
    page_num = get_page(url) #get new url
    for i in range(pages):
        page_num -= i #download
        page_url = url + 'page-' + str(page_num) + '#comments' #make url
        img_addrs = find_imgs(page_url) #get pic's url
        save_imgs(img_addrs,page_num,folder) #save the pic
        os.chdir(folder_top)

if __name__ == '__main__':
    timeformat ='%Y-%m-%d %X'
    timenow = time.strftime( timeformat,time.localtime( time.time() ) )
    folder = str(timenow)  
    for i in folder:
        if i == ':' or '-'or'/':
            i = ''#the document's name is the time
    print folder
    pages = raw_input("How many pages do you wan to download(default is 10): ")
    time.sleep(0.2)
    print '少女祈祷中………'
    if pages is '':
        pages = 10
        download_mm(str(folder),int(pages))
    else:
        download_mm(str(folder),int(pages))

    print '爬虫运行完成，妹子图保存在名为“',folder,'”的文件夹中，按任意键退出~~'
    raw_input()
    exit()










