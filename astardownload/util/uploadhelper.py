# -*- coding: utf-8 -*-

from astardownload.util.ossClientHelper import *
import datetime
import astardownload.models as models
from astardownload.exception.astarDownloadException import OSSFileUploadException
from astardownload.util.filehelper import get_file_name, rename, CalcMD5

'''
上传文件
'''
def uploadfile(userid,uploadedfilepath,tag):
    # 取出文件名
    uploadedfilename = get_file_name(uploadedfilepath)
    if not tag.endswith('/'):
        tag += '/'
    # 更新文件名
    newuploadedfilepath = rename(uploadedfilepath)
    newuploadedfilename = get_file_name(newuploadedfilepath)
    remotefilename = tag + newuploadedfilename

    md5 = CalcMD5(uploadedfilepath)
    if check_exist(md5):
        errorString = '文件重复上传，请保证原创'
        return errorString
    else:
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
                                             uploadtime=mydatetime,md5=md5, abstract='', eabstract='')
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


'''
检验是否有同样的文件上传过
'''
def check_exist(file_md5):
    try:
        models.file.objects.get(md5=file_md5)
        return True
    except BaseException:
        return False