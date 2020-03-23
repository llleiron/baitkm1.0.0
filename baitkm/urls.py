from django.contrib import admin
from django.urls import path, include 
from users import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('router/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('Announcement/', include('announcement.urls')),
]
