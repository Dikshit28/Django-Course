from django.shortcuts import render

# Create your views here.
def sign_in(request):
    return render(request,"login/landing.html",{})

def sign_up(request):
    #To do: Create a sign up page.
    pass