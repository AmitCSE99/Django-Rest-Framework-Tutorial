from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        user = User.objects.get(id=serializer.data.get('id'))
        refresh = RefreshToken.for_user(user)
        return Response({'data': serializer.data, 'refresh': str(refresh), 'access': str(refresh.access_token)})


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        refresh = RefreshToken.for_user(user)
        serializer = UserSerializer(user)
        return Response({'data': serializer.data, 'refresh': str(refresh), 'access': str(refresh.access_token)})


class ResetAll(APIView):
    def post(self, request):
        User.objects.delete()
        return Response({
            'message': "Deleted"
        })


class GetUsersList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
