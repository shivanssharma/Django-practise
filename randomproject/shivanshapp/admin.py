from django.contrib import admin

# Register your models here.
from .models import student,college,job,placement,training


admin.site.register(student)
admin.site.register(college)
admin.site.register(job)
admin.site.register(placement)
admin.site.register(training)
