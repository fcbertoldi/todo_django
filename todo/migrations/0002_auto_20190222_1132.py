# Generated by Django 2.1.7 on 2019-02-22 14:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('T', 'TODO'), ('S', 'STARTED'), ('W', 'WAITING'), ('D', 'DONE'), ('C', 'CANCELLED')], default='T', max_length=1),
        ),
    ]
