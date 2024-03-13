# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
#     email = models.EmailField(unique=True) 
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     # Specify the unique identifier for authentication
#     USERNAME_FIELD = 'username'

# models.py

# from django.contrib.auth.models import User

# No need to define a custom user model, just use the built-in User model
