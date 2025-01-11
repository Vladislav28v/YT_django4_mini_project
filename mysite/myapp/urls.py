from django.urls import path
from myapp import views

#Обозначили простаранство имен
app_name ="myapp"

urlpatterns = [
    path('', views.index),
    path('<int:id>/', views.indexItem, name='detail'),


]
