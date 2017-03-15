from django.forms import ModelForm
from homepage.models import timemodel
from django import forms

# class addform(ModelForm):
# 	class Meta:
# 		model = timemodel
# 		fields = [user_name, password, time_submitted]
# 		widgets = {'time submitted' : forms.hiddeninput()}


class startform(forms.Form):
	first_entry = forms.CharField(label = 'first entry', max_length=100)
	second_entry = forms.CharField(label = 'second entry', max_length=100)








