from django.db import models

# Create your models here.
from django.utils import timezone

# Create your models here.
class faq(models.Model):
	question=models.CharField(max_length=600)
	answer=models.TextField()

	def __str__(self):
		return self.question
class how_the_ai_system_works(models.Model):
	title=models.CharField(max_length=600)
	explanation=models.TextField()

	def __str__(self):
		return self.title

class testimonial(models.Model):
	fullname=models.CharField(max_length=200)
	country=models.CharField(max_length=200)
	role=models.CharField(max_length=200)
	testimony=models.TextField()
	date=models.DateField(default=timezone.now)

	def __str__(self):
		return self.fullname + " " + self.role