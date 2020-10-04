from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
        serializer_class = serializers.HelloSerializer #Define a form
        def post(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                name = serializer.validated_data.get('name')
                message = f'Hello {name}'
                return Response({'message': message})
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

        def get(self, request, format=None):
            an_apiview = [
                'Uses API View',
                'The List of the Functions'
            ]
            return Response({'message': ' Hello', 'an_apiview': an_apiview});

        def put(self, request, pk=None):
            return Response({'message': 'PUT'})

        def patch(self, request, pk=None):
            return Response({'message': 'PATCH'})

        def delete(self, request, pk=None):
            return Response({'message': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provies more functionality with less code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            message = f'Hello {first_name} {last_name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})
