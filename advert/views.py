from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AdvertSerializer
from .models import Advert


class AdvertListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        advert_all = Advert.objects.all()
        advert_serializer = AdvertSerializer(instance=advert_all, many=True)
        return Response(advert_serializer.data, status=status.HTTP_200_OK)


class AdvertDetailAPIView(APIView):

    def get(self, request, id_advert, *args, **kwargs):
        advert_detail = get_object_or_404(Advert, pk=id_advert)
        advert_detail.views += 1
        advert_detail.save()
        advert_serializer = AdvertSerializer(instance=advert_detail)
        return Response(advert_serializer.data, status=status.HTTP_200_OK)


