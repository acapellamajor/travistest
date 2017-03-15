from __future__ import unicode_literals
from datetime import datetime 
from django.db import models

class timemodel (models.Model):
	user_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	time_submitted=models.DateTimeField(auto_now = True, blank = True)
