from django.shortcuts import  render, redirect
from .forms import RegisterForm
# from django.contrib.auth import login

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			# login(request, user)
	form = RegisterForm()
	return render (request,"signup.html",{"form":form})