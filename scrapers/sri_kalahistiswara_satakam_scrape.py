import urllib2
import urllib
import BeautifulSoup
import nltk
import os
import sys

def get(url):
   req = urllib2.Request(url, headers = {"Connection":"keep-alive", "User-Agent":"Mozilla/5.0"})
   html = urllib2.urlopen(req).read()
   html = html.replace('\r','')
   soup = BeautifulSoup.BeautifulSoup(html)
   con = soup.findAll('b') 
   res = []
   for i in con:
      x = i.findAll(text = True)
      if(len(x) == 0):
         continue
      tt = str(x[0].encode('utf8'))
      tt = tt.strip('\n')
      tt = tt.strip(' ')
      tt = tt.strip('')
      tt = tt[::-1]
      tt = tt.strip('\n')
      tt = tt.strip(' ')
      tt = tt.strip('')
      tt = tt[::-1]
      res.append(tt)      
   return res

def main(urls):
   f = open('./satakam.txt', 'w')
   for i in urls:
      text = get(i)
      for j in text:
         x = j
         if(x == '' or x == None):
            continue
         else:
            f.write(x)
            f.write('\n')
         if('\xe0\xb0\xb6\xe0\xb1\x8d\xe0\xb0\xb0\xe0\xb1\x80\xe0\xb0\x95\xe0\xb0\xbe\xe0\xb0\xb3\xe0\xb0\xb9\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xa4\xe0\xb1\x80\xe0\xb0\xb6\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xb0\xe0\xb0\xbe' in x):
            f.write('\n')
   f.close()
   sys.stdout.flush()

baseurls = []
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B6%E0%B1%8D%E0%B0%B0%E0%B1%80_%E0%B0%95%E0%B0%BE%E0%B0%B3%E0%B0%B9%E0%B0%B8%E0%B1%8D%E0%B0%A4%E0%B1%80%E0%B0%B6%E0%B1%8D%E0%B0%B5%E0%B0%B0_%E0%B0%B6%E0%B0%A4%E0%B0%95%E0%B0%AE%E0%B1%81')
main(baseurls)