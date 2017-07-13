import datetime

class OSSFileDownloadException(BaseException):
    def __init__(self, uploadedfilename):
        self.uploadedfilename = uploadedfilename
    def __str__(self):
        mydatetime = datetime.datetime.now()
        timeString = mydatetime.strftime('%Y-%m-%d %H:%M:%S')
        errorString = 'oss upload ' + self.uploadedfilename + ' failed at ' + timeString
        return errorString
class OSSFileUploadException(BaseException):
    def __init__(self, downloadedfilename):
        self.downloadedfilename = downloadedfilename
    def __str__(self):
        mydatetime = datetime.datetime.now()
        timeString = mydatetime.strftime('%Y-%m-%d %H:%M:%S')
        errorString = 'oss download ' + self.downloadedfilename + ' failed at ' + timeString
        return errorString
