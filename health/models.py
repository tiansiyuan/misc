# -*- coding:utf-8 -*-
from django.db import models

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

class Doctor(models.Model):
    """
    医生
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    specialty = models.IntegerField(choices = SPECIALTY_CHOICES)

class Disease(models.Model):
    """
    疾病
    """
    name = models.IntegerField(choices = DISEASE_CHOICES)

class Patient(models.Model):
    """
    患者
    """
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)    
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    doctor = models.ForeignKey(Doctor)
    disease = models.ForeignKey(Disease)

class Equipment(models.Model):
    """
    设备
    """
    name = models.CharFields(max_length=60)

class Site(models.Model):
    """
    检查地点
    """
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    equipment = models.ForeignKey(Equipment)

class Check(models.Model):
    """
    检查
    """
    site = models.ForeignKey(Site)
    date = models.DateField()
    patient = models.ForeignKey(Patient)

class Index(models.Model):
    """
    指标
    """
    name = models.CharField(max_length=50)
    value = models.FloatField()
    min_value = models.FloatField()
    max_value = models.FloatField()

class CheckItem(models.Model):
    """
    检查项目
    """
    check = models.ForeignKey(Check)
    index = models.ForeignKey(Index)

class Comment(models.Model):
    """
    """
    content = models.IntegerField(choices = COMMENT_CHOICES)
    addon = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)
    datetime = models.DateTimeField()
