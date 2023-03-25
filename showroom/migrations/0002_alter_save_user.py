# Generated by Django 4.1.6 on 2023-03-25 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save', to=settings.AUTH_USER_MODEL),
        ),
    ]
