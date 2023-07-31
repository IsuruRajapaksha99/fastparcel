"""
URL configuration for Fastparcel project.

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
from django.contrib import admin
from django.urls import path,include
from core import views  # new
from django.contrib.auth import views as auth_views
from core.customer import views as customer_views
from core.courier import views as courier_views


customer_urlpatterns = [
    path('', customer_views.home, name='home'),
]

courier_urlpatterns = [
    path('', courier_views.home, name='home'),
]

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),

    path('', views.home, name='home'),

    path('sign_in/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='sign-in'),
    path('sign_out/', auth_views.LogoutView.as_view(next_page='/'), name='sign-out'),

    path('sign_up/', views.sign_up, name='sign-up'),

    path('customer/', include((customer_urlpatterns, 'customer'))),
    path('courier/', include((courier_urlpatterns, 'courier')))
]
    