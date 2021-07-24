from datetime import date
from django.shortcuts import render
from rest_framework.authtoken.views import APIView
from pytrends.request import TrendReq
from .serializers import DataSerializer ,MapSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
import pandas as pd
import json


class getGoogleTrends(APIView):
    permission_classes = [AllowAny]
    def get(self, request, kw="" ,format='json'):
        pytrends = TrendReq(hl='en-US')
        kw_list = []
        kw_list.append(kw)
        data= pytrends.get_historical_interest(kw_list, 
                                        cat=0, geo='', gprop='', sleep=0)
        data.reset_index(inplace=True)
        data['name']=kw
        data = data.drop(labels=['isPartial'],axis='columns')
        data = data.rename(columns={kw: 'term'})
        data=data.to_dict("records")
        
        serializer = DataSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            json_obj = serializer.data
            return Response(json_obj , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getGoogleTrendsMap(APIView):
    permission_classes = [AllowAny]
    def post(self, request ,format='json'):
        postdata=request.data
       
        first_term=postdata['first_term']
        
        second_term=postdata['second_term']
        pytrends = TrendReq(hl='en-US')
        kw_list = []
        kw_list.append(first_term)
        kw_list.append(second_term)
        print(kw_list)
        pytrends.build_payload(kw_list)
        data = pytrends.interest_by_region(resolution='USA', inc_low_vol=False)
        data.reset_index(inplace=True)
        data = data.rename(columns={first_term: 'first_term',second_term:'second_term'})
        data['first_term_name']=first_term
        data['second_term_name']=second_term
        data=data.to_dict("records")
        
        serializer = MapSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            json_obj = serializer.data
            return Response(json_obj , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
def IndexView(request):
    return render(request, 'index.html')

def MapView(request):
    return render(request, 'map.html')