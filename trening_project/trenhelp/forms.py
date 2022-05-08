from django import forms
from django.contrib.auth.models import User
from trenhelp.models import Profile,Training
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreateProfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age']
    
class CreateTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['name','date_created']

        