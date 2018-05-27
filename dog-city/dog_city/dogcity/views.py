from django.shortcuts import render, get_object_or_404
from .models import Owner, Dog, Playdate, Attendance

def home_page(request):
    return render(request, 'dogcity/home_page.html')

def dog_list(request):
    dogs = Dog.objects.all()
    return render(request, 'dogcity/dog_list.html', {'dogs': dogs})

def dog_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'dogcity/dog_detail.html', {'dog': dog})

def playdate_list(request):
    playdates = Playdate.objects.all()
    return render(request, 'dogcity/playdate_list.html', {'playdates': playdates})

def playdate_detail(request, pk):
    playdate = get_object_or_404(Playdate, pk=pk)
    return render(request, 'dogcity/playdate_detail.html', {'playdate': playdate})
