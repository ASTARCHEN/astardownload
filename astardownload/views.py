
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
import configparser
import logging

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
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse('ok')
    else:
        form = UserForm()
    return render_to_response(cp.get('html','register'),{'form':form})

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
            fp = open(prefix_upload+myfile_name,'wb')
            fp.write(myfile.read())
            fp.close()
            return HttpResponse('ok')
    else:
        uf = UserFormUpload()
    mystr = cp.get('html','upload')
    print(mystr)
    return render_to_response(mystr, {'uf': uf})

def do_login(req):
    pass

def do_download(req):
    pass

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