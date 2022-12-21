from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('momo/', views.momo, name='momo_page'),
    path('sms/', views.sms, name='sms_page'),


    path('callback', views.callback, name='callback_url'),
    path('cancel', views.cancel, name='cancel_url'),
    path('return', views.returns, name='return_url')
    
]
