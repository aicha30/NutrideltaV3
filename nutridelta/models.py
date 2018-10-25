import datetime

from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

class aliment(models.Model):
	aliment_name = models.CharField(max_length=200,)
	frequency = models.CharField(max_length=200,default='')



