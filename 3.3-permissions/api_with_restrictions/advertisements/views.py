from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer
from advertisements.permissions import IsOwnerReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerReadOnly, IsAuthenticated]
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['creator', 'id', 'status', 'created_at',]


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerReadOnly(), IsAuthenticated()]
        return []

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        creator = self.request.query_params.get("creator", None)

        if creator is not None:
            print(creator)
            queryset = queryset.filter(creator__id=creator)

        return queryset
