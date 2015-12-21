from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(self):
	response = HttpResponse("<html><title>Destiny SquadTracker</title></html>")
	return response