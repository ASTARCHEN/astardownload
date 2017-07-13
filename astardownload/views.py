
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
import os
import sys
import configparser
from astardownload.util.downloadhelper import big_file_download
from astardownload.util.uploadhelper import uploadfile
from django.http import StreamingHttpResponse

cp = configparser.ConfigParser()
cp.read('myconfig.conf')
# Create your views here.
class UserForm(forms.Form):
    name = forms.CharField()

class UserFormUpload(forms.Form):
    myfile = forms.FileField()
'''
    注册
'''
def do_register(req):
    pass
    # if req.method == 'POST':
    #     form = UserForm(req.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         return HttpResponse('ok')
    # else:
    #     form = UserForm()
    # return render_to_response(cp.get('html','register'),{'form':form})

def do_upload(req):

    if req.method == 'POST':
        uf = UserFormUpload(req.POST, req.FILES)
        if uf.is_valid():
            # 得到uploadedfile类型的文件对象
            myfile = uf.cleaned_data['myfile']
            prefix_upload = cp.get('dirs','prefix_upload')
            # 得到文件名
            myfile_name = myfile.name
            # fp = file(prefix_upload + myfile_name, 'wb')
            localpath = prefix_upload+myfile_name
            fp = open(localpath,'wb')
            fp.write(myfile.read())

            fp.close()
            fp = open(localpath,'rb')
            # 绝对路径获取
            abspath = os.path.abspath(sys.argv[0])
            abspath = os.path.dirname(abspath) + cp.get('dirs', 'abspath_upload')+'/'
            print(abspath)
            print(abspath+myfile_name)
            resstr = uploadfile(0,abspath+myfile_name,'matlab/test/test')
            fp.close()
            return HttpResponse(resstr)
    else:
        uf = UserFormUpload()
    mystr = cp.get('html','upload')
    print(mystr)
    return render_to_response(mystr, {'uf': uf})

def do_login(req):
    pass

def do_download(req):
    fileid = int(req.GET.get('fileid', -1))
    res = big_file_download(fileid)
    if res is None:
        resstr = 'remote file is not found'
        response = HttpResponse(resstr)
    else:
        obj2 = res['file_obj']
        the_file_name = res['file_name']
        response = StreamingHttpResponse(obj2)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response

def do_admin(req):
    if req.method == 'POST':
        uf = UserFormUpload(req.POST, req.FILES)
        if uf.is_valid():
            # 得到uploadedfile类型的文件对象
            myfile = uf.cleaned_data['myfile']
            prefix_upload = cp.get('dirs','prefix_upload')
            # 得到文件名
            myfile_name = myfile.name
            # fp = file(prefix_upload + myfile_name, 'wb')
            fp = open(prefix_upload+myfile_name,'wb')
            fp.write(myfile.read())
            fp.close()

            return HttpResponse('ok')
    else:
        uf = UserFormUpload()
    mystr = cp.get('html','upload')
    print(mystr)
    return render_to_response(mystr, {'uf': uf})

def index(req):
    return render_to_response(cp.get('html','index'))

def myzone(req):
    pass





