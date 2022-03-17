from django.db import models

from user.models import User


class Notice(models.Model):
    notice_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    img1 = models.ImageField(upload_to="knowledge/notice/%Y/%m/%d/%H/%M/%S", blank=True)
    img2 = models.ImageField(upload_to="knowledge/notice/%Y/%m/%d/%H/%M/%S", blank=True)
    img3 = models.ImageField(upload_to="knowledge/notice/%Y/%m/%d/%H/%M/%S", blank=True)
    img4 = models.ImageField(upload_to="knowledge/notice/%Y/%m/%d/%H/%M/%S", blank=True)
    img5 = models.ImageField(upload_to="knowledge/notice/%Y/%m/%d/%H/%M/%S", blank=True)
    update_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-notice_no"]
