# Generated by Django 5.0.2 on 2024-03-13 14:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='장소명')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('classification', models.CharField(max_length=150, verbose_name='업종')),
                ('street_name_address', models.TextField(max_length=150, verbose_name='도로명주소')),
                ('hardness', models.FloatField(verbose_name='경도')),
                ('latitude', models.FloatField(verbose_name='위도')),
                ('like', models.IntegerField(default=0, verbose_name='좋아요수')),
                ('info', models.TextField(verbose_name='장소정보')),
                ('call', models.CharField(max_length=150, verbose_name='전화번호')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='태그명')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='리뷰내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='리뷰이미지')),
                ('score', models.IntegerField(verbose_name='리뷰점수')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='리뷰작성일')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
