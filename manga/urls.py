from django.urls import path
from . import views
from core.views import author
from .models import Chapter
app_name = 'manga'
urlpatterns = [
    path('<int:pk>/', views.detail, name = 'detail'),
    path('like/<int:pk>', views.LikeView, name = 'like_manga'),
    path('author/<int:pk>', author, name = 'author')
]