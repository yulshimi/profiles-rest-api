from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
        def get(self, request, format=None):
            an_apiview = [
                'Uses API View',
                'The List of the Functions'
            ]
            return Response({'message': ' Hello', 'an_apiview': an_apiview});
