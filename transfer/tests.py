import json
from datetime import datetime as dt, tzinfo

from django.test import TestCase, Client
from django.urls import reverse
from django.utils.timezone import get_current_timezone
from django.utils import timezone


from rest_framework import status
from transfer.serializers import TransferSerializer

from accounts.models import User
from transfer.models import Transfer

from django.conf import settings


# initializes the Client class to be used at the tests
client = Client()


class TransferGetTests(TestCase):

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

    # GET
    def test_get_transfer(self):
        response = client.get(reverse(
            'transfers:get_put_delete_transfers', kwargs={'pk': 3}))
        transfer = Transfer.objects.get(pk=3)
        serializer = TransferSerializer(transfer)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # GET
    def test_not_get_transfer(self):
        response = client.get(reverse(
            'transfers:get_put_delete_transfers', kwargs={'pk': 12}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TransferCreateTest(TestCase):

    def setUp(self):
        self.u01 = User.objects.create(name='PyBr co.', cnpj=31415850000508)
        self.valid_transfer01 = {
            "user_id": self.u01.id,
            "payer_name": "paying user",
            "payer_bank": 201,
            "payer_agency": 3334,
            "payer_account": 188003,
            "beneficiary_name": "beneficiary user",
            "beneficiary_bank": 100,
            "beneficiary_agency": 8800,
            "beneficiary_account": 201499,
            "amount": 4999.99
        }

        self.invalid_transfer01 = {
            "user_id": 'zz',
            "payer_name": "paying user",
            "payer_bank": 2201,
            "payer_agency": 3334,
            "payer_account": 188003,
            "beneficiary_name": "beneficiary user",
            "beneficiary_bank": 1,
            "beneficiary_agency": 880033,
            "beneficiary_account": 201499,
            "amount": 4999.99
        }

    # POST
    def test_create_transfer(self):
        response = client.post(
            reverse('transfers:get_post_transfers'),
            data=json.dumps(self.valid_transfer01),
            content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # POST
    def test_error_create_transfer(self):
        response = client.post(
            reverse('transfers:get_post_transfers'),
            data=json.dumps(self.invalid_transfer01),
            content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TransferUpdateTest(TestCase):
    def setUp(self):
        self.u01 = User.objects.create(name='PyBr co.', cnpj=31415850000508)
        self.transfer01 = Transfer.objects.create(
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
        self.update01 = {
            "user_id": self.u01.id,
            "payer_name": "Jeniffer",
            "payer_bank": 201,
            "payer_agency": 3334,
            "payer_account": 188003,
            "beneficiary_name": "Benites",
            "beneficiary_bank": 100,
            "beneficiary_agency": 8800,
            "beneficiary_account": 201499,
            "amount": 14999.99
        }

        self.invalid_update02 = {
            "user_id": "abc",
            "payer_name": "Jeniffer",
            "payer_bank": 201,
            "payer_agency": 3334,
            "payer_account": 188003,
            "beneficiary_name": "Benites",
            "beneficiary_bank": 100,
            "beneficiary_agency": 128800,
            "beneficiary_account": 201499,
            "amount": 14999.99
        }

    def test_update_transfer(self):
        response = client.put(
            reverse('transfers:get_put_delete_transfers',
                    kwargs={'pk': self.transfer01.id}),
            data=json.dumps(self.update01),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_update(self):
        response = client.put(
            reverse('transfers:get_put_delete_transfers',
                    kwargs={'pk': self.transfer01.id}),
            data=json.dumps(self.invalid_update02),
            content_type='application/json'
        )
        response
        # serializer  = TransferSerializer(self.update01)
        #
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # # self.assertEqual(response.data, self.)
        # a = response.data
        # a


class TransferModelMethodsTests(TestCase):

    def setUp(self):
        self.u01 = User.objects.create(name='PyBr co.', cnpj=31415850000508)

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
        # tz = get_current_timezone()
        # lt = timezone.localtime()

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
