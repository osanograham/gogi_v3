from django import forms 
from .models import add_client_trading_account

class add_client_account_form(forms.ModelForm):
	class Meta:
		model=add_client_trading_account
		fields=('account_name','choose_platform','account_number','account_password', 'broker_name','account_server_name',)
