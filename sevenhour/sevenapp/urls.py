from django.urls import path 

from . import views

# urlpatterns =[
#     # path("<str:name>",views.index,name="index"),
#     # path('',views.myapp,name='login-page'),
#     path('room',views.room),
#     path('home',views.home),
#     path('sairam',views.sairam, name="sairam")
# ]
#----------------------------------------------------------------------
# api/urls.py

from django.urls import path, include

urlpatterns =[ 
    path('login/',views.login, name="login"),
    path('signup/',views.signup, name="signup")
]
