from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('profile-feed', views.UserProfileFeedViewSet) # Don't need to put base_name if quertset is provided
#base_name is needed when we need to retrieve the URL by using the URL retrieving function provided by Django
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
