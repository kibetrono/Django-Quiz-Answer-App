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

@login_required(login_url='/accounts/login/')
def update_profile_form(request):

    context={}
    return render(request, 'Question_app/updateProfile.html',context)

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == "POST":
        current_user = request.user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        bio = request.POST["bio"]
        name = request.POST["first_name"] + " " + request.POST["last_name"]

        profile_image = request.FILES["profile_pic"]
        profile_image = cloudinary.uploader.upload(profile_image)
        profile_url = profile_image["url"]
        user = User.objects.get(id=current_user.id)
        if Profile.objects.filter(user_id=current_user.id).exists():

            profile = Profile.objects.get(user_id=current_user.id)
            profile.profile_pic = profile_url
            profile.save()
        else:
            profile = Profile(user_id=current_user.id,name=name,profile_pic=profile_url)

            profile.save_profile()

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.bio=bio
        user.save()
        return redirect("/profile")
    else:
        return render(request, "Question_app/profile.html")
