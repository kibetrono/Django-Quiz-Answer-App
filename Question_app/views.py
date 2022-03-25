import imp
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,QuestionAnswer
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.contrib.auth.models import User
from .forms import QuestionForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == 'POST':
        questions=QuestionAnswer.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
        percent = score/total *100
        context = {'score':score,'time': request.POST.get('timer'),'correct':correct,'wrong':wrong,'percent':percent,'total':total}
        return render(request,'Question_app/result.html',context)
    else:
        questions=QuestionAnswer.objects.all()
        context = {
            'questions':questions
        }
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


# def add_question(request):
#     form=QuestionForm()
#     if(request.method=='POST'):
#         form_results=QuestionForm(request.POST)
#         if form_results.is_valid():
#             form_results.save()
#             return redirect('/')
#     context={'form':form}
#     return render(request,'Question_app/add_question.html',context)

 
def add_question(request): 

    if request.user.is_staff:
        form=QuestionForm()
        if(request.method=='POST'):
            form_results=QuestionForm(request.POST)
            if form_results.is_valid():
                form_results.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Question_app/add_question.html',context)
    else: 
        return redirect('home')

@login_required(login_url="/accounts/login/")
def search(request):
    questions = QuestionAnswer.objects.all()
    if 'query' in request.GET and request.GET["query"]:
        search_term = request.GET.get("query")
        searched_results = QuestionAnswer.objects.filter(question__icontains=search_term)
        message = f"Search For: {search_term}"
        context = {"message": message, "businesses": searched_results}
        return render(request, "Question_app/search.html", context)
    else:
        message = "You haven't searched for any term"
        context = {"message": message,'questions':questions}
        return render(request, "Question_app/search.html", context)