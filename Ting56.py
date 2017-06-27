# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import sys
import re


type = sys.getfilesystemencoding()

urlPrefix="http://www.ting56.com"

def main():
    url = "http://www.ting56.com/mp3/4094.html"
    getUrls(getHtml(url));

def getHtml(url):

    # 浏览器头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url=url, headers=headers)
    data = urllib2.urlopen(req).read()
    html = data.decode("gbk").encode(type)
    # print  html

    return html

def FonHen_JieMa(u):
    u= u.replace("FonHen_JieMa('","").replace("')","")

    tArr=u.split("*");

    str=""

    for code in tArr:
        #print code
        if len(code)==0:
            continue
        str+=chr(int(code))

    return str.split("&")[0];



def getUrls(html):
    count = 0
    matchObjs = regex_match_findall("/video.*?.html", html)
    if matchObjs and len(matchObjs) > 0:
        for temp in matchObjs:
            number = temp.split('-')[2].split('.')[0]
            if int(number) > 1170:
                count += 1
                sourceUrl= urlPrefix+temp
                html = getHtml(sourceUrl)
                code = getCharAtt(html)
                #print code
                m4aUrl= FonHen_JieMa(code);
                title=getTitle(html);
                print "downloading start"+title
                urllib.urlretrieve(m4aUrl, title+".m4a")
                print "downloading end"+title


    print count

def getTitle(html):
    #print html
    m = re.search(u"<title>.*?</title>", html);
    code = m.group(0).replace("<title>", "").replace("</title>", "")
    print code
    return code

def getCharAtt(html):
    m = re.search(u"FonHen_JieMa\('([0-9,*]*)'\)", html);
    code= m.group(0)
    return code

'''查找所有的匹配结果'''
def regex_match_findall(regex, data):
   result = re.findall(regex, data, re.I|re.M|re.S)
   return result

if __name__ == '__main__':
    main()