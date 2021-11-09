from django import forms
from .models import Recipe, Nutri_content, Recipe_prep_details

class Form1(forms.ModelForm):
	class Meta:
		model = Recipe
		fields = ['Recipe_name', 'Recipe_category', 'Recipe_type']

class Form2(forms.ModelForm):
	class Meta:
		model = Recipe_prep_details
		fields = ['preparation_time', 'num_of_servings', 'ingredients', 'instructions']

class Form3(forms.ModelForm):
	class Meta:
		model = Nutri_content
		fields = ['calories_per_serving', 'carbs', 'proteins', 'saturated_fats', 'trans_fats', 'cholestrol']