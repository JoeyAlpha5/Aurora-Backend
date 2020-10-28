from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from .models import Color

# Create your views here.
def getFeed(request):
    if 'search_term' in request.GET:
        print('there is a search term')
    else:
        print('there is no search term')
    feed_count = int(request.GET['feed_count'])
    latest_colors_videos = Color.objects.all().order_by('-id')[feed_count:feed_count+5]
    # create feed object
    feed_array = []
    for post in latest_colors_videos:
        feed_array.append({"post_id":post.id,"instagram_link":post.post_instagram_link,'post_title':post.colors_song_title,"post_artist":post.colors_artist_name,"artist_photo":post.colors_artist_photo,"cover_poto":post.colors_cover_photo,"video_url":post.colors_video})
    return JsonResponse({"response":feed_array})


# if request has no parameters passed
def emptyParams(request):
    return JsonResponse({'error':'authentication failed'})


def isUserSignedIn(token):
    return True