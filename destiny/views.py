from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from destiny.models import Item, List

# Create your views here.
def home_page(request):
	return render(request, 'home.html')

def view_squad(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items':items})

def new_squad(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/squads/the-only-squad-in-the-world/')