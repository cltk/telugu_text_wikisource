import urllib2
import urllib
import BeautifulSoup
import nltk
import os
import sys

def extracturls(url):
   #url = 'https://te.wikisource.org/wiki/%E0%B0%AA%E0%B1%8B%E0%B0%A4%E0%B0%A8_%E0%B0%A4%E0%B1%86%E0%B0%B2%E0%B1%81%E0%B0%97%E0%B1%81_%E0%B0%AD%E0%B0%BE%E0%B0%97%E0%B0%B5%E0%B0%A4%E0%B0%AE%E0%B1%81/%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%A5%E0%B0%AE_%E0%B0%B8%E0%B1%8D%E0%B0%95%E0%B0%82%E0%B0%A7%E0%B0%AE%E0%B1%81'
   req = urllib2.Request(url, headers = {"Connection":"keep-alive", "User-Agent":"Mozilla/5.0"})
   html = urllib2.urlopen(req).read()
   html = html.replace('\r','')
   soup = BeautifulSoup.BeautifulSoup(html)
   span = soup.findAll(lambda tag: tag.name=='span' and tag.has_key('class') and tag['class'] == 'mw-headline')
   res = []
   for i in span:
      #a = i.findAll(lambda tag: tag.name=='a')
      try:
         res.append('http://te.wikisource.org' + i.find('a').get('href'))
      except AttributeError:
         pass
   return res

def getall(Url):
   print "getting urls ... ",
   sys.stdout.flush()
   res = []
   j = 1
   for i in Url:
      print j,
      sys.stdout.flush()
      res.append(extracturls(i))
      j += 1
   print
   print "Done"
   sys.stdout.flush()
   return res

def get(url):
   req = urllib2.Request(url, headers = {"Connection":"keep-alive", "User-Agent":"Mozilla/5.0"})
   html = urllib2.urlopen(req).read()
   html = html.replace('\r','')
   soup = BeautifulSoup.BeautifulSoup(html)
   div = soup.findAll(lambda tag: tag.name=='div' and tag.has_key('class') and tag['class'] == 'poem') 
   res = []
   for i in div:
      rows = i.findAll(lambda tag: tag.name=='p')
      for j in rows:
         tmp = j.findAll(text = True)
         for k in tmp:
            tt = str(k.encode('utf8'))
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
   a = {}
   a[1] = "avatharika"
   a[2] = "bala_khandam"
   a[3] = "ayodhya_khandam"
   a[4] = "aranya_khandam"
   a[5] = "kishkindha_khandam"
   a[6] = "sundara_khandam"
   a[7] = "yudha_khandam"
   L = len(urls)
   assert(L == 7)
   print 'scraping page :   '
   for i in xrange(L):
      dirname = './' + a[i + 1]
      os.system('rm -rf ' + dirname)
      os.system('mkdir ' + dirname)
      print "    ", dirname[2::], ",   chapter : ",
      sys.stdout.flush()
      L1 = len(urls[i])
      for j in xrange(L1):
         fname = dirname + '/' + 'chapter-' + str(j + 1)
         os.system('rm -rf ' + fname)
         cont = get(urls[i][j])
         f = open(fname, 'w')
         print j + 1,
         sys.stdout.flush()
         for k in cont:
            tmp = k
            f.write(tmp + '\n')
         f.close()
      print
   print
   print "Done"
   sys.stdout.flush()

baseurls = []
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%AE%E0%B1%8A%E0%B0%B2%E0%B1%8D%E0%B0%B2_%E0%B0%B0%E0%B0%BE%E0%B0%AE%E0%B0%BE%E0%B0%AF%E0%B0%A3%E0%B0%AE%E0%B1%81/%E0%B0%85%E0%B0%B5%E0%B0%A4%E0%B0%BE%E0%B0%B0%E0%B0%BF%E0%B0%95')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%AE%E0%B1%8A%E0%B0%B2%E0%B1%8D%E0%B0%B2_%E0%B0%B0%E0%B0%BE%E0%B0%AE%E0%B0%BE%E0%B0%AF%E0%B0%A3%E0%B0%AE%E0%B1%81/%E0%B0%AC%E0%B0%BE%E0%B0%B2_%E0%B0%95%E0%B0%BE%E0%B0%82%E0%B0%A1%E0%B0%AE%E0%B1%81')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%AE%E0%B1%8A%E0%B0%B2%E0%B1%8D%E0%B0%B2_%E0%B0%B0%E0%B0%BE%E0%B0%AE%E0%B0%BE%E0%B0%AF%E0%B0%A3%E0%B0%AE%E0%B1%81/%E0%B0%85%E0%B0%AF%E0%B1%8B%E0%B0%A7%E0%B1%8D%E0%B0%AF%E0%B0%BE_%E0%B0%95%E0%B0%BE%E0%B0%82%E0%B0%A1%E0%B0%AE%E0%B1%81')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%AE%E0%B1%8A%E0%B0%B2%E0%B1%8D%E0%B0%B2_%E0%B0%B0%E0%B0%BE%E0%B0%AE%E0%B0%BE%E0%B0%AF%E0%B0%A3%E0%B0%AE%E0%B1%81/%E0%B0%85%E0%B0%B0%E0%B0%A3%E0%B1%8D%E0%B0%AF_%E0%B0%95%E0%B0%BE%E0%B0%82%E0%B0%A1%E0%B0%AE%E0%B1%81')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%AE%E0%B1%8A%E0%B0%B2%E0%B1%8D%E0%B0%B2_%E0%B0%B0%E0%B0%BE%E0%B0%AE%E0%B0%BE%E0%B0%AF%E0%B0%A3%E0%B0%AE%E0%B1%81/%E0%B0%95%E0%B0%BF%E0%B0%B7%E0%B1%8D%E0%B0%95%E0%B0%BF%E0%B0%82%E0%B0%A7%E0%B0%BE_%E0%B0%95%E0%B0%BE%E0%B0%82%E0%B0%A1%E0%B0%AE%E0%B1%81')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%AE%E0%B1%8A%E0%B0%B2%E0%B1%8D%E0%B0%B2_%E0%B0%B0%E0%B0%BE%E0%B0%AE%E0%B0%BE%E0%B0%AF%E0%B0%A3%E0%B0%AE%E0%B1%81/%E0%B0%B8%E0%B1%81%E0%B0%82%E0%B0%A6%E0%B0%B0%E0%B0%95%E0%B0%BE%E0%B0%82%E0%B0%A1%E0%B0%AE%E0%B1%81')
baseurls.append('https://te.wikisource.org/wiki/%E0%B0%AE%E0%B1%8A%E0%B0%B2%E0%B1%8D%E0%B0%B2_%E0%B0%B0%E0%B0%BE%E0%B0%AE%E0%B0%BE%E0%B0%AF%E0%B0%A3%E0%B0%AE%E0%B1%81/%E0%B0%AF%E0%B1%81%E0%B0%A6%E0%B1%8D%E0%B0%A7_%E0%B0%95%E0%B0%BE%E0%B0%82%E0%B0%A1%E0%B0%AE%E0%B1%81_-_%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%A5%E0%B0%AE%E0%B0%BE%E0%B0%B6%E0%B1%8D%E0%B0%B5%E0%B0%BE%E0%B0%B8%E0%B0%AE%E0%B1%81')

urls = getall(baseurls)
main(urls)