from accounts.models import User
from accounts.serializers import UserSerializer
from datetime import datetime as dt
from django_filters import  rest_framework as filters
from transfer.models import Transfer
from transfer.serializers import TransferSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class ListCreateTransfer(generics.ListCreateAPIView):
    serializer_class = TransferSerializer
    # filter_backends = (DjangoFilterBackend,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('updated_at', 'payer_name', 'beneficiary_name',)
    # search_fields = ('updated_at', 'payer_name', 'beneficiary_name',)

    def get_queryset(self):
        return Transfer.objects.filter(deleted_at=None)


class RetrieveUpdateDestroyTransfer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    # TODO - Implement logical exclusion
    def destroy(self, request, *args, **kwargs):
        try:
            my_query = self.get_queryset()
            obj = my_query.get(pk=kwargs['pk'])
        except Transfer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if obj.deleted_at:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                obj.deleted_at = dt.now()
                obj.save()
                return Response(status=status.HTTP_204_NO_CONTENT)



class ListCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Return empty list for get all transfers
    # def list(self, request, *args, **kwargs):
    #     return Response([OrderedDict()])


class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
