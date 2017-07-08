from django.test import TestCase
import configparser
# import urllib2 python2
import urllib.request as urllib2
# Create your tests here.



cp = configparser.ConfigParser()
cp.read('myconfig.conf')

url = 'http://localhost/astardownlaod/uplaod/'
# f = urllib.urlopen(url)
# data = f.read()
# with open(cp.get('dirs','prefix_upload')+"/demo2.zip", "wb") as code:
#     code.write(data)

f = urllib2.urlopen(url)
with open("demo2.zip", "wb") as code:
  code.write(f.read())