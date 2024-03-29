from rest_framework.authtoken.models import Token
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.views import Response,status
from django.contrib.auth import authenticate
from .mixins import SerializerByMethodMixin

from users.serializers import UserSerializer, LoginSerializer,UserAdminSerializer, ListUserSerializer, SpecificUserSerializer
from users.models import User
from . import permissions
from rest_framework.authentication import TokenAuthentication


class UserAdminView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer

class UserView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_map = {
        'GET': ListUserSerializer,
        'POST': UserSerializer    
    }

    

class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_instance = authenticate(
            email = serializer.validated_data["email"],
            password = serializer.validated_data["password"],
        )

        if user_instance:
            token, _ = Token.objects.get_or_create(user=user_instance)
            return Response({"token": token.key})

        return Response(
            {"detail": "Invalid email or password"}, status.HTTP_401_UNAUTHORIZED 
        )


class UserDetailView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwner]

    queryset = User.objects.all()
    serializer_map = {
        'GET': SpecificUserSerializer,
        'PATCH': UserSerializer,
        'DELETE': UserSerializer
    }
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance,"is_active",False)
        instance.save()
        serializer = UserSerializer(instance,{"is_active":False},partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
