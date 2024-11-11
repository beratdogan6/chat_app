from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .serializers import RegistrationSerializer, UserSerializer


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        self.__change_status(user)
        serialize_user = UserSerializer(user, many=False)
        return Response({
            'token': token.key,
            'user': serialize_user.data,
        })

    def __change_status(self, user: User):
        profile = user.profile
        profile.online = True
        profile.save()


class RegisterView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        super(RegisterView, self).post(request, *args, **kwargs)
        return Response({'message': 'Registration success, now you can login'})


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        profile = request.user.profile
        profile.online = False
        profile.save()
        return Response({'message': 'logout'})
