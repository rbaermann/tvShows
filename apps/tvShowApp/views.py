from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    return redirect('/shows')

def shows(request):
    context = {}
    context['shows'] = Show.objects.all()
    return render(request, 'tvShowApp/index.html', context)

def new(request):
    return render(request, 'tvShowApp/newShows.html')

def showsAdd(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else: 
        newShow = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            desc = request.POST['desc'],
        )
        newShow.save()
        return redirect(f'/shows/{newShow.id}')

def desc(request, showID):
    context = {}
    context['show'] = Show.objects.get(id=showID)
    return render(request, 'tvShowApp/tvDesc.html', context)

def destroy(request, showID):
    delShow = Show.objects.get(id=showID)
    delShow.delete()
    return redirect('/shows')

def edit(request, showID):
    context = {}
    context['show'] = Show.objects.get(id=showID)
    return render(request, 'tvShowApp/updateShow.html', context)

def editShow(request, showID):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        show = Show.objects.get(id=showID)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
    return redirect(f'/shows/{showID}')
