from django.forms import ModelForm
from . models import QuestionAnswer
class QuestionForm(ModelForm):
    class Meta:
        model=QuestionAnswer
        fields="__all__"
    