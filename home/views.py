from django.shortcuts import render


def home_view(request):
     return render(request , 'home/home.html')
# Create your views here.
def success_view(request):
     return render(request, 'home/success.html')