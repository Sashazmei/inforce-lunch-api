from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        restaurant = self.get_object()
        if restaurant.owner != self.request.user:
            raise PermissionDenied("You can edit only your own restaurants.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You can delete only your own restaurants.")
        instance.delete()
