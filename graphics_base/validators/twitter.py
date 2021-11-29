import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_twitter_handle(value):
    if not re.match(r'^@\w{1,15}$"', value):
        raise ValidationError(
            _("%(value)s is not a valid twitter handle"),
            params={"value": value},
        )
