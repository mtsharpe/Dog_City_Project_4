from django import forms
from .models import Owner, Dog, Playdate, Attendance
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'age', 'breed', 'personality', 'photo_url', 'owner',)

class PlaydateForm(forms.ModelForm):
    class Meta:
        model = Playdate
        fields = ('location', 'description', 'date', 'time', 'dogs',)

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'email', 'zipcode',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)