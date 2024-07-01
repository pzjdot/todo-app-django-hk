

# Create your models here.
from django.db import models


# Task模型，包含了待办事项的名称，是否完成，创建时间和更新时间，并使用str方法返回task字段
class Task(models.Model):
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
