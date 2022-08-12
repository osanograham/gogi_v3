from django.urls import path, include
from . import views
urlpatterns = [
    path('result',views.result,name="result"),
    path('go/gold/results/<int:indices_nu>/',views.results_specific,name="results_specific"),

    path('result/<int:indices_nu>/',views.results_specific,name="results_specific"),
    path('go/indices/results/<int:indices_nu>/',views.results_specific,name="results_specific"),
    path('go/forex/results/<int:indices_nu>/',views.results_specific,name="results_specific"),
    
    path('go/crypto/results/<int:indices_nu>/',views.results_specific,name="results_specific"),

]
