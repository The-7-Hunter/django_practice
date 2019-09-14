from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("this is list of all bolgs")

def new(request):
    return HttpResponse("this is where we will add new something!")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"this is the blog number { number }, isn't it ?")

def edit(request, number):
    return HttpResponse(f"this is when you want to edit number { number }")

def destroy(request, number):
    return HttpResponse(f"this is when you want to delete number { number }, are you sure!")