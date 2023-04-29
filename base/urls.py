from django.urls import  path
from . import  views
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('login/', views.login_view, name='login'),
    path('home/',views.home,name= "home"),
    path('register/',views.register,name="register"),
    path('form_submit/', views.form_submit, name='form_submit'),
    path('ml_model/',views.mlmodel,name="ml_model"),
    path('upload/', views.upload_files, name='upload_files'),

]