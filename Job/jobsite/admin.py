from django.contrib import admin

from jobsite.models import Company,Job,CustomUser

# Register your models here.
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(CustomUser)