from django.urls import path
from .import views
urlpatterns = [
    path('fundlist/', views.fundList, name='fundlist'),

]