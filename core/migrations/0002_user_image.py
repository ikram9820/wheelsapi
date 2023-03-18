# Generated by Django 4.0.2 on 2022-02-25 13:04

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=1, upload_to='user/profile', validators=[core.validators.validate_file_size]),
            preserve_default=False,
        ),
    ]
