from django.urls import path
from . import views

app_name = 'analysis_app'
urlpatterns = [
    path('', views.temp_list, name='temp_list'),
    path('a/<int:pk>/', views.temp_detail, name='temp_detail'),
    path('a/new/',views.temp_new,name='temp_new'),
    path('a/<int:pk>/edit/', views.temp_edit, name='temp_edit'),
    path('analysis', views.analysis_screen, name='analysis_screen'),
    path('analysis/plot', views.img_plot, name="img_plot"),
]
