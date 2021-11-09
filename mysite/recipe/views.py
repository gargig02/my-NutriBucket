from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipe.models import Recipe, Recipe_prep_details, Nutri_content
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Form1, Form2, Form3
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
	var = {
	'Recipe': Recipe.objects.all(),
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
	'title': cat_name,
	'cat_name': cat_name
	}
	return render(request, 'recipe/category.html', var)

#class RecipeDetailView(DetailedView):
#	model = Recipe

@login_required
def RecipeCreateView(request):
	if request.method == 'POST':
		form1 = Form1(request.POST)
		form1.instance.user = request.user
		form2 = Form2(request.POST)
		form2.instance.Recipe = form1.instance
		form3 = Form3(request.POST)
		form3.instance.Recipe = form1.instance
		if form1.is_valid() and form2.is_valid() and form3.is_valid():
			form1.save()
			form2.save()
			form3.save()
			name = form1.cleaned_data.get('Recipe_name')
			messages.success(request, f'Your recipe {name} has been uploaded')
			return redirect('recipe-home')

	else:
		form1 = Form1()
		form2 = Form2()
		form3 = Form3()

	var = {'form1': form1, 'form2':form2, 'form3': form3}

	return render(request, 'recipe/recipe_form.html', var)

