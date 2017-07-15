import os.path
import zipfile
import rarfile
# 文件扩展名
def file_extension(path):
  return os.path.splitext(path)[1]

# zip/rar文件名列表
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
