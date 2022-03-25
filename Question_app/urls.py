from django.urls import path,re_path
from . import views

urlpatterns=[
    # homepage
    path("", views.index, name="index"),
    # profile
    path("profile/", views.my_profile, name="profile"),
    path("profile/updateprofile/", views.update_profile_form, name="updateprofileform"),
    path("profile/update/", views.update_profile, name="updateprofile"),
    # add_question
    path('add_question',views.add_question,name='add_question'),
    path("search/", views.search, name="search"),

]