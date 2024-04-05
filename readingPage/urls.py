from django.urls import path
from .views import readingPage
app_name = 'readingPage'
urlpatterns = [
    path('<int:pk>/', readingPage, name = 'readingPage'),
]