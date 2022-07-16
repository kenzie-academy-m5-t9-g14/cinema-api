from rest_framework.authtoken.models import Token
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status

from django.contrib.auth import authenticate

from users.serializers import UserSerializer, LoginSerializer
from users.models import User
from . import permissions
from rest_framework.authentication import TokenAuthentication


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
