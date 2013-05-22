# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('M', u'男'),
    ('F', u'女'),
)

SPECIALTY_CHOICES = (
    (1, u'内科'),
    (2, u'外科'),
    (3, u'妇科'),
    (4, u'牙科'),
)


DISEASE_CHOICES = (
    (1, u'肝病'),
    (2, u'肺病'),
    (3, u'心脏病'),
    (4, u'肾病'),
)

COMMENT_CHOICES = (
    (1, u'尽快见医生'),
    (2, u'减药'),
    (3, u'加药'),
    (4, u'继续按量服药'),
)

class CommonUser(models.Model):
    user = models.OneToOneField(User)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        abstract = True

class Doctor(CommonUser):
    """
    医生
    """
    specialty = models.IntegerField(choices = SPECIALTY_CHOICES)

    def __unicode__(self):
        return self.user.username

class Patient(CommonUser):
    """
    患者
    """
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)    
    doctor = models.ForeignKey(Doctor)
    disease = models.CharField(max_length=2, choices=DISEASE_CHOICES)

    def __unicode__(self):
        return self.user.username

class Equipment(models.Model):
    """
    体检设备
    暂忽略
    """
    name = models.CharField(max_length=60)

class Site(models.Model):
    """
    体检地点
    暂忽略
    """
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    equipment = models.ForeignKey(Equipment)

class Check(models.Model):
    """
    体检
    """
    # site = models.ForeignKey(Site)
    date = models.DateField()
    patient = models.ForeignKey(Patient)

class Index(models.Model):
    """
    体检指标
    """
    name = models.CharField(max_length=50)
    value = models.FloatField()
    min_value = models.FloatField()
    max_value = models.FloatField()
    unit = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class CheckItem(models.Model):
    """
    体检项目
    """
    check = models.ForeignKey(Check)
    index = models.ForeignKey(Index)

class Comment(models.Model):
    """
    医生的反馈
    """
    content = models.IntegerField(choices = COMMENT_CHOICES)
    addon = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)
    datetime = models.DateTimeField()
