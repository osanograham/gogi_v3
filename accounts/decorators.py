from .models import add_client_trading_account

def main(request):
	user=request.user
	print(user.email)
	entry=[]
	accounts=add_client_trading_account.objects.all()
	print(accounts)


