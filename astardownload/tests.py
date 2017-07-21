
from django.test import TestCase
from astardownload.util.filehelper import *
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import RegexAnalyzer
import time
# Create your tests here.

def test_filehelper():
  filepath = 'E:/cxl/snowland/astar/astardownload/util/filehelper.py'
  print(CalcSha1(filepath))
  print(CalcMD5(filepath))
  print(rename(filepath))

def test_namelist():
  filepath = 'E:/cxl/snowland/astar/astardownload/util/util.zip'
  print(namelist(filepath))

def test_whoosh():
    t1 = time.clock()
    analyzer = RegexAnalyzer(r"([\u4e00-\u9fa5])|[A-Z]|[a-z]|(\w+(\.?\w+)*)")
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
    ix = create_in("/", schema)
    writer = ix.writer()
    writer.add_document(title="First document", path="/a",
    content="This is the first document we’ve added!")
    writer.add_document(title="Second document", path="/b",
    content="The second one 你 中文测试中文 is even more interesting!")

    writer.add_document(title="Second document", path="/b",
    content="The third one 你测试中文")

    writer.add_document(title="Second document", path="/b",
    content="The forth one 测试你的中文")


    writer.add_document(title="1", path="/b",
    content="萤火虫")
    writer.add_document(title="2", path="/b",
    content="旅行商大框架萤火虫")
    writer.add_document(title="3", path="/b",
    content="粒子群看CAD是旅行商")
    writer.add_document(title="3", path="/b",
    content="旅行商粒子群看CAD是GSO")
    writer.commit()
    searcher = ix.searcher()
    # results = searcher.find("content", "first")
    # print(results[0]  )
    results = searcher.find("content", "GSO")
    t2 = time.clock()
    print(t2-t1)
    print(len(results))
    for i in range((len(results))):
        print(results[i])

if __name__ == '__main__':
    test_whoosh()

