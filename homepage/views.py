from django.shortcuts import render
from django.http import HttpResponse
from .forms import  startform
from homepage.models import timemodel
from django.shortcuts import render
import datetime
from django.contrib.auth.views import login 



def index(request):
	if request.method == "GET":
		return render(request, 'homepage/home.html', {'form': 'startform'},)

		# form = startform(request.POST)
		# username = form.cleaned_data.get('first_entry')
		# pw = form.cleaned_data.get('second_entry')
		# x = timemodel.objects.filter(first_name=username)
		# x = x[(len(x)-1)]
		# if x.time_submitted
		# now = datetime.datetime.now()



