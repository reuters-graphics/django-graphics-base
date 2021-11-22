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
      path("graphics_base/", include("graphics_base.urls")),
   ]
   ```

4. Run `python manage.py migrate` to create the graphics_base models.
