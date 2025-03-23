from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, response
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('test', lambda request: render(request,"main.html",content_type="application/json")),
    path('api/', include('base.api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
