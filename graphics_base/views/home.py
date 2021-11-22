from django.views.generic.base import TemplateView
from graphics_base.utils.auth import secure


@secure
class Home(TemplateView):
    template_name = "graphics_base/home.html"
