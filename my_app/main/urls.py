from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import BooksViewSet, JournalsViewSet

urlpatterns = [
    path('auth/login/', obtain_jwt_token),
    path('books/', BooksViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:pk>', BooksViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('journals/', JournalsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('journals/<int:pk>', JournalsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
