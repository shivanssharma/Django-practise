# from django.db import models

# # Create your models here.
# class React(models.Model): 
#     username = models.CharField(max_length=30) 
#     password = models.CharField(max_length=500)  

from django.db import models

class YourModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name