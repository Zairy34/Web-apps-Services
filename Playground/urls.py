from django.urls import path
from . import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path("hello/",views.product_list),
        path('success/', views.success, name='success'),
        path('services/', views.Services, name='services'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)