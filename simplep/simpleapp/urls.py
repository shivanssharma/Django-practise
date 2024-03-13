# from django.urls import path,re_path 
# from . import views

# urlpatterns=[
#     path('kasol',views.index,name='viewing'),
#     path('home',views.home,name='home chalo'),
#     path('date',views.display_date),
#     path('new',views.new),
#     path('naam/<name>/<id>',views.naam),
#     path('naam1/',views.naam1),
#     path('showform',views.showform),
#     path('food_items/<str:items>',views.dishname),
#     re_path(r'^menu_item/([0-9]{2})/$',views.menu_item),
# ]

#--------------------------------------------------------------------------------------------------------------------
# from django.urls import path,re_path 
# from . import views

# urlpatterns =[
#     path('/',views.home,name='home')
# ]

from django.urls import *
from .views import fetch_data

urlpatterns = [
    path('api/fetch-data/', fetch_data, name='fetch-data'),
    # Other URL patterns
]