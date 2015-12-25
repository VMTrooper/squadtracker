from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from destiny.models import Item, List

# Create your views here.
def home_page(request):
	return render(request, 'home.html')

def view_squad(request, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'list.html', {'squad':list_})

def new_squad(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/squads/%d/' %(list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/squads/%d/' % (list_.id,))