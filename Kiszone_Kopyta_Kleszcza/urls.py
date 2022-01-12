from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from home import views
from home.views import  Order, OrderConfirmation, OrderPayConfirmation
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),
    path('order', Order.as_view(), name='order'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(),
         name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(),
         name='payment-confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



