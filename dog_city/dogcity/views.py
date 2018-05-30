from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Owner, Dog, Walk
from .forms import DogForm, WalkForm, OwnerForm, SignUpForm
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, 'dogcity/home_page.html')

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'dogcity/owner_list.html', {'owners': owners})

@login_required
def owner_detail(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    return render(request, 'dogcity/owner_detail.html', {'owner': owner})

@login_required
def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', pk=owner.pk)
    else: 
        form = OwnerForm()
    return render(request, 'dogcity/owner_create.html', {'form': form})

@login_required
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

@login_required
def owner_delete(request, pk):
    Owner.objects.get(id=pk).delete()
    return redirect('owner_list')
    
def dog_list(request):
    dogs = Dog.objects.all().order_by('name')
    return render(request, 'dogcity/dog_list.html', {'dogs': dogs})

@login_required
def dog_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'dogcity/dog_detail.html', {'dog': dog})

@login_required
def dog_create(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            dog = form.save()
            return redirect('dog_detail', pk=dog.pk)
    else:
        form = DogForm()
    return render(request, 'dogcity/dog_create.html', {'form': form})

@login_required
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

@login_required
def dog_delete(request, pk):
    Dog.objects.get(id=pk).delete()
    return redirect('dog_list')

def walk_list(request):
    walks = Walk.objects.all().order_by('date')
    return render(request, 'dogcity/walk_list.html', {'walks': walks})

@login_required
def walk_detail(request, pk):
    walk = get_object_or_404(Walk, pk=pk)
    return render(request, 'dogcity/walk_detail.html', {'walk': walk})

@login_required
def walk_create(request):
    if request.method == 'POST':
        form = WalkForm(request.POST)
        if form.is_valid():
            walk = form.save()
            walk.publish()
            return redirect('walk_detail', pk=walk.pk)
    else:
        form = WalkForm()
    return render(request, 'dogcity/walk_create.html', {'form': form})

@login_required
def walk_edit(request, pk):
    walk = Walk.objects.get(pk=pk)
    if request.method == 'POST':
        form = WalkForm(request.POST, instance=walk)
        if form.is_valid():
            walk = form.save()
            return redirect('walk_detail', pk=walk.pk)
    else: 
        form = WalkForm(instance=walk)
    return render(request, 'dogcity/walk_create.html', {'form': form})

@login_required
def walk_delete(request, pk):
    Walk.objects.get(id=pk).delete()
    return redirect('walk_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'dogcity/signup.html', {'form': form})


# def add_attendance(request, playdate_id, dog_id):
#     walk = Walk.objects.get(id=walk_id)
#     dog = Dog.objects.get(id=dog_id)
#     Attendance.objects.create(wal=playdate, dog=dog)
#     return redirect('playdate_detail', pk=playdate.pk)

# def remove_attendance(request, playdate_id, dog_id):
#     playdate = Playdate.objects.get(id=playdate_id)
#     dog = Dog.objects.get(id=dog_id)
#     Attendance.objects.get(playdate=playdate, dog=dog_id).delete()
#     return redirect('playdate_detail', pk=playdate.pk)    