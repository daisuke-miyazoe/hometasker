from django.conf import settings
from django.db import models
from django.utils import timezone


class Folder(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'フォルダ'
        verbose_name_plural = 'フォルダ'


class Task(models.Model):
    STATUS_CHOICES = [(1, '未完了'),(2, '作業中'),(3, '完了')]

    folder_id = models.ForeignKey(Folder, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    due_date =  models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'タスク'
        verbose_name_plural = 'タスク'
