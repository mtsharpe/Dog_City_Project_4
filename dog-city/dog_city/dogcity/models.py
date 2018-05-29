from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    zipcode = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
    created_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    dogs = models.ManyToManyField(Dog)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.location

class Attendance(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='attending')
    playdate = models.ForeignKey(Playdate, on_delete=models.CASCADE, related_name='attending')

    def __str__(self):
        return f'{self.dog.name} {self.playdate}'
    


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Owner.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Owner.objects.create(user=instance)
#     instance.profile.save()