from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
	return render(request, 'usuarios/index-login.html')

def loginView(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active==1:
			login(request, user)
			if user.is_superuser==1:
				return redirect('../admin/')
		else:
			return render(request, 'usuarios/error.html')
	return render(request,'usuarios/errorusuario.html')

def logoutView(request):
	logout(request)
	return redirect('/')