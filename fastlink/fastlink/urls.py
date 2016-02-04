from django.conf.urls import url
from django.contrib import admin

from fastlink.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', FastcampusRedirectView.as_view(), name='home'),

    url(
        r'^(?P<hash_id>\w+)/$',
        ResourceRedirectView.as_view(),
        name="resource-redirect",
    ),
]
