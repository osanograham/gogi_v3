from django.urls import path
from .import views
urlpatterns = [
    path('go/indices/bots',views.bots_list,name='indices_bots'),
    path('go/forex/bots',views.go_forex_bots,name='go_forex_bots'),
    path('go/gold/bots',views.gold_bots,name='gold_bots'),
    path('go/crypto/bots',views.crypto_bots,name='crypto_bots'),
    #urls,
    path('go/indices/<int:master>/<int:slave>/',views.add_account,name='adding-accounts'),
    path('go/crypto/<int:master>/<int:slave>/',views.add_account_to_crypto,name='adding-accounts'),
    path('go/gold/<int:master>/<int:slave>/',views.add_account_to_gold,name='adding-accounts'),
    path('go/forex/<int:master>/<int:slave>/',views.add_account_to_forex,name='adding-accounts'),

]
