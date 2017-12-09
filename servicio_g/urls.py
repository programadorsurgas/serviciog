from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from apps.sg_usuario_rest.viewsets import Usr_systemViewSet
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'usuarios', Usr_systemViewSet)

urlpatterns = [
    url(r'^', include('apps.sg_usuario.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^rest/', include(router.urls), name="restg"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

