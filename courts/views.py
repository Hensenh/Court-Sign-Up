from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from courts.models import Court
from courts.serializers import CourtSerializer
from rest_framework import generics


class CourtList(generics.ListAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


@api_view(['POST'])
def push_player(request):
    if request.method == 'POST':
        current_court = Court.objects.get(request.data.id)
        current_court.on_court = current_court.wait_list[0]
        current_court.wait_list = current_court.wait_list[1:]
        current_court.save()
        return Response({"message": "Court Updated", "info": current_court})

