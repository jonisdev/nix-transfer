from django.urls import path
from .views import RetrieveUpdateDestroyTransfer, ListCreateTransfer

app_name = 'transfers'

urlpatterns = [
    path('api/v1/transfers/', ListCreateTransfer.as_view(),
         name='get_post_transfers'),

    path('api/v1/transfers/<int:pk>',
         RetrieveUpdateDestroyTransfer.as_view(),
         name='get_put_delete_transfers'),
]
