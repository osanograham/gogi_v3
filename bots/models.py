from django.db import models

# Create your models here.
class indices_bot(models.Model):
	name=models.CharField("Bot Name ",max_length=120, blank=False)
	capital_required=models.FloatField("Capital Field",blank=False,default=0.00)
	pricing=models.FloatField("pricingpricing",blank=False, default=0.00)
	choices=[
		("Super High Risk","Super High Risk"),
		("Very Risk","Very Risk"),
		("High Risk","High Risk"),
		("High","High"),
		("Moderate Risk","Moderate Risk"),
		("Low Risk","Low Risk"),
		]
	instrument=[
		("US30, NAS100","US30, NAS100"),
		("US30, NAS100, SPX500","US30, NAS100, SPX500"),
		]
	level_of_risk=models.CharField("Risk Level",choices=choices,blank=False,max_length=150,)
	instruments=models.CharField("Instruments",choices=instrument,blank=False,max_length=150,)
	
	company=models.CharField("Broker Company",max_length=150,blank=False)
	server=models.CharField("Server Name",max_length=150,blank=False)
	login=models.IntegerField("Account Number",blank=False)
	master_password=models.CharField("Master Password",max_length=200,blank=False)
	investor_password=models.CharField("Investor Password",max_length=200,blank=False)
	PLATFORM = [("MT4","MT4"),("MT5","MT5")]
	choose_platform = models.CharField('Platform',max_length=50,choices=PLATFORM,default="MT4")
	paid_subscribers=models.TextField("Paid Subscribers",max_length=10000,default="", blank=True)
	non_paid_subscribers=models.TextField("Non-Paid Subscribers",max_length=10000,default="",blank=True)

	def __str__(self):
		return self.name
class fx_bot(models.Model):
	name=models.CharField("Bot Name ",max_length=120, blank=False)
	capital_required=models.FloatField("Capital Field",blank=False,default=0.00)
	pricing=models.FloatField("pricingpricing",blank=False, default=0.00)
	choices=[
		("Super High Risk","Super High Risk"),
		("Very Risk","Very Risk"),
		("High Risk","High Risk"),
		("High","High"),
		("Moderate Risk","Moderate Risk"),
		("Low Risk","Low Risk"),
		]
	level_of_risk=models.CharField("Risk Level",choices=choices,blank=False,max_length=150,)
	instruments=models.CharField("Instruments",default="",blank=False,max_length=150,)
	company=models.CharField("Broker Company",max_length=150,blank=False)
	server=models.CharField("Server Name",max_length=150,blank=False)
	login=models.IntegerField("Account Number",blank=False)
	master_password=models.CharField("Master Password",max_length=200,blank=False)
	investor_password=models.CharField("Investor Password",max_length=200,blank=False)
	PLATFORM = [("MT4","MT4"),("MT5","MT5")]
	choose_platform = models.CharField('Platform',max_length=50,choices=PLATFORM,default="MT4")
	paid_subscribers=models.TextField("Paid Subscribers",max_length=10000,default="", blank=True)
	non_paid_subscribers=models.TextField("Non-Paid Subscribers",max_length=10000,default="",blank=True)

	def __str__(self):
		return self.name

class gold_bot(models.Model):
	name=models.CharField("Bot Name ",max_length=120, blank=False)
	capital_required=models.FloatField("Capital Field",blank=False,default=0.00)
	pricing=models.FloatField("pricingpricing",blank=False, default=0.00)
	choices=[
		("Super High Risk","Super High Risk"),
		("Very Risk","Very Risk"),
		("High Risk","High Risk"),
		("High","High"),
		("Moderate Risk","Moderate Risk"),
		("Low Risk","Low Risk"),
		]
	level_of_risk=models.CharField("Risk Level",choices=choices,blank=False,max_length=150,)
	instruments=models.CharField("Instruments",default="",blank=False,max_length=150,)
	company=models.CharField("Broker Company",max_length=150,blank=False)
	server=models.CharField("Server Name",max_length=150,blank=False)
	login=models.IntegerField("Account Number",blank=False)
	master_password=models.CharField("Master Password",max_length=200,blank=False)
	investor_password=models.CharField("Investor Password",max_length=200,blank=False)
	PLATFORM = [("MT4","MT4"),("MT5","MT5")]
	choose_platform = models.CharField('Platform',max_length=50,choices=PLATFORM,default="MT4")
	paid_subscribers=models.TextField("Paid Subscribers",max_length=10000,default="", blank=True)
	non_paid_subscribers=models.TextField("Non-Paid Subscribers",max_length=10000,default="",blank=True)

	def __str__(self):
		return self.name
class crypto_bot(models.Model):
	name=models.CharField("Bot Name ",max_length=120, blank=False)
	capital_required=models.FloatField("Capital Field",blank=False,default=0.00)
	pricing=models.FloatField("pricingpricing",blank=False, default=0.00)
	choices=[
		("Super High Risk","Super High Risk"),
		("Very Risk","Very Risk"),
		("High Risk","High Risk"),
		("High","High"),
		("Moderate Risk","Moderate Risk"),
		("Low Risk","Low Risk"),
		]
	level_of_risk=models.CharField("Risk Level",choices=choices,blank=False,max_length=150,)	
	instruments=models.CharField("Instruments",default="",blank=False,max_length=150,)
	company=models.CharField("Broker Company",max_length=150,blank=False)
	server=models.CharField("Server Name",max_length=150,blank=False)
	login=models.IntegerField("Account Number",blank=False)
	master_password=models.CharField("Master Password",max_length=200,blank=False)
	investor_password=models.CharField("Investor Password",max_length=200,blank=False)
	PLATFORM = [("MT4","MT4"),("MT5","MT5")]
	choose_platform = models.CharField('Platform',max_length=50,choices=PLATFORM,default="MT4")
	paid_subscribers=models.TextField("Paid Subscribers",max_length=10000,default="", blank=True)
	non_paid_subscribers=models.TextField("Non-Paid Subscribers",max_length=10000,default="",blank=True)

	def __str__(self):
		return self.name