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

    # def list(self, request, *args, **kwargs):
    #     return Response([OrderedDict()])


    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if transfer_serializer.is_valid():
    #         transfer_serializer.sa
    #         data = transfer.data
    #         # t = Transfer(user_id=User.objects.get(pk=data['user_id']),
    #         #              payer_name=data['payer_name'],
    #         #              payer_bank=data['payer_bank'],
    #         #              payer_agency=data['payer_agency'],
    #         #              payer_account=data['payer_account'],
    #         #              beneficiary_name=data['beneficiary_name'],
    #         #              beneficiary_bank=data['beneficiary_bank'],
    #         #              beneficiary_agency=data['beneficiary_agency'],
    #         #              beneficiary_account=data['beneficiary_account'],
    #         #              amount=data['amount'],
    #         #              )
    #         # t.set_transfer_type()
    #         # t.set_transfer_status()
    #         if t.type == 'OK':
    #             t.save()
    #             return Response(transfer)
    #         else:
    #             return Response({'error': 'Transfêrencia acima de R$ 100.000,00'})


@api_view(['GET', 'POST'])
def get_post_transfer(request):
    if request.method == 'GET':
        transfers = Transfer.objects.all()
        serialized_transfer = TransferSerializer(transfers, many=True)
        return Response(serialized_transfer.data)
    if request.method == 'POST':
        pass
