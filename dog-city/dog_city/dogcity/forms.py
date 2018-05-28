from django import forms
from .models import Owner, Dog, Playdate, Attendance

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'age', 'breed', 'personality', 'photo_url', 'owner',)

class PlaydateForm(forms.ModelForm):
    class Meta:
        model = Playdate
        fields = ('created_date', 'location', 'description', 'date', 'time',)

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('user', 'first_name', 'last_name', 'email', 'zipcode',)

       