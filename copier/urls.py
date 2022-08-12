from django.urls import path
from .import views
urlpatterns = [
    path('base/copier',views.base_copier,name="base-copier")
]
