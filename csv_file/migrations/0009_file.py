# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import csv_file.validators


class Migration(migrations.Migration):

    dependencies = [
        ('csv_file', '0008_delete_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('csv_file', models.FileField(default=None, validators=[csv_file.validators.validate_file], upload_to='file/')),
            ],
        ),
    ]
