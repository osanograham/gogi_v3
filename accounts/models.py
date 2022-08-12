from django.db import models
from users.models import CustomUser



class add_client_trading_account(models.Model):
	account_name=models.CharField('Account_Name',max_length=50,blank=True)
	PLATFORM = [("MT4","MT4"),("MT5","MT5")]
	choose_platform = models.CharField('Platform',max_length=50,choices=PLATFORM,default="MT4")
	account_number=models.CharField('Account_Number',max_length=300,blank=False, unique=True)
	account_password=models.CharField('Password',max_length=300,blank=False)
	broker_name=models.CharField('Broker Name',max_length=100,blank=False, default="")
	account_server_name=models.CharField('Account Server Name',max_length=100,blank=False)
	date_added=models.DateTimeField("Date Added",auto_now_add=True)
	choices=[("Deactivate","Deactivate"),("Active","Active")]
	status=models.CharField("Status",max_length=120,choices=choices,default="Deactivate")
	created_by=models.EmailField("Owner",max_length=156,default="email@company.com")
	
	def __str__(self):
		return self.account_name