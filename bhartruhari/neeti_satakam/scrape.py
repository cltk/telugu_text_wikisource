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
   con = soup.findAll('p') 
   res = []
   for i in con:
      x = i.findAll(text = True)
      if(len(x) == 0):
         continue
      for j in x:
         tt = str(j.encode('utf8'))
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
   current = 1
   f = open('./satakam.txt', 'w')
   for i in urls:
      print current, 
      sys.stdout.flush()
      current += 1
      text = get(i)
      for j in text:
         x = j
         x = x.replace('       ', '')
         if(x == '' or x == None):
            continue
         else:
            if('\xe0\xb0\xa4\xe0\xb0\xbe\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xaa\xe0\xb0\xb0\xe0\xb1\x8d\xe0\xb0\xaf\xe0\xb0\xae\xe0\xb1\x81' in x):
               f.write('\n')
            else:
               f.write(x)
               f.write('\n')
   f.close()
   print
   sys.stdout.flush()

baseurls = []
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%A8%E0%B1%80%E0%B0%A4%E0%B0%BF_%E0%B0%B6%E0%B0%A4%E0%B0%95%E0%B0%AE%E0%B1%81')
main(baseurls)