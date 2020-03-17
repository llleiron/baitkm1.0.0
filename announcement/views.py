from rest_framework import generics
from .models import Announcement
from .serializers import *

class AnnouncementCreateAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementCreateSerializer

class AnnouncementListAPIView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListSerializer
    
class SaleUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachSaleSerializer

class PropertyTypeUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachPropertyTypeSerializer

class PropertyResidentialUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachPropertyResidentialSerializer

class PropertyRetailUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachPropertyRetailSerializer

class PropertyLandUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachPropertyLandSerializer

class AnnouncementdescriptionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachAnnouncementdescriptionSerializer

class SetLocationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachLocationSerializer

class ImageAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachImagesSerializer

class RentUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AttachRentSerializer