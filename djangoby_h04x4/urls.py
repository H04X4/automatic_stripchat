from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run-main/', views.run_main, name='run_main'),

]
