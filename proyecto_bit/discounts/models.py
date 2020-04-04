import datetime

from django.db import models


class DateDiscount(models.Model):

    date = models.DateTimeField(default=datetime.datetime.now())


