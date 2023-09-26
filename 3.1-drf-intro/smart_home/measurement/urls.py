from django.urls import path
from .views import SensorView, CreateSesnorView, UpdateSensorView, CreateMeasurementsView, MeasurementsView,\
    SensorViewID

urlpatterns = [
    path('sensor/', SensorView.as_view()),
    path('create/', CreateSesnorView.as_view()),
    path('update/<pk>/', UpdateSensorView.as_view()),
    path('measurements/', CreateMeasurementsView.as_view()),
    path('measurements_all/', MeasurementsView.as_view()),
    path('measurements/<pk>/', SensorViewID.as_view()),
]
