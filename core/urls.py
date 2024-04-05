from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
app_name = 'core'
urlpatterns = [
    path('', views.frontpage, name = 'frontpage'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('mangaByLikes/', views.mangaByLikes, name = 'mangaByLikes'),
    path('likedManga/', views.likedManga, name = 'likedManga'),
    path('mangaByUpdate/', views.mangaByUpdate, name = 'mangaByUpdate'),
    path('filterView/', views.filterView, name = 'filterView'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'core/frontpage.html'), name = 'logout'),
    path('<int:pk>/', views.mangaByTag, name = 'mangaByTag'),
    path('searchpage/', views.searchpage, name = 'searchpage'),
]