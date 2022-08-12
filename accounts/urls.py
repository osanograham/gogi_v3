from django.urls import path, include
from .import views
urlpatterns = [
	path('add/client/account',views.add_account,name="add-client-account"),
	path('account/history',views.account_history,name="account-history"),
	path('account/delet',views.delete_account,name="delete-account"),
	path('test',views.test,name="test"),
	path('my/trading/accounts',views.my_trading_accounts,name="my-trading-accounts"),
	path('<int:num>',views.account_details,name="trading-accounts-details"),
	path('change/status/<int:num>',views.status_Set,name="status_Set"),
	path('testing_logged_user',views.logged_user,name="logged_user"),

 
]
