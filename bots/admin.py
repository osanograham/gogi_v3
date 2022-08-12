from django.contrib import admin
from .models import gold_bot,indices_bot,fx_bot,crypto_bot
# Register your models here.

#class go_botsAdmin(Admin.ModelAdmin):

admin.site.register(crypto_bot)

class gold_bot_admin(admin.ModelAdmin):
	list_display=("name","level_of_risk","company","server","login")
	list_filter = ('name', 'level_of_risk')
admin.site.register(gold_bot, gold_bot_admin)

class indices_bot_admin(admin.ModelAdmin):
	list_display=("name","level_of_risk","company","server","login")
	list_filter = ('name', 'level_of_risk')
admin.site.register(indices_bot, indices_bot_admin)

class fx_bot_bot_admin(admin.ModelAdmin):
	list_display=("name","level_of_risk","company","server","login")
	list_filter = ('name', 'level_of_risk')
admin.site.register(fx_bot, fx_bot_bot_admin)