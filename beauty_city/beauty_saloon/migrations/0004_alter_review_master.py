# Generated by Django 3.2.19 on 2023-05-27 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty_saloon', '0003_auto_20230527_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='beauty_saloon.master'),
        ),
    ]
