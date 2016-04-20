import urllib2
import urllib
import BeautifulSoup
import nltk
import os
import sys

def extracturls(url):
   req = urllib2.Request(url, headers = {"Connection":"keep-alive", "User-Agent":"Mozilla/5.0"})
   html = urllib2.urlopen(req).read()
   html = html.replace('\r','')
   soup = BeautifulSoup.BeautifulSoup(html)
   try:
       OL = soup.findAll('ol')
       LI = OL[0].findAll('li')
   except IndexError:
      UL = soup.findAll('ul')
      LI = UL[0].findAll('li')
   res = []
   for i in LI:
      res.append('http://te.wikisource.org' + i.find('a').get('href'))
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
   div = soup.findAll(lambda tag: tag.name=='div' and tag.has_key('class') and tag['class'] == 'mw-content-ltr') 
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
   a[1] = "srushti_khandam"
   a[2] = "sathi_khandam"
   a[3] = "parvathy_khandam"
   a[4] = "kumara_khandam"
   a[5] = "yuddha_khandam"
   a[6] = "rudra_khandam"
   a[7] = "leela_khandam"
   a[8] = "linga_vybhava_khandam"
   a[9] = 'uma_khandam'
   a[10] = "kailasa_khandam"
   a[11] = "vayuviya_khandam"
   a[12] = "vidweswara_khandam"
   L = len(urls)
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

baseurls = extracturls('https://te.wikisource.org/wiki/%E0%B0%B6%E0%B0%BF%E0%B0%B5%E0%B0%AA%E0%B1%81%E0%B0%B0%E0%B0%BE%E0%B0%A3%E0%B0%AE%E0%B1%81')
urls = getall(baseurls)
main(urls)