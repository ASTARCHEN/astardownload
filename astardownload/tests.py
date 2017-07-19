from django.test import TestCase
from astardownload.util.filehelper import *
# Create your tests here.

# if __name__ == '__main__':
#   filepath = 'E:/cxl/snowland/astar/astardownload/util/filehelper.py'
#   print(CalcSha1(filepath))
#   print(CalcMD5(filepath))
#   print(rename(filepath))

if __name__ == '__main__':
  filepath = 'E:/cxl/snowland/astar/astardownload/util/util.zip'
  print(namelist(filepath))