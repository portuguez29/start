from django.urls import path
from . import views
urlpatterns = [
 path('', views.index),
 path('admin/<path>', views.index),
]