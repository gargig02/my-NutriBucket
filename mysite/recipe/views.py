from django.shortcuts import render
from django.http import HttpResponse
from recipe.models import Recipe, Recipe_prep_details

# Create your views here.
def home(request):
	var = {
	'Recipe': Recipe.objects.all(),
	'Recipe_prep_details': Recipe_prep_details.objects.all(),
	'title': 'Home'
	}
	return render(request,'recipe/home.html', var)

def contact(request):
	return render(request,'recipe/contact.html', {'title' : 'Contact'})

def about(request):
	return render(request,'recipe/about.html', {'title' : 'About'})

def category(request, cat_name):
	var = {
	'Recipe': Recipe.objects.all(),
	'Recipe_prep_details': Recipe_prep_details.objects.all(),
	'title': cat_name,
	'cat_name': cat_name
	}
	return render(request, 'recipe/category.html', var)
