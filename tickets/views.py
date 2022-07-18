from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from tickets.models import Ticket
from rest_framework.views import Response,status
from tickets.serializers import TicketDetailSerializer, TicketSerializer
from .mixins import SerializerByMethodMixin

class TicketView(SerializerByMethodMixin,generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Ticket.objects.all()
    serializer_map = {
        "GET": TicketSerializer,
        "POST": TicketDetailSerializer,
    }

    def perform_create(self, serializer):
        return serializer.save(buyer=self.request.user)

class TicketDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Ticket.objects.all()
    serializer_class = TicketDetailSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance,"status_active",False)
        instance.save()
        serializer = TicketSerializer(instance,{"status_active":False},partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)

