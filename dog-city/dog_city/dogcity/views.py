from django.shortcuts import render, get_object_or_404, redirect
from .models import Owner, Dog, Playdate, Attendance
from .forms import DogForm, PlaydateForm, OwnerForm

def home_page(request):
    return render(request, 'dogcity/home_page.html')

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'dogcity/owner_list.html', {'owners': owners})

def owner_detail(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    return render(request, 'dogcity/owner_detail.html', {'owner': owner})

def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', pk=owner.pk)
    else: 
        form = OwnerForm()
    return render(request, 'dogcity/owner_create.html', {'form': form})

def owner_edit(request, pk):
    owner = Owner.objects.get(pk=pk)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', pk=owner.pk)
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'dogcity/owner_create.html', {'form': form})

def owner_delete(request, pk):
    Owner.objects.get(id=pk).delete()
    return redirect('owner_list')
    
def dog_list(request):
    dogs = Dog.objects.all().order_by('name')
    return render(request, 'dogcity/dog_list.html', {'dogs': dogs})

def dog_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'dogcity/dog_detail.html', {'dog': dog})

def dog_create(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            dog = form.save()
            return redirect('dog_detail', pk=dog.pk)
    else:
        form = DogForm()
    return render(request, 'dogcity/dog_create.html', {'form': form})

def dog_edit(request, pk):
    dog = Dog.objects.get(pk=pk)
    if request.method == 'POST':
        form = DogForm(request.POST, instance=dog)
        if form.is_valid():
            dog = form.save()
            return redirect('dog_detail', pk=dog.pk)
    else: 
        form = DogForm(instance=dog)
    return render(request, 'dogcity/dog_create.html', {'form': form})

def dog_delete(request, pk):
    Dog.objects.get(id=pk).delete()
    return redirect('dog_list')

def playdate_list(request):
    playdates = Playdate.objects.all()
    return render(request, 'dogcity/playdate_list.html', {'playdates': playdates})

def playdate_detail(request, pk):
    playdate = get_object_or_404(Playdate, pk=pk)
    return render(request, 'dogcity/playdate_detail.html', {'playdate': playdate})

def playdate_create(request):
    if request.method == 'POST':
        form = PlaydateForm(request.POST)
        if form.is_valid():
            playdate = form.save()
            return redirect('playdate_detail', pk=playdate.pk)
    else:
        form = PlaydateForm()
    return render(request, 'dogcity/playdate_create.html', {'form': form})

def playdate_edit(request, pk):
    playdate = Playdate.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlaydateForm(request.POST, instance=playdate)
        if form.is_valid():
            playdate = form.save()
            return redirect('playdate_detail', pk=playdate.pk)
    else: 
        form = PlaydateForm(instance=playdate)
    return render(request, 'dogcity/playdate_create.html', {'form': form})

def playdate_delete(request, pk):
    Playdate.objects.get(id=pk).delete()
    return redirect('playdate_list')

def add_attendance(request, playdate_id, dog_id):
    playdate = Playdate.objects.get(id=playdate_id)
    dog = Dog.objects.get(id=dog_id)
    Attendance.objects.create(playdate=playdate, dog=dog)
    return redirect('playdate_detail', pk=playdate.pk)

def remove_attendance(request, playdate_id, dog_id):
    playdate = Playdate.objects.get(id=playdate_id)
    dog = Dog.objects.get(id=dog_id)
    Attendance.objects.get(playdate=playdate, dog=dog_id).delete()
    return redirect('playdate_detail', pk=playdate.pk)    