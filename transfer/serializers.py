from rest_framework import serializers
from .models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        ordering = ('user_id',)
        fields = ('id', 'user_id', 'payer_name', 'payer_bank', 'payer_agency',
                  'payer_account', 'beneficiary_name', 'beneficiary_bank',
                  'beneficiary_agency', 'beneficiary_account', 'amount',
                  'type', 'status',
                  )
        # It prevents the field to be available in method like post or put.
        read_only_fields = ('type', 'status')
