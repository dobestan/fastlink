from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from fastlink.models import Resource


class ResourceRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        resource = get_object_or_404(
            Resource,
            hash_id=kwargs['hash_id'],
        )

        return resource.url
