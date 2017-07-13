import os, tempfile, zipfile
import datetime
import sys
import astardownload.models as models
from astardownload.util.ossClientHelper import *
from django.http import StreamingHttpResponse
#
def big_file_download(fileid):
    # do something...
    fileid = int(fileid)
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    # 通过fileid获得文件名
    if fileid != -1:
        obj = models.file.objects.get(id=fileid)
        the_file_name = obj.filename
        abspath = os.path.abspath(sys.argv[0])
        abspath = os.path.dirname(abspath) + cp.get('dirs', 'abspath_upload') + '/'
        localpath = abspath + the_file_name
        if not os.path.isfile(localpath):
            remotepath = obj.remotepath;
            try:
                oss_download(remotepath, localpath)
            except BaseException:
                return None
        res = [];
        res = {'file_obj':file_iterator(localpath),'file_name': the_file_name}
        return res
    else:
        # 没有对应的文件
        # do sth...
        pass
    return None



