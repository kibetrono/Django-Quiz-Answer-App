import imp
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context={}
    return render(request, 'Question_app/index.html',context)

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    context={'profile': profile}
    return render(request, 'Question_app/profile.html', context)

