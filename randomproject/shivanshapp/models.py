from django.db import models
import uuid
# Create your models here.

#placement cell management 

# student model
class student (models.Model):
    student_id=models.IntegerField(primary_key=True)
    first_name=models.TextField(max_length=100)
    last_name_name=models.TextField(max_length=100)
    state=models.TextField(max_length=100)
    city=models.TextField(max_length=100)
    email=models.TextField(max_length=100)
    
# college model
class college(models.Model):
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    college_id=models.IntegerField(primary_key=True)    
    name_of_college=models.TextField(max_length=200)
    name_of_college=models.TextField(max_length=200)
    state=models.TextField(max_length=100)
    city=models.TextField(max_length=100)
    courses=models.TextField(max_length=100)

# job model
class job(models.Model):
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    college_id=models.ForeignKey(college,on_delete=models.CASCADE)  
    job_id=models.IntegerField(primary_key=True)  
    company_name=models.TextField(max_length=200)
    job_name=models.TextField(max_length=200)
    salary=models.IntegerField()    
    
# placement 
class placement(models.Model):
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    college_id=models.ForeignKey(college,on_delete=models.CASCADE)  
    placement_id=models.IntegerField(primary_key=True)  
    qualification_requirement=models.TextField(max_length=200)

class training(models.Model):
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    training_id=models.IntegerField(primary_key=True)  
    training_name=models.TextField(max_length=200)    
    training_period=models.IntegerField()