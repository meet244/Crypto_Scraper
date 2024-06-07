from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskManagerViewSet

from django.urls import path
from .views import TaskManagerViewSet

# Define the URL patterns for the API endpoints
urlpatterns = [
    # Endpoint for starting the scraping process
    path('taskmanager/start_scraping/', TaskManagerViewSet.as_view({'post': 'start_scraping'}), name='start_scraping'),

    # Endpoint for checking the status of the scraping process
    path('taskmanager/scraping_status/<uuid:pk>/', TaskManagerViewSet.as_view({'get': 'scraping_status'}), name='scraping_status'),
]

