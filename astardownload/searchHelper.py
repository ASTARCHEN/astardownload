
#一个完整的演示  
#!/usr/bin/env python  
# -*- coding: UTF-8 -*-  
import pymysql
from whoosh.analysis import RegexAnalyzer
from whoosh.fields import *
from whoosh.index import create_in

from astardownload.dbHelper import *


def search_file(search_string):
    analyzer = RegexAnalyzer(r"([\u4e00-\u9fa5])|[A-Z]|[a-z]|(\w+(\.?\w+)*)")
    print(db_name)
    conf={'host': db_host,
     'port': int(db_port),
     'user': db_user,
     'password': db_password,
     'database': db_name,
     }
    conn = pymysql.Connect(**conf)

    cursor = conn.cursor()
    mylen = cursor.execute("select id,abstract,eabstract from astardownload_file")
    file_table = cursor.fetchall()
    schema = Schema(id=ID(stored=True),abstract=TEXT(stored=True, analyzer=analyzer),eabstract=TEXT(stored=True, analyzer=analyzer))
    # schema = Schema(path=TEXT(stored=True), id=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
    ix = create_in("/", schema)
    writer = ix.writer()
    for i in xrange(mylen):
        item = file_table[i]
        writer.add_document(id=str(item[0]),abstract=str(item[1]),eabstract=str(item[2]));
    writer.commit()
    searcher = ix.searcher()
    # results = searcher.find("content", "first")
    # print(results[0]  )
    results = searcher.find("abstract", "GSO")
    return results

if __name__ == '__main__':
    search_file('123')