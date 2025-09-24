from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Signup API
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    name = request.data.get("name")
    password = request.data.get("password")

    if not name or not password:
        return Response({"error": "Name and password required"}, status=HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=name).exists():
        return Response({"error": "User already exists"}, status=HTTP_400_BAD_REQUEST)

    User.objects.create_user(username=name, password=password)
    return Response({"message": "Account created successfully"}, status=HTTP_200_OK)


# Login API
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    name = request.data.get("name")
    password = request.data.get("password")

    user = authenticate(username=name, password=password)
    if user is None:
        return Response({"error": "Invalid credentials"}, status=HTTP_401_UNAUTHORIZED)

    # Create or get token
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        "name": user.username,
        "token": token.key
    }, status=HTTP_200_OK)
