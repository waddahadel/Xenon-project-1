from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Car
from django.db.models import Q
from django.views.generic import ListView,DetailView

# Create your views here.
class home(ListView):
    model=Car
    context_object_name='cars'
    queryset=Car.objects.all()
    template_name="main/home.html"

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        
        user=User.objects.create_user(username=username,password=password)
        user.save()
        auth.login(request,user)
        return redirect('home')
    else:
        return render(request,"main/register.html")


class carDetail(DetailView):

    model = Car
    template_name="main/details.html"
        
    