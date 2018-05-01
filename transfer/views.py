from rest_framework.decorators import api_view
from transfer.models import Transfer
from accounts.models import User
from transfer.serializers import TransferSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from collections import OrderedDict


# Create your views here.


class ListTransfer(generics.ListAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class ListCreateTransfer(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class RetrieveUpdateDestroyTransfer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer






@api_view(['GET', 'POST'])
def get_post_transfer(request):
    if request.method == 'GET':
        transfers = Transfer.objects.all()
        serialized_transfer = TransferSerializer(transfers, many=True)
        return Response(serialized_transfer.data)
    if request.method == 'POST':
        pass
