from django.db import models

# Create your models here.
class Thanks(models.Model):
	thanks_id = models.BigAutoField(primary_key=True,unique=True)
	thanks_title = models.CharField(max_length=100, blank=False, null=False)
	thanks_date = models.DateTimeField(null=False)
	thanks_description = models.CharField(max_length=1000,null=False)
	givethanks_count = models.IntegerField(null=False)
