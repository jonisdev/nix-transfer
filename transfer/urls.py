from django.urls import path
from .views import get_post_transfer, ListCreateTransfer
app_name = 'transfers'

urlpatterns = [
    path('transfers/', ListCreateTransfer.as_view(), name='transfers'),
    # path('transfers/', CreateTransfer.as_view(), name='create-transfer'),
]
