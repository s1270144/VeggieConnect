from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def buyer_home(request):
    return render(request, 'buyer/home.html')
