from django.urls import path, include
from .import views
urlpatterns = [
    path('performance',views.individual_performance,name="account-performance"),
    path('history',views.account_history_,name="account-history"),
]
