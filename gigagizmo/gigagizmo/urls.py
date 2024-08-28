"""
URL configuration for gigagizmo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from ggapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('index', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.user_login, name="user_login"), 
    path('list-items',views.list_items, name="list_items"),
    path('item-details/<int:id>',views.item_details, name="item_details"),
    path('logout', views.user_logout, name="user_logout"), 
    path('add-to-cart/<int:component_id>',views.add_to_cart, name="add_to_cart"),
    path('display-cart-items',views.display_cart_items, name="display_cart_items"),
    path('remove-cart-items/<int:component_id>',views.remove_cart_items, name="remove_cart_items"),
    path('manage-addresses',views.manage_addresses, name="manage_addresses"),
    path('add-address',views.add_address, name="add_address"),
    path('set-address', views.set_address, name='set_address'),
    path('order-review/<int:sa_id>', views.order_review, name='order_review'),
    path('checkout-order/<int:sa_id>', views.checkout_order, name='checkout_order'),
    path('payment-order', views.payment_order, name="payment_order"),
    path('payment-process/<int:order_id>/<int:amount>', views.payment_process, name="payment_process")
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
