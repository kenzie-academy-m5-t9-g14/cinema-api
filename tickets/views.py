from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from movie_sessions.models import MovieSession

from tickets.models import Ticket
from rest_framework.views import Response,status
from tickets.serializers import TicketDetailSerializer, TicketSerializer


class TicketListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Ticket.objects.all()

    serializer_class = TicketDetailSerializer


    def perform_create(self, serializer):
        movie_session = get_object_or_404(MovieSession ,pk = self.kwargs.get("movie_session_id"))
        return serializer.save(buyer=self.request.user,movie_session=movie_session)



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

