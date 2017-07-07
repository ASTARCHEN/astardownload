from django.test import TestCase
import configparser
# Create your tests here.
import urllib

cp = configparser.ConfigParser()
cp.read('myconfig.conf')

url = 'http://www.jb51.net/test/demo.zip'
# f = urllib.urlopen(url)
# data = f.read()
# with open(cp.get('dirs','prefix_upload')+"/demo2.zip", "wb") as code:
#     code.write(data)

f = urllib.urlopen(url)
with open("demo2.zip", "wb") as code:
  code.write(f.read())