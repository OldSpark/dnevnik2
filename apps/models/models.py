from django.db import models
from django.contrib.auth.models import User
from apps.models import settings as ns
import datetime


class City(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __unicode__(self):
        return self.name
    
class Organization(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.name

class School(models.Model):    
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City)
    address = models.CharField(max_length = 255, blank = True, null = True)
    mobile = models.CharField(max_length = 20, blank = True, null = True)
    org = models.ForeignKey(Organization)
    
    def __unicode__(self):
        return self.name

class School_info(models.Model):
    school = models.OneToOneField(School)
    teachers_number = models.IntegerField(default = 0)
    students_number = models.IntegerField(default = 0)
    parents_number = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.school.name
    
class Student(models.Model):
    user_id = models.OneToOneField(User)    
    school = models.ForeignKey(School)
    
    def __unicode__(self):
        return self.user_id.username
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student)
    
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    
    email = models.EmailField(max_length = 40,blank = True,)
    mobile =  models.CharField(max_length = 255, blank = True, null = True)
    address = models.CharField(max_length = 255, blank = True, null = True)    
    birth = models.DateField(blank = True, default=datetime.datetime.now)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length = 255, blank = True, null = True)

    def __unicode__(self):
        return self.teacher.user_id.username
    
class Teacher(models.Model):
    user_id = models.OneToOneField(User)    
    school = models.ForeignKey(School)
    
    def __unicode__(self):
        return self.user_id.username
    
class TeacherProfile(models.Model):
    teacher = models.OneToOneField(Teacher)
    
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    
    email = models.EmailField(max_length = 40,blank = True,)
    mobile =  models.CharField(max_length = 255, blank = True, null = True)
    address = models.CharField(max_length = 255, blank = True, null = True)        
    birth = models.DateField(blank = True, default=datetime.datetime.now)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length = 255, blank = True, null = True)

    def __unicode__(self):
        return self.teacher.user_id.username

class Parent(models.Model):
    user = models.OneToOneField(User)    
    school = models.ForeignKey(School)
    child = models.OneToOneField(Student)
    
    def __unicode__(self):
        return self.user.username
    
    
    
class ParentProfile(models.Model):
    parent = models.OneToOneField(Parent)
    
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    
    email = models.EmailField(max_length = 40,blank = True,)
    mobile =  models.CharField(max_length = 255, blank = True, null = True)
    address = models.CharField(max_length = 255, blank = True, null = True)        
    birth = models.DateField(blank = True, default=datetime.datetime.now)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length = 255, blank = True, null = True)
    
class Temporary(models.Model):
    username = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    school = models.ForeignKey(School)
    city = models.ForeignKey(City)
    
    role = models.IntegerField(choices = ns.USER_POSITIONS, default = ns.STUDENT_POSITION)
    
    def __unicode__(self):
        return self.username
    
    