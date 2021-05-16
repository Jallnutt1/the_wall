
from django.urls import path, include

urlpatterns = [
    path('', include('application.urls')),
    path('wall/', include('application_wall.urls')),
]
