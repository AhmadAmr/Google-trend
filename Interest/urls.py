from django.urls import  path
from .views import  getGoogleTrends ,getGoogleTrendsMap
urlpatterns = [
    path('historical/<str:kw>/' ,getGoogleTrends.as_view()),   
    path('map/',getGoogleTrendsMap.as_view())  
]