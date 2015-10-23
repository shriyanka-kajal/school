from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BaseModel(models.Model):
	creator = models.ForeignKey(User,related_name = "Created_By_User")
	#created_date = models.DateTimeField(auto_now_add=True,auto_now=False, default=timezone.now)
	#modified_date = models.DateTimeField(auto_now=True,auto_now_add=False, default=timezone.now)
	#editor = models.ForeignKey(User, null=True, blank=True, related_name='%(app_label)s_%(class)s_last_modified')

	def __str__(self):
		return self.creator.get_full_name()

	class Meta:
		abstract = True

