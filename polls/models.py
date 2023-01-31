from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    # cơ sở dữ liệu sẽ sử dụng tên trường (như question_text) làm tên cột)
    question_text = models.CharField(max_length=200)
    # 'date published' là nhãn hoặc tên chi tiết cho trường pub_date trong mô hình.
    # chỉ được sử dụng cho mục đích hiển thị, nó không ảnh hưởng đến hành vi hoặc các giá trị được lưu trữ trong trường pub_date.
    pub_date = models.DateTimeField('date published')
    # đại diện của một đối tượng
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text