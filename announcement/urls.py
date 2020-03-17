from rest_framework import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('create', AnnouncementCreateAPIView.as_view()),
    path('all', AnnouncementListAPIView.as_view()),
    path('StepOne/sale/<int:pk>', SaleUpdateAPIView.as_view()),
    path('StepOne/rent/<int:pk>', RentUpdateAPIView.as_view()),
    path('StepTwo/<int:pk>', PropertyTypeUpdateAPIView.as_view()),
    path('StepThree/Residential/<int:pk>', PropertyResidentialUpdateAPIView.as_view()),
    path('StepThree/Retail/<int:pk>', PropertyRetailUpdateAPIView.as_view()),
    path('StepThree/Commercial/<int:pk>', PropertyRetailUpdateAPIView.as_view()),
    path('StepThree/Land/<int:pk>', PropertyLandUpdateAPIView.as_view()),
    path('StepFour/<int:pk>', AnnouncementdescriptionAPIView.as_view()),
    path('StepFive/<int:pk>', SetLocationAPIView.as_view()),
    path('StepSix/<int:pk>', ImageAPIView.as_view())
]
