from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.upload_image, name="Image Upload Page"),
    path('process/', include("result.urls"), name='process'),
]
