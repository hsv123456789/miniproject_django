from django.urls import  path
from . import  views
urlpatterns = [
    path('',views.login,name="login"),
    path('home/',views.home,name= "home"),
    path('register/',views.register,name="register"),
    path('form_submit/', views.form_submit, name='form_submit'),
    path('ml_model/',views.mlmodel,name="ml_model")

]