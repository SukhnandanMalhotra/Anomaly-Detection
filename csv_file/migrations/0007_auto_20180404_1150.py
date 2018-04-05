# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_file', '0006_auto_20180404_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='title',
        ),
        migrations.AlterField(
            model_name='file',
            name='csv_file',
            field=models.FileField(default=None, upload_to='file/'),
        ),
    ]
