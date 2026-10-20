from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicionando as rotas de login e logout padrão do Django
    path('login/', auth_views.LoginView.as_view(template_name='manutencao/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Rotas do seu app
    path('', include('manutencao.urls')),
]