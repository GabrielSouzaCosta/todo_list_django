from django.db import models
import datetime
from django.utils import timezone

class TodoItem(models.Model):
    text = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)
    doing = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    def was_added_recently(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.text
