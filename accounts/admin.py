from django.contrib import admin
from .models import add_client_trading_account
from django.contrib import messages
from django.utils.translation import ngettext
# Register your models here.
#admin.site.register(add_client_trading_account)

@admin.action(description='Activate')
def make_active(modeladmin, request, queryset):
	queryset.update(status='Active')
@admin.action(description='Deactivate')
def make_deactivate(modeladmin, request, queryset):
	queryset.update(status='Deactivate')

class add_account_admin(admin.ModelAdmin):
	
	list_display=("status","account_name","choose_platform","account_number","account_password","account_server_name")
	list_filter = ("status", "choose_platform")
	actions = [make_active,make_deactivate]

admin.site.register(add_client_trading_account, add_account_admin)