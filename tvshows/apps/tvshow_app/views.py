from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import TV_shows


def index(request):
    context = {
        "all_shows": TV_shows.objects.all()
    }
    return render(request, 'tvshow_app/index.html', context)


def new_show_form(request):
    return render(request, 'tvshow_app/new_show.html')


def add_new_show(request):
    errors = TV_shows.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/new_show_form")
    else:
        new_show = TV_shows.objects.create(title=request.POST['title'],
                                        network=request.POST['network'],
                                        description=request.POST['description'],
                                        release_date=request.POST['release_date'])
        return redirect("/", messages)


def display_show_info(request, show_id):
    context = {
        "show_info": TV_shows.objects.get(id=show_id)
    }
    return render(request, 'tvshow_app/show_info.html', context)


def edit_show_form(request, show_id):
    context = {
        "show_info": TV_shows.objects.get(id=show_id)
    }
    return render(request, 'tvshow_app/edit_show.html', context)

def edit_show(request, show_id):
    errors = TV_shows.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/{show_id}/edit")
    else:
        edit_show = TV_shows.objects.get(id = show_id)
        edit_show.title = request.POST['title']
        edit_show.network = request.POST['network']
        edit_show.description = request.POST['description']
        edit_show.release_date = request.POST['release_date']
        edit_show.save()
    return redirect(f'/{show_id}')

def delete_warning(request, show_id):
    context = {
        "show_info": TV_shows.objects.get(id=show_id)
    }
    return render(request, 'tvshow_app/warning.html', context)

def delete_show(request, show_id):
    delete_this = TV_shows.objects.get(id = show_id)
    delete_this.delete()
    return redirect("/")
    