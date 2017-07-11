from django.db import models
# from django.db import connection
# cursor = connection.cursor()

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=30)
#     headImg = models.FileField(upload_to='./upload/')
#     def __unicode__(self):
#         return self.username
'''
对应用户表
'''
class user(models.Model):
    # id = models.IntegerField(primary_key=True)
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    QQ = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    realname = models.CharField(max_length=255)
    IDcard = models.CharField(max_length=255)
    registertime = models.DateTimeField(auto_now_add=True)
    integrals = models.IntegerField()
'''
对应搜索表
'''
class search(models.Model):
    # id = models.IntegerField(primary_key=True)
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    searchstring = models.CharField(max_length=255)
    searchtime = models.DateTimeField(auto_now_add=True)

'''
对应动作表
'''
class action(models.Model):
    # id = models.IntegerField(primary_key=True)
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    fileid = models.IntegerField()
    actioncode = models.IntegerField()
    integralschange = models.IntegerField()
'''
对应文件表
'''
class file(models.Model):
    # id = models.IntegerField(primary_key=True)
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    filename = models.CharField(max_length=255)
    remotepath = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    uploadtime = models.DateTimeField(auto_now_add=True)