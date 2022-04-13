from django.db import models

from user.models import User


class Trade(models.Model):
    trade_no = models.AutoField(primary_key=True)
    application_item = models.CharField(max_length=100)
    processing = models.IntegerField(default=0, choices=[(0, 0), (1, 1)])
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    def __str__(self) -> str:
        return self.application_item

    class Meta:
        ordering = ["-trade_no"]
