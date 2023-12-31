"""
URL configuration for Dating_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from dating.views import create_client, match_client,\
    client_list, nearby_clients


urlpatterns = [
    path('api/clients/create', create_client),
    path('api/clients/<int:id>/match', match_client),
    path('api/list', client_list),
    path('api/nearby', nearby_clients),
]
