from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import volunteer_profiles, volunteerform
from .models import volunteer_profiles



def addvolunteer(request):

    form = volunteerform()
    if request.method == "POST":
        form = volunteerform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("volunteers:index"))
    return render(request,"volunteers/add.html",{"form":form})

def index(request):
    volunteers = volunteer_profiles.objects.all().order_by('-volunteer_no')
    return render(request,"volunteers/index.html",{"volunteers":volunteers})

def update_view(request, pk):
    object = get_object_or_404(volunteer_profiles,pk=pk)  # Use the passed pk argument instead of hardcoding it
    if request.method == "POST":
        form = volunteerform(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect(reverse("volunteers:index"))
    else:
        form = volunteerform(instance=object)
    return render(request,"volunteers/update.html", {"form": form, "object": object})