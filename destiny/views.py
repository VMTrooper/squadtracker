from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
	# response = HttpResponse("<html><title>Destiny SquadTracker</title></html>")
	return render(request,'home.html')