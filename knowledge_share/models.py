from django.db import models

from user.models import User


class Knowledge_Share(models.Model):
    knowledge_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ("CPU/MB/RAM", "CPU/메인보드/램"),
        ("VGA", "그래픽카드"),
        ("CASE", "케이스"),
        ("SSD/HDD/USB", "SSD/HDD/USB"),
        ("COOLER", "공랭/수랭쿨러"),
        ("POWER", "파워서플라이"),
        ("KEYBOARD/MOUSE", "키보드/마우스")],
                                blank=True)
    img1 = models.ImageField(upload_to="knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S", blank=True)
    img2 = models.ImageField(upload_to="knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S", blank=True)
    img3 = models.ImageField(upload_to="knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S", blank=True)
    img4 = models.ImageField(upload_to="knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S", blank=True)
    img5 = models.ImageField(upload_to="knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S", blank=True)
    update_at = models.DateTimeField(auto_now_add=True)
    view_cnt = models.PositiveIntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-knowledge_no"]
