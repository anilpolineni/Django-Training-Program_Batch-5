from django.db import models

from django.contrib.auth.models import User

from PIL import Image

# Create your models here.


class Profile(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="pics/")
	dob=models.DateField(null=True)
	mobileno=models.CharField(max_length=10)