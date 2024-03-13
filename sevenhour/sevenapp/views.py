# from django.shortcuts import render
# from django.http import HttpResponse,HttpRequest
# # Create your views here.
# # def home(request):
# #     return render(request,'sevenapp/home.html')

# # def room(request):
# #     return render(request,'sevenapp/room.html')

# # def sairam(request):
# #     return render(request,'sevenapp/sairam.html')
# #-----------------------------------------------------

# def index(request):
#     return HttpResponse("<h1>Sairam</h1>")

# def feb(request):
#     return HttpResponse("<h1>jai sai Sairam</h1>")

# def monthly_challenge(request,month):
#     challenge_text=None
#     if month=="jan":
#         challenge_text="sairam jan"
#     elif month=="feb":
#         challenge_text="sairam march"
#     elif month=="march":
#         challenge_text="sairam march"
#     elif month=="april":
#         challenge_text="sairam april"
#     elif month=="may":
#         challenge_text="sairam may"
#     elif month=="june":
#         challenge_text="sairam june"
#     elif month=="july":
#         challenge_text="sairam july"
#     elif month=="sep":
#         challenge_text="sairam sep"
#     return HttpResponse(challenge_text)    



#------------------------------------------------------------------------------------
# api/views.py
# views.py
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        # Add validation and error handling as needed
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': 'Signup successful'})



