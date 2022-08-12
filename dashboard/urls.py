from django.urls import path
from .import views
urlpatterns = [
    path('dashboard', views.dashboard,name="dashboard-template"),
    path('logout', views.logout_,name="logout"),
]
