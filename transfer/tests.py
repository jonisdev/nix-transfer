from django.test import TestCase, Client
from django.urls import reverse
from .models import Transfer
from transfer.serializers import TransferSerializer
from accounts.models import User
from rest_framework import status
from datetime import datetime as dt

# initializes the Client class to be used at the tests
client = Client()

class TransferMethodTests(TestCase):

    def setUp(self):
        self.u01 = User.objects.create(name='PyBr co.', cnpj=31415850000508)

        self.t01 = Transfer.objects.create(
            user_id=self.u01,
            payer_name='Jonatan',
            payer_bank=2,
            payer_agency=3334,
            payer_account=188003,
            beneficiary_name='Alexsandra',
            beneficiary_bank=1,
            beneficiary_agency=1800,
            beneficiary_account=201499,
            amount=4999.99,
        )

        self.t02 = Transfer.objects.create(
            user_id=self.u01,
            payer_name='John',
            payer_bank=2,
            payer_agency=3334,
            payer_account=188003,
            beneficiary_name='May',
            beneficiary_bank=1,
            beneficiary_agency=1880,
            beneficiary_account=201499,
            amount=4999.99,
        )

        self.t03 = Transfer.objects.create(
            user_id=self.u01,
            payer_name='Jonatan',
            payer_bank=2,
            payer_agency=3334,
            payer_account=188003,
            beneficiary_name='Benites',
            beneficiary_bank=1,
            beneficiary_agency=18800,
            beneficiary_account=201499,
            amount=4999.99,
        )

    def test_transfer_type(self):
        self.t03.set_transfer_type()

        current_datetime = dt.now()
        current_time = dt.time(current_datetime)
        current_date = current_datetime.date()
        initial_ted_time = dt.time(dt(
            current_date.year, current_date.month, current_date.day, 10, 0, 0))
        final_ted_time = dt.time(dt(
            current_date.year, current_date.month, current_date.day, 16, 0, 0))

        if self.t03.payer_bank == self.t03.beneficiary_bank:
            ttype = 'CC'
        elif dt.weekday(current_datetime) in (5, 6):
            ttype = 'DOC'
        elif initial_ted_time < current_time < final_ted_time \
                and self.t03.amount < 5000.0:
            ttype = 'TED'
        else:
            ttype = 'DOC'

        self.assertEqual(self.t03.type, ttype)

    def test_tranfer_status(self):
        self.t03.set_transfer_status()

        if 100000.0 < self.t03.amount <= 0:
            tstatus = 'ERRO'
        else:
            tstatus = 'OK'
        self.assertEqual(self.t03.status, tstatus)

    def test_get_all_transfers(self):
        response = client.get(reverse('transfers:transfers'))
        transfers = Transfer.objects.all()

        serializer = TransferSerializer(transfers, many=True)
        a = serializer.data
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)





