from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home.views import Order, OrderConfirmation, OrderPayConfirmation, home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('order/', Order.as_view(), name='order'),
                  path('', home.as_view(), name='index'),
                  path('order-confirmation/<int:pk>', OrderConfirmation.as_view(),
                       name='order-confirmation'),
                  path('payment-confirmation/', OrderPayConfirmation.as_view(),
                       name='payment-confirmation'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
