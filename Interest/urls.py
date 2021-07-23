from django.urls import  path
from .views import  getGoogleTrends 
urlpatterns = [
    path('historical/<str:kw>/' ,getGoogleTrends.as_view()),     
]