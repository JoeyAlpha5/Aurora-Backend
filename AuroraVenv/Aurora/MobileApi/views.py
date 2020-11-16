from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from .models import Color
from lyricsgenius import Genius

# Create your views here.
def getFeed(request):
    feed_count = int(request.GET['feed_count'])
    feed_array = []
    # if there's a search term get the search results
    if 'search_term' in request.GET:
        search_term = request.GET['search_term']
        feed_array = getSearchPostArray(feed_count,search_term)
    else:
        latest_colors_videos = Color.objects.all().order_by('-id')[feed_count:feed_count+5]
        for post in latest_colors_videos:
            feed_array.append({"post_id":post.id,"instagram_link":post.post_instagram_link,'post_title':post.colors_song_title,"post_artist":post.colors_artist_name,"artist_photo":post.colors_artist_photo,"cover_poto":post.colors_cover_photo,"video_url":post.colors_video})

    return JsonResponse({"response":feed_array})


# get search results
def getSearchPostArray(feed_count,search_term):
    colors_videos_array = []
    colors_videos = Color.objects.filter(colors_artist_name__istartswith=search_term)[feed_count:feed_count+5]
    if len(colors_videos) == 0:
        colors_videos = Color.objects.filter(colors_song_title__istartswith=search_term)[feed_count:feed_count+5]
    for video in colors_videos:
        colors_videos_array.append({"post_id":video.id,"instagram_link":video.post_instagram_link,'post_title':video.colors_song_title,"post_artist":video.colors_artist_name,"artist_photo":video.colors_artist_photo,"cover_poto":video.colors_cover_photo,"video_url":video.colors_video})
    return colors_videos_array
    

# get song lyrics and other required data
def getLyrics(request):
    song_title = request.GET['title']
    artist_name = request.GET['artist']
    genius = Genius('WriwiCbp2JoJJMWVY_J2f7o8aZZUChedm7wJLFl1lFvz15mKJqHORYa0gx8q0sG2')
    song = genius.search_song(song_title, artist_name)

    return JsonResponse({'cover_image':song._body['song_art_image_thumbnail_url'],'lyrics':str(song.lyrics),'title':song._body['title'],'date':song._body['release_date_for_display'],'artist':song._body['primary_artist']['name']})



# if request has no parameters passed
def emptyParams(request):
    return JsonResponse({'error':'authentication failed'})


def isUserSignedIn(token):
    return True