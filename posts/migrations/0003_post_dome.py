# Generated by Django 4.0.3 on 2022-04-10 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Domes', '0001_initial'),
        ('posts', '0002_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dome',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='Domes.dome'),
        ),
    ]
