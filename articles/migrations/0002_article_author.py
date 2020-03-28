# Generated by Django 2.0.7 on 2020-03-20 21:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=None, on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]