from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_urls
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('/accounts/login/') if not request.user.is_authenticated else None),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
