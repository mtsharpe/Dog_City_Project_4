from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    zipcode = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    breed = models.CharField(max_length=100)
    personality = models.TextField()
    photo_url = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='dogs')

    def __str__(self):
        return self.name

class Playdate(models.Model):
    created_date = models.DateTimeField(default=timezone.now())
    location = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.location

class Attendance(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='attending')
    playdate = models.ForeignKey(Playdate, on_delete=models.CASCADE, related_name='attending')

    def __str__(self):
        return self.dog.name
    