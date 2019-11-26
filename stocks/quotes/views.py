from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
#Type in public key
public_key = 
# Create your views here.
def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token="+public_key)

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api':api})
	else:
		return render(request, 'home.html', {'ticker':"Enter a ticker symbol above..."})

	#pk_78e5c006aeef4f3ea34f21ae5ae4ce67
	

def about(request):
	return render(request, 'about.html', {})




def add_stock(request):

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added"))
			return redirect('add_stock')
	else:		
		ticker = Stock.objects.all()
		return render(request, 'add_stock.html', {'ticker':ticker})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted!"))
	return redirect(add_stock)
