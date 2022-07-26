# Generated by Django 4.1 on 2022-09-02 22:10

import Domes.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Domes', '0002_alter_dome_members_alter_dome_moderators'),
    ]

    operations = [
        migrations.AddField(
            model_name='dome',
            name='invitationstr',
            field=models.CharField(default=Domes.models.generate_random, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='dome',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='dome_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dome',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='dome_moderators', to=settings.AUTH_USER_MODEL),
        ),
    ]
