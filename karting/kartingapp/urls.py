from django.urls import include, path
from kartingapp import views, forms


urlpatterns=[
    path('home', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.form_name_view, name='contact'),
    path('result', views.result, name='result'),
]