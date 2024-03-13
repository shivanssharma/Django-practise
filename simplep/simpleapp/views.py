# from django.shortcuts import render
# from datetime import datetime
# # Create your views here.
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("hello brother welcome to the new world")

# def home(request):
#     content="<html><h1>welcome to my world <h1><html>"
#     return HttpResponse(content)

# def display_date(request):
#     date_time=datetime.today().year
#     return HttpResponse(date_time)

# def new(request):
#     path=request.path
#     scheme=request.scheme 
#     method =request.method
#     address=request.META['REMOTE_ADDR']
#     user_agent=request.META['HTTP_USER_AGENT']
#     path_info=request.path_info   

#     response=HttpResponse()
#     response.headers['Age']=20

#     # response=HttpResponse("this actually works!")
#     msg =f"""
#         <br>Path:{path}
#         <br> Address:{address}
#         <br> Scheme:{scheme}
#         <br> method:{method}
#         <br> User agent:{user_agent}
#         <br> Path info:{path_info}
#         <br> response header:{response.headers}
# """
#     return HttpResponse(msg,content_type='text/html',charset='utf-8')
#     # return HttpResponse(path,content_type='text/html',charset='utf=8')
#     # return response

# #by path parameter
# # http://localhost:8000/next/name/John/1
# def naam(request,name,id):
#     return HttpResponse("Name:{}, <br>User id:{}".format(name,id))   

# #by query parameter
# # http://localhost:8000/next/name1/?name=John&id=1
# def naam1(request):
#     name=request.GET['name']
#     id=request.GET['id']
#     return HttpResponse("Name:{}, <br>User id:{}".format(name,id)) 

# #body parameter and form.html is made in html     
# def showform(request):
#     return render(request,'form.html'),


# #managing urls with params
# def dishname(request,items):
#     dishes={
#         'momo':'momo is very famous dish in the mountain region and mostly made by nepali.',
#         'thupka':'It is mostly ate in the snowy regions .',

#     }
#     description=dishes[items]
#     return HttpResponse(f"<h2>{items}<h2>"+description)

# #doing from regular expressions
# def menu_item(request,items):
#     dish={
#         'momo':'momo is very famous dish in the mountain region and mostly made by nepali.',
#         'thupka':'It is mostly ate in the snowy regions .',
#         'chutni':'It is mostly ate in the snowy regions .',
#     }
#     description=dish[items]
#     return HttpResponse(f"<h2>{items}<h2>"+description)

#-------------------------------------------------------------------------------------------------------

# from django.shortcuts import render
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse ("<h1>hello world</h1>")


#--------------------------------------------------------------
# from django.shortcuts import render
# from rest_framework.views import APIView
# from .models import React
# from rest_framework.response import Response  # Correct import statement
# from .serializers import ReactSerializer

# class ReactView(APIView):
#     serializer_class = ReactSerializer

#     def get(self, request):
#         details = [
#             {"name": detail.name, "detail": detail.detail}
#             for detail in React.objects.all()
#         ]
#         return Response(details)  # Corrected variable name here

#     def post(self, request):
#         serializer = ReactSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)  # Corrected variable name here




from django.http import JsonResponse
from .models import YourModel

def fetch_data(request):
    # Retrieve data from the database
    data = YourModel.objects.all()

    # Serialize data into JSON format
    serialized_data = [{'id': item.id, 'name': item.name} for item in data]

    # Return JSON response
    return JsonResponse(serialized_data, safe=False)


