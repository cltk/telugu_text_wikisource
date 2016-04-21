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
   OL = soup.findAll('ol')
   LI = OL[0].findAll('li')
   res = []
   for i in LI:
      res.append('http://te.wikisource.org' + i.find('a').get('href'))
   return res

def getall():
   print "getting urls ... ",
   sys.stdout.flush()
   Url = []
   Url.append('https://te.wikisource.org/wiki/%E0%B0%AC%E0%B1%8D%E0%B0%B0%E0%B0%B9%E0%B1%8D%E0%B0%AE%E0%B0%AA%E0%B1%81%E0%B0%B0%E0%B0%BE%E0%B0%A3%E0%B0%AE%E0%B1%81')
   res = []
   j = 1
   for i in Url:
      print j,
      sys.stdout.flush()
      res.append(extracturls(i))
      j += 1
   print
   print "Done"
   #print res
   sys.stdout.flush()
   assert(len(res) == 1)
   assert(len(res[0]) == 246)
   res = res[0]
   return res

def get(url):
   req = urllib2.Request(url, headers = {"Connection":"keep-alive", "User-Agent":"Mozilla/5.0"})
   html = urllib2.urlopen(req).read()
   html = html.replace('\r','')
   soup = BeautifulSoup.BeautifulSoup(html)
   div = soup.findAll(lambda tag: tag.name=='div' and tag.has_key('class') and tag['class'] == 'poem') 
   res = []
   #print div[0]
   #exit(0)
   for i in div:
      rows = i.findAll(lambda tag: tag.name=='p')
      #print rows[0].findAll(text = True)[1]
      #exit(0)
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
      #   #print j.findAll(text = True)[0]
      #   res.append(j.findAll(text = True)[0])
   return res

#print get('https://te.wikisource.org/wiki/%E0%B0%AA%E0%B1%8B%E0%B0%A4%E0%B0%A8_%E0%B0%A4%E0%B1%86%E0%B0%B2%E0%B1%81%E0%B0%97%E0%B1%81_%E0%B0%AD%E0%B0%BE%E0%B0%97%E0%B0%B5%E0%B0%A4%E0%B0%AE%E0%B1%81/%E0%B0%A8%E0%B0%B5%E0%B0%AE_%E0%B0%B8%E0%B1%8D%E0%B0%95%E0%B0%82%E0%B0%A7%E0%B0%AE%E0%B1%81/%E0%B0%89%E0%B0%AA%E0%B1%8B%E0%B0%A6%E0%B1%8D%E0%B0%98%E0%B0%BE%E0%B0%A4%E0%B0%AE%E0%B1%81')
#exit(0)
def main(urls):
   a = {}
   L = len(urls)
   print 'scraping page :   ',
   for i in xrange(L):
      fname = './' + 'chapter-' + str(i + 1)
      print i + 1,
      sys.stdout.flush()
      os.system('rm -f ./' + fname)
      cont = get(urls[i])
      f = open(fname, 'w')
      for k in cont:
         tmp = k
         f.write(tmp + '\n')
      f.close()
   print
   print "Done"
   sys.stdout.flush()
urls = getall()
#print urls[0]
#cont = get(urls[0])
#for i in cont:
#   print i
#f = open('./urls.py', 'w')
#f.write(str(urls))
#f.close()
main(urls)
#print extracturls('https://te.wikisource.org/wiki/%E0%B0%AA%E0%B1%8B%E0%B0%A4%E0%B0%A8_%E0%B0%A4%E0%B1%86%E0%B0%B2%E0%B1%81%E0%B0%97%E0%B1%81_%E0%B0%AD%E0%B0%BE%E0%B0%97%E0%B0%B5%E0%B0%A4%E0%B0%AE%E0%B1%81/%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%A5%E0%B0%AE_%E0%B0%B8%E0%B1%8D%E0%B0%95%E0%B0%82%E0%B0%A7%E0%B0%AE%E0%B1%81')





















exit(0)
def iseng(s):
   return all(ord(c) < 128 for c in s)

def Parse(val0, val1, val2):
   Url = 'http://www.valmiki.iitk.ac.in/content?language=dv&field_kanda_tid=' + str(val0)+'&field_sarga_value=' + str(val1)+'&field_sloka_value=' + str(val2)
   idy = str(val0) + '.' + str(val1) + '.' + str(val2)
   pidy = str(val0) + '.' + str(val1) + '.' + str(val2 - 1)
   nidy = str(val0) + '.' + str(val1) + '.' + str(val2 + 1)
   #print Url
   html = urllib.urlopen(Url).read()
   html = html.replace('\r','')
   soup = BeautifulSoup.BeautifulSoup(html)
   DIV = soup.findAll('div', {'class' : 'field-content'})
   san = ''
   try:
      x = DIV[0].findAll(text = True)
   except IndexError:
      return None, None
   if(idy not in html):
      return None, None
   #if(pidy in html or nidy in html):
   #   return None, None
   L = len(x)
   for i in x:
      if(iseng(i)):
         continue
      first = str(i.encode('utf8'))
      for aa in xrange(-6, 6):
          for bb in xrange(-6, 6):
            first = first.replace(str(val0) + '.' + str(val1 + aa) + '.' + str(val2 + bb), '')
            first = first.replace(str(val0) + str(val1 + aa) + str(val2 + bb), '')
      first = first.replace('\xe0\xa5\xa4', '')
      if(i == x[-1]):
         first += '\xe0\xa5\xa4\xe0\xa5\xa4'
      else:
         first += '\xe0\xa5\xa4'
      san += first + ' '
   #san = DIV[0].findAll(text = True)[2]
   #print san
   #print "------"
   en = DIV[2].findAll(text = True)
   #print x[0]
   try:
      en = en[len(en) - 1]
   except Exception:
      return None, None
   san = san.strip()
   san = san.strip(' ')
   san = san.strip('\n')
   #san = san.decode('utf8')[:-2]
   #san = san.encode('utf8')
   #san = san.replace(str(val0) + '.' + str(val1) + '.' + str(val2), '')
   en = en.strip()
   en = en.strip('\n')
   
   #return None, None
   return san, en
   

x, en = Parse(1, 9, 9)
print x
print en
exit(0)
#try:
#   print "   en: <" + str(en) + '>'
#except UnicodeError:
#   en = en[:-2]
#print str(en.encode('utf8'))
#exit(0)
def main():
   Filename = 'sundarakanda'
   Mem = []
   for i in xrange(1, 69):
      Count = 0
      for j in xrange(1, 201):
         san, en = Parse(5, i, j)
         if((san, en) in Mem):
            continue
         else:
            Mem.append((san, en))
         if(len(Mem) >= 20):
            Mem = Mem[1:]
         print i, j
         print "   san: <" + str(san) + '>'
         try:
            print "   en: <" + str(en) + '>'
         except UnicodeError:
            en = str(en.encode('utf8'))
         if(san != None and en != None):
            f = open(Filename + '_sanskrit.txt', 'a+')
            f.write(san + '\n')
            f.close()
            f = open(Filename + '_english.txt', 'a+')
            f.write(en + '\n')
            f.close()
         else:
            Count += 1
            if(Count >= 20):
               break
main()