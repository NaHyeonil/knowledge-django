from django.db import models

from user.models import User


class PointManagement(models.Model):
    point_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    update_at = models.DateTimeField(auto_now_add=True)
    approval = models.IntegerField(default=0, choices=[(0, 0), (1, 1)])
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-point_no"]