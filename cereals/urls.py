from django.urls import path
from .views import CerealList, CerealDetail

urlpatterns = [
    path('cereals/', CerealList.as_view(), name= 'cereal_list'),
    path('cereals/<int:pk>/', CerealDetail.as_view(), name= 'cereal_detail')
]