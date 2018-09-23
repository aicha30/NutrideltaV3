import datetime

from django.db import models
from django.utils import timezone
import datetime

class aliment(models.Model):
	aliment_name = models.CharField(max_length=200,)
	frequency = models.CharField(max_length=200,default='')


