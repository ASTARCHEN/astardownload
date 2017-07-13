# -*- coding: utf-8 -*-

from astardownload.util.ossClientHelper import *
import datetime
import astardownload.models as models
from astardownload.exception.astarDownloadException import OSSFileUploadException

def uploadfile(userid,uploadedfilepath,tag):
    strsplit = str(uploadedfilepath).split('/')
    # 取出文件名
    uploadedfilename = strsplit[len(strsplit)-1]
    if not tag.endswith('/'):
        tag += '/'
    remotefilename = tag + uploadedfilename
    try:

        # OSS上传
        oss_upload(remotefilename,uploadedfilepath)

    except OSSFileUploadException:
        # 上传失败
        errorString = str(OSSFileUploadException)
        return errorString
    else:
        mydatetime = datetime.datetime.now()
        # 上传成功
        # 有新文件上传，更新文件表
        obj = models.file(userid=userid, filename=uploadedfilename, remotepath=remotefilename, tag=tag,
                                         uploadtime=mydatetime)
        obj.save()

        fileid = obj.id
        # 用户上传了文件，应该获得积分，更新用户表
        integralschange = int(cp.get('integrals', 'integralschange'))
        obj = models.user.objects.get(id=userid)
        obj.integrals += integralschange
        obj.save()
        # 用户上传了文件，更新动作表
        ationcode = int(cp.get('actioncode', 'UPLOAD'))

        models.action.objects.create(userid=userid, fileid=fileid, actioncode=ationcode, integralschange=integralschange)


        return True