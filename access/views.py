from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Users, Questions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsersSerializer, QuestionsSerializer, LoginSerializers

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            user_instance = serializer.validated_data['user_instance']
            
            # Crear el token JWT para el usuario autenticado
            refresh = RefreshToken.for_user(user_instance)
            access_token = str(refresh.access_token)

            return Response({
                'refresh': str(refresh),
                'access': access_token
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
