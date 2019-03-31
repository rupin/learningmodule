from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

#this model saves the modules currently being offered	
class Module(models.Model):
	module_id = models.BigAutoField(primary_key=True)
	module_name = models.CharField(max_length=50)
	module_category = models.CharField(max_length=50)
	module_grade= models.CharField(max_length=100)
	

#this model saves the relationship between which module has been offered by which user. It will also have schedule information associated with it.
class Schedule(models.Model):
	schedule_id=models.BigAutoField(primary_key=True)
	fk_module_id=models.ForeignKey(Module, on_delete=models.CASCADE)
	fk_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

#this model saves the relationship between which module has been taken by which user, and which schedule it was done on.
class Milestone(models.Model):	
	milestone_id=models.BigAutoField(primary_key=True)
	fk_schedule_id=models.ForeignKey(Schedule, on_delete=models.CASCADE)
	fk_module_id=models.ForeignKey(Module, on_delete=models.CASCADE)
	fk_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)