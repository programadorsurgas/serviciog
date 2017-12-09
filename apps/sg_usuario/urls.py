from django.conf.urls import url

from apps.sg_usuario.views import index

urlpatterns = [
    url(r'^$', index.as_view(), name="index"),
]