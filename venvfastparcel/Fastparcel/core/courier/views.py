from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    return render(request,'home.html')

#please add comments to the all function because this is a complex app