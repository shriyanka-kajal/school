from django.db import models
from django.contrib.auth.models import User,Group
from common.models import BaseModel,TaggedItem,RangeField
from django.core.validators import RegexValidator
from django.utils import timezone
import os
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from colorful.fields import RGBColorField

class Pincode(models.Model):
	pass

class Address(models.Model):
	add1 = models.CharField(max_length = 50)
	add2 = models.CharField(max_length = 50, null = True, blank = True)
	mobile = RegexValidator(regex=r'\d{10}$', message="Phone number must be 10 digits entered without +91")
	city = models.CharField(max_length=50, blank=False)
	state = models.CharField(max_length=40, blank=False)
	country = models.CharField(max_length=45, blank=False, default='India')
	pincode = models.ForeignKey(Pincode,blank=False,null=False)    

	def __str__(self):
		return "address1 = %s , city = %s , state = %s , pincode = %s, country = %s"%(self.add1,self.city,self.state,self.pincode,self.country)

	class Meta:
		pass

class UserProfile(BaseModel):
	user = models.ForeignKey(User)
	address = models.CharField(max_length = 50, null=True,blank=True)
	address_fk = models.ForeignKey(Address,max_length = 50,null=True,blank=True)
	mobile = RegexValidator(regex=r'\d[0-9]{10}$', message="Phone number must be 10 digits entered without +91")
	phone = models.CharField(blank=True, null=True, max_length=15)
	ip = models.CharField(blank=True, null=True, max_length=50, default="") #store real ip from  requests meta field
	country = models.CharField(blank=True, null=True, max_length=50, default="India")
	subscribed = models.BooleanField(default=True)

	def unsubscribe_link(self):
		'''create a hashed unsubscribed link for the newsletter and use url to join with it and pass it to users'''

		link = str(self.user.email)+str(self.user.id)
		return urlsafe_base64_encode(link)
	
	def _get_username_profile(self):
		return "Username - %s , Profile - %s"%(self.user.username,self.user.get_full_name())

	full_name = property(_get_username_profile)
	link = property(unsubscribe_link)

	def __str__(self):
		return self.full_name

	class Meta:
		ordering = ['user']

class Product(models.Model):
	pass

class Enquiry(models.Model):
	pass

class Feedback(models.Model):
	pass

class CartList(BaseModel):
	user = models.ForeignKey(User)
	product = models.ForeignKey(Product)

	class Meta:
		unique_together = ('user', 'product',)

class Images(BaseModel):
	pass

class Category(BaseModel):
	pass

class Size(models.Model):
	pass

class Color(models.Model):
	color = models.CharField(max_length=20)
	colorcode = RGBColorField(default='#FFFFFF')

class Ratings(TaggedItem):
	rating = RangeField(min_value=1, max_value=5)

	def __str__(self):
		return '%d - %s - %s' % (self.rating, self.user, self.content_object, )

class Reviews(TaggedItem):
	review = models.CharField(max_length=100)

	def __str__(self):
		return '%d - %s - %s' % (self.review, self.user, self.content_object, )