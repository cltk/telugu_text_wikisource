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
         if(x == '' or x == None):
            continue
         else:
            f.write(x)
            f.write('\n')
   f.close()
   print
   sys.stdout.flush()

baseurls = []
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%85')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%86')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%87')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%88')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%89')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%8A')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%8B')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%8E')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%8F')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%90')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%92')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%93')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%95')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%97')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%98')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%9A')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%9B')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%9C')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%9F')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%A4')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%A6')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%A7')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%A8')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%AA')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%AC')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%AD')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%AE')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%AF')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%B0')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%B2')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%B5')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%B6')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%B8')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%B5%E0%B1%87%E0%B0%AE%E0%B0%A8_%E0%B0%AA%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%B2%E0%B1%81_%E0%B0%B9')
main(baseurls)