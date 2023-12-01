from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        verbose_name='武器種・カテゴリ',
        max_length=20
    )

    def __str__(self):
        return self.title
    
class Monster(models.Model):
    title = models.CharField(
        verbose_name='モンスター',
        max_length=20
    )

    def __str__(self):
        return self.title    

class ArimsPost(models.Model):
    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー名',
        on_delete=models.CASCADE
    )
    
    monster_name=models.ForeignKey(
        Monster,
        verbose_name='モンスター',
        on_delete=models.PROTECT
    )


    category = models.ForeignKey(
        Category,
        verbose_name='武器種・カテゴリ',
        on_delete = models.PROTECT
    )

    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )

    comment = models.TextField(
        verbose_name='コメント',
    )

    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to='photos',
    )

    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to='photos',
        blank=True,
        null=True
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add='True',
    )

    def __str__(self):
        return self.title
    