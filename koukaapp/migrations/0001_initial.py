# Generated by Django 4.0 on 2023-11-13 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='武器種')),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='モンスター')),
            ],
        ),
        migrations.CreateModel(
            name='ArimsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ１')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ2')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='koukaapp.category', verbose_name='武器種')),
                ('monster_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koukaapp.monster', verbose_name='モンスター')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', verbose_name='ユーザー名')),
            ],
        ),
    ]
