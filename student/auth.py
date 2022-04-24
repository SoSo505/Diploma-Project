from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User


from .models import Student
from .serializers import UserProfileSerializerSignUp, UserSerializer


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response('Successfully deleted')


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.data['username'],
            email=serializer.data['email'],
            password=serializer.data['password']
        )
        studentserializer = UserProfileSerializerSignUp(data=request.data)
        if studentserializer.is_valid():
            userProfile = Student.objects.create_user_profile(user=user,
                                                                  phone_number=studentserializer.data['phone_number'],
                                                                    university=studentserializer.data['university'],
                                                                    )
            return Response(userProfile, status=status.HTTP_200_OK)
    return Response(serializer.errors)
