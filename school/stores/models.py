from django.db import models
from django.contrib.auth.models import User,Group
from common.models import BaseModel
from django.core.validators import RegexValidator
from django.utils import timezone

class UserProfile(BaseModel):
	user = models.ForeignKey(User)
	address = models.CharField(max_length = 50,null=True,blank=True)
	mobile = RegexValidator(regex=r'\d{10}', message="Phone number must be entered in the format: '9999889999'.")
	phone = models.CharField(blank=True, null=True, max_length=15)

	def __str__(self):
		return "Username - %s Profile - %s"%(self.user.username,self.user.get_full_name())

