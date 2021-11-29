![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# django-graphics_base

## Quickstart

1. Install the app from GitHub:

   ```bash
   pipenv install -e git+https://github.com/reuters-graphics/django-graphics_base.git#egg=graphics_base
   ```

2. Add "graphics_base" to your INSTALLED_APPS setting like this:

   ```python
   INSTALLED_APPS = [
       # ...
       "graphics_base",
   ]
   ```

3. Include the graphics_base URLconf in your project's `urls.py` like this:

   ```python
   from django.urls import include, path

   urlpatterns = [
      # ...
      path("", include("graphics_base.urls")),
   ]
   ```

4. Add a template to override admin styles:

   ```python
   # settings.py
   TEMPLATES = [
      {
         "BACKEND": "django.template.backends.django.DjangoTemplates",
         "DIRS": [BASE_DIR.parent / "templates"], # ADD THIS
         "APP_DIRS": True,
         "OPTIONS": {
               "context_processors": [
                  "django.template.context_processors.debug",
                  "django.template.context_processors.request",
                  "django.contrib.auth.context_processors.auth",
                  "django.contrib.messages.context_processors.messages",
               ]
         },
      }
   ]
   ```

   ```jinja
   <!-- tempaltes/admin/base_site.html -->
   {% extends "admin/base_site.html" %}
   {% load graphics_base_manifest %}

   {% block branding %}
   <h1 id="site-name"><a href="{% url 'admin:index' %}"><img src="https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-light.svg" /> Admin</a></h1>
   {% endblock %}

   {% block extrastyle %}
   {{ block.super }}
   {% vite 'src/admin.js' %}
   {% endblock %}
   ```

5. Run `python manage.py migrate` to create the graphics_base models.
