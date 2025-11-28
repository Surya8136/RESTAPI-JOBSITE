from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Company(models.Model):
    company_name=models.CharField()
    area=models.CharField()
    description=models.TextField()
    CEO=models.CharField()
    contact=models.IntegerField()

    def __str__(self):
        return self.company_name

class Job(models.Model):
    job_title=models.CharField()
    location=models.CharField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='jobs')
    description=models.TextField()
    skills=models.CharField()
    experience=models.CharField()

    def __str__(self):
        return self.job_title

class CustomUser(AbstractUser):
    roles = [
        ('company','Company'),('employee','Employee')
    ]
    role=models.CharField(null=True,choices=roles)

    def __str__(self):
        return self.username
