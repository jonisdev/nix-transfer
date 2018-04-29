from .models import Transfer
from datetime import datetime as dt
import calendar


def validate_transction_type(transferency):

    current_datetime = dt.now()

    current_time = dt.time(current_datetime)
    current_date = current_datetime.date()
    initial_ted_time = dt.time(dt(
        current_date.year, current_date.month, current_date.day, 10, 0, 0))
    final_ted_time = dt.time(dt(
        current_date.year, current_date.month, current_date.day, 16, 0, 0))

    if transferency.paying_bank == transferency.beneficiary_bank:
        return transferency.type == transferency.TYPE_CHOICES.CC
    elif dt.weekday(current_datetime) in (5, 6):
        return transferency.type == transferency.TYPE_CHOICES.DOC
    elif current_time > initial_ted_time and current_time < final_ted_time and \
            transferency.amount < 5000.0:
        return transferency.type == transferency.TYPE_CHOICES.TED
    else:
        return transferency.type == transferency.TYPE_CHOICES.DOC


