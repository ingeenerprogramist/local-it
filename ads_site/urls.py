from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # главная страница
    path('about/', views.about, name='about'), # страница о нас
    path('', include('ads_sit.urls')),
]

