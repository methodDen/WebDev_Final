from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Время последнего изменения"
    )


class IsActiveMixin(models.Model):
    is_active = models.BooleanField(verbose_name=_("Is active?"), default=True)

    class Meta:
        abstract = True
