from django.contrib.auth.models import User
from django.db import models
from graphics_base.validators import validate_twitter_handle


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    preferred_byline = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Preferred byline"
    )

    # Google
    google_email = models.EmailField(blank=True, null=True, verbose_name="Gmail")

    # twitter
    twitter_handle = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Twitter handle",
        validators=[validate_twitter_handle],
    )

    @property
    def byline(self):
        if self.preferred_byline:
            return self.preferred_byline
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return self.user.email
