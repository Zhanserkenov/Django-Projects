from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Главная страница
    path("add-food/", views.add_food, name="add-food"),
    path("update-goals/", views.update_goals, name="update-goals"),
    path("chart-data/", views.chart_data, name="chart-data"),
]