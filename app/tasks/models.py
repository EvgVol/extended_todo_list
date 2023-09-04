from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(_("category name"), max_length=50, blank=False)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Task(models.Model):

    name = models.CharField(_("tast name"), max_length=150, blank=False)
    category = models.ForeignKey(Category,
                                 verbose_name=_("category"),
                                 related_name='tasks',
                                 on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=_("user"),
                             related_name='user_tasks',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

    def __str__(self):
        return self.name
