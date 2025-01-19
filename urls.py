from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from django.conf import settings
from django.conf.urls.static import static
from gallery import views  # Import your views from the gallery app

urlpatterns = [
    # Admin URL path
    path('admin/', admin.site.urls),

    # Application-specific URL paths
    path('home', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),

    # Including gallery URLs from the gallery app
    path('gallery/', include('gallery.urls')),  # Ensure 'gallery/urls.py' exists and is defined properly
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
