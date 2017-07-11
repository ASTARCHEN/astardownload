# -*- coding: utf-8 -*-

import oss2
import configparser
cp = configparser.ConfigParser()
cp.read('myconfig.conf')
accessKeySecret = cp.get('oss', 'accessKeySecret')
accessKeyId = cp.get('oss', 'accessKeyId')
endpoint = cp.get('oss', 'oss_endpoint')
bucketname = cp.get('oss', 'bucketname')


auth = oss2.Auth(accessKeyId, accessKeySecret)
service = oss2.Service(auth, endpoint=endpoint)

bucket = oss2.Bucket(auth=auth, bucket_name=bucketname, endpoint=endpoint, app_name='astar download')

def oss_upload(remotefilename, localfilename):
    bucket.put_object_from_file(remotefilename, localfilename)
def oss_download(remotefilename, localfilename):
    bucket.get_object_to_file(remotefilename, localfilename)