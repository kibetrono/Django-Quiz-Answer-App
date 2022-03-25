from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import QuestionAnswer,Profile
from django.contrib.auth.models import User


class QuestionTestClass(TestCase):
    def setUp(self):
        self.question = QuestionAnswer(question="New question",choice1="choice1",choice2="choice2",
        choice3="choice3",choice4="choice4",answer="answer 1")
        self.question.save_question_answer()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.question, QuestionAnswer))

    def test_save_method(self):
        self.question.save_question_answer()
        quizes = QuestionAnswer.objects.all()
        self.assertTrue(len(quizes) > 0)

    def test_delete_method(self):
        self.question.save_question_answer()
        self.question.delete()
        quizes =QuestionAnswer.objects.all()
        self.assertTrue(len(quizes) == 0)



class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        user = User.objects.create(username='kibet',first_name='rono',last_name='David')

        self.profile=Profile.objects.create(user=user,name="Kibet",email="kibetdavidro@gmail.com",profile_photo='lorem2.png',bio="New description")
        self.profile.save_profile()

    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        """Testing Save Method"""
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) < 1)

    def tearDown(self):
        """tearDown method"""
        Profile.objects.all().delete()
