# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_file', '0002_auto_20180404_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
