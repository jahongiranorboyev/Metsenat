from django.db import models

from apps.utils.models import AbstractBaseModel


class DailyStatistics(AbstractBaseModel):
    date = models.DateField(unique=True)

    class Meta:
        managed = False
        verbose_name = "DailyStatistic"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return str(self.date)
