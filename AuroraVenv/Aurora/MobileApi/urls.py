from django.urls import path
from .views import getFeed, emptyParams

urlpatterns = [
    path('', emptyParams),
    path('feed', getFeed),
]
