from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
#base_name is needed when we need to retrieve the URL by using the URL retrieving function provided by Django
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
