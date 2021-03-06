
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
import os
import sys
import json
import configparser
from astardownload.util.downloadhelper import big_file_download
from astardownload.util.uploadhelper import uploadfile
from astardownload.util.sms import send_sms
# from astardownload.util.uploadhelper import uploadfile
from django.http import StreamingHttpResponse

cp = configparser.ConfigParser()
cp.read('myconfig.conf')

class UserForm(forms.Form):
    # TODO(A.Star) 需要重新定义用户信息
    username = forms.CharField()
    password = forms.PasswordInput()
    passwordagain = forms.PasswordInput()

class RegisterForm(forms.Form):

    pass




class UserFormUpload(forms.Form):
    myfile = forms.FileField()

'''
    注册
'''
def do_register(req):
    # TODO(A.Star) 需要重写注册
    if req.method == 'POST':
        # form = UserForm(req.POST)
        # if form.is_valid():
        #
        #     print(form.cleaned_data)
        #     return HttpResponse('ok')
        realname = req.POST.get('realname')
        phone = req.POST.get('phone')
        if req.POST.get('button') == '获取验证码':
            yzm = '【253云通讯】您的验证码为1234'
            # TODO(A.Star) 需要验证验证码是否正常发送
            json_str = send_sms(text=yzm,phone=phone).decode()
            data = json.loads(json_str)
            # return HttpResponse(data[''])
        elif req.POST.get('button') == '完成':
            # TODO(A.Star) 需要判断完成之后的动作
            pass

        return render_to_response(cp.get('html','register'),{'phone':phone, 'realname':realname, 'yzm':""})
    # else:
    #     form = UserForm()
    # return render_to_response(cp.get('html','register'),{'form':form})
    else:
        # 开始时候GET的界面
        phone = ""
        realname = ""
        yzm = ""
        return  render_to_response(cp.get('html','register'),{'phone':phone, 'realname':realname, 'yzm':yzm})



def do_upload(req):
    # TODO(A.Star) 添加MD5重复检测功能
    # TODO(A.Star) 需要传进用户id
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
    # TODO(A.Star） 需要重写登录操作
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
'''
管理员界面
'''
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
'''
主页
'''
def index(req):
    if req.method == "GET":
        return render_to_response(cp.get('html','index'))
    elif req.method == "POST":
        pass
'''
个人信息页
'''
def myzone(req):
    userid = int(req.GET.get('userid', -1))
    if req.method == 'GET':
        if userid == -1:
            return render_to_response(cp.get('html', 'myzone'))
        else:
            return render_to_response(cp.get('html', 'myzone'), {'userid': userid})
    elif req.method == 'POST':
        pass




