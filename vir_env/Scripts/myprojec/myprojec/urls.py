"""myprojec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from myapps import views as myapps_views
from userapp import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapps_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="myapps/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="myapps/logout.html"), name="logout"),
    path( "register/", myapps_views.register, name="register"),
    path('product/<int:pk>/', myapps_views.PostDetailView.as_view(), name='Product-detail'),
    path('add_to_cart/<int:product_id>/', user_views.add_to_cart, name='add_to_cart'),
    path('cart/', user_views.cart_details, name='cart'),
    path('update-cart/<int:item_id>/', user_views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:cart_item_id>/', user_views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', user_views.checkout, name='checkout'),
    path('order-history/', user_views.order_history, name='order_history')

    



]
