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
