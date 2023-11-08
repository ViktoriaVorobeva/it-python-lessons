from django.urls import path
from . import views

urlpatterns = [
    path('', views.temperature_chart, name='temperature_chart')
    # path('chart/', views.chart_view, name='chart-view'),
]