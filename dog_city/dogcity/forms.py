from django import forms
from .models import Owner, Dog, Walk
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import CheckboxSelectMultiple

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'age', 'breed', 'personality', 'instructions', 'photo_url', 'owner',)

class WalkForm(forms.ModelForm):
    class Meta:
        model = Walk
        fields = ('date', 'day', 'dogs',)
        widgets = {'dogs': CheckboxSelectMultiple}

        def __init__(self, *args, **kwargs):
            super(WalkForm, self).__init__(*args, **kwargs)                    
            self.fields['dogs'].widget = CheckboxSelectMultiple()
            self.fields['dogs'].queryset = Dog.objects.all()
        # fields = ('day', 'date', 'dogs',)

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'zipcode',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)