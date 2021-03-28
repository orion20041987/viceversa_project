from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def tryit(request):
	return render(request, 'tryit.html')
