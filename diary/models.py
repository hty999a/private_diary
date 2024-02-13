####         ####
    #? 追加#
####         ####
from django.db import models ###最初入ってたやつ###これ以外は追加した。

from django.contrib.auth.models import AbstractUser ###1 追加###

class CustomUser(AbstractUser): ###2 追加###
    """拡張ユーザーモデル"""

    class Meta:
        verbose_name_plural = "CustomUser"
# Create your models here.

class Diary(models.Model):
    """日記モデル"""
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        return self.title