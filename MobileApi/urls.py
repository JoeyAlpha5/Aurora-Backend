from django.urls import path
from .views import getFeed, emptyParams,getLyrics

urlpatterns = [
    path('', emptyParams),
    path('feed', getFeed),
    path('lyrics', getLyrics),
]
