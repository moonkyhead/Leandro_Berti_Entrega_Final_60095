from django.urls import path
from final import views

urlpatterns = [
    path('sesion/', views.sesion, name='sesion'),
    path('registro/', views.registro, name='registro'),
]
