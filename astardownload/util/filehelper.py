import os.path
import zipfile
import rarfile
import hashlib
import os

'''
文件扩展名
'''
def file_extension(path):
  return os.path.splitext(path)[1]

'''
zip/rar文件名列表
'''
def namelist(filepath):
    extension = file_extension(filepath)
    if extension.lower()== '.zip':
        z = zipfile.ZipFile(filepath, "r")
        #打印zip文件中的文件列表
        return z.namelist()
    elif extension.lower()== '.rar':
        z = rarfile.RarFile(filepath, "r")
        # 打印zip文件中的文件列表
        return z.namelist()
    else:
        return None
'''
    通过文件路径获得文件名(无论路径是否真正存在对应的文件)
'''
def get_file_name(filepath):
    strsplit = str(filepath).split('/')
    filename = strsplit[-1]
    return filename

'''
    通过加sha的方式重新命名文件
'''
def rename(filepath):
    splitext = os.path.splitext(filepath)
    sha1 = CalcSha1(filepath)
    new_name = str(splitext[0]) + '_' + sha1 + splitext[-1]
    return new_name

'''
计算文件SHA1
'''
def CalcSha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash

'''
计算文件MD5
'''
def CalcMD5(filepath):
    print(filepath)
    with open(filepath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
