from django.urls import path
from . import views
from .views import home,carDetail

urlpatterns = [
    path('',views.home.as_view(),name="home"),
    path('Detail/<int:pk>',views.carDetail.as_view(),name="detail"),
    path('register/',views.register,name="register")
]
