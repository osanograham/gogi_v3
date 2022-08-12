from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomerUserAdmin(UserAdmin):
	model=CustomUser
	add_form=CustomUserCreationForm

	fieldsets=(
			*UserAdmin.fieldsets,
			[

				'User role',
				{

					'fields':(
					'phone_number',
					'country',
					'about'
					)
				}
			]

		)
admin.site.register(CustomUser,CustomerUserAdmin)