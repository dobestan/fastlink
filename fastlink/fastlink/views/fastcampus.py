from django.views.generic.base import RedirectView


class FastcampusRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return "https://fastcamp.us/"
