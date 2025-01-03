from django.urls import path
from portfolio_app import views

urlpatterns = [
    path('', views.index, name='index'),  # Home/index route
    path('contact/', views.index, name='contact'),  # Contact route
    path('view-messages/', views.view_messages, name='view_messages'),
]
