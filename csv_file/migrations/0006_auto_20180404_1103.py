# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_file', '0005_auto_20180404_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('csv_file', models.FileField(upload_to='file/')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
