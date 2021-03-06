from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=250, blank=True, null=True)
    profile_pic = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated_at','-created_at']

    def save_profile(self):
        self.save()

    def update_profile(self,name,email,profile_pic):
        self.name=name
        self.email=email
        self.profile_pic=profile_pic
        self.save()

    def delete_Profile(self):
        self.delete()

    def __str__(self):
        return self.name

class QuestionAnswer(models.Model):
    question=models.CharField(max_length=250,null=True)
    choice1=models.CharField(max_length=150,null=True)
    choice2=models.CharField(max_length=150,null=True)
    choice3=models.CharField(max_length=150,null=True)
    choice4=models.CharField(max_length=150,null=True)
    answer=models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated_at','-created_at']

    def save_question_answer(self):
        self.save()

    def update_question_answer(self,question,choice1,choice2,choice3,choice4,answer):
        self.question=question
        self.choice1=choice1
        self.choice2=choice2
        self.choice3=choice3
        self.choice4=choice4
        self.answer=answer
        self.save()

    def delete_question_answer(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        question = cls.objects.filter(question__icontains=search_term)
        return question

    def __str__(self):
        return self.question
