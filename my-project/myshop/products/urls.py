from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('products',views.index),
    path('products/<product>',views.product),
    path('signup',views.signup,name="signup"),
]