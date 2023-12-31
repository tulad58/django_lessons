from rest_framework.routers import DefaultRouter
from django.urls import path
from logistic.views import ProductViewSet, StockViewSet, sample_view

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path('test/', sample_view),
]

urlpatterns += router.urls
