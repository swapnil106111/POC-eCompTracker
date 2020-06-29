from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate

from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields=['email','first_name','username']


class UserView(viewsets.ModelViewSet):

    @api_view(['POST'])
    @permission_classes([AllowAny])
    @csrf_exempt
    def signup(request):

        username = request.data.get('username')
        name = request.data.get('name')
        email = request.data.get('email')
        if not username:
            return Response({'detail': 'please provide username'}, status=400)
        # if not email:
        #     return Response({'detail': 'please provide email'}, status=400)
        if not name:
            return Response({'detail': 'please provide name'}, status=400)
        password = request.data.get('password')
        if not password:
            return Response({'detail': 'please provide password'}, status=400)
        else:
            print(username, password)

            user = User.objects.filter(username=username).first()
            user_group = Group.objects.get(name='todo_view')
            if not user:
                user = User.objects.create_user(username=username, password=password, first_name=name)
                if email:
                    user.email = email
                #user.save()
                #user_group = Group.objects.get(name='todo_view')
                user_group.user_set.add(user)
            token = Token.objects.filter(user=user).first()
            if not token:
                Token.objects.get_or_create(user=user)
                token = Token.objects.filter(user=user).first()
            print(token)
            print(user_group)
            serializer = UserSerializer(user)
            response_data = serializer.data
            response_data['token'] = token.key
            response_data['user_group']= user_group.name

            login(request, user)
            return Response(response_data)


    @api_view(['POST'])
    @permission_classes([AllowAny])
    @csrf_exempt
    def loginwithpassword(request):

        username = request.data.get('username')
        if not username:
            return Response({'detail': 'please provide email'}, status=400)
        password = request.data.get('password')
        if not password:
            return Response({'detail': 'please provide password'}, status=400)
        else:
            print(username, password)
            user = User.objects.filter(username=username, is_active=True).first()
            print(user)
            if not user or not user.password:
                return Response({'detail': 'Unauthorised'}, status=401)
            u1 = authenticate(username= username,password =password)
            if u1:
                print(u1)
                login(request, user)

                token = Token.objects.filter(user=user).first()

                if not token:
                    Token.objects.get_or_create(user=user)
                    token = Token.objects.filter(user=user).first()
                print(token)
                return Response({'user_id': user.id, 'auth_token':token.key})
            return Response('invalid credentials')
