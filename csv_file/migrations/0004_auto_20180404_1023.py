# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_file', '0003_auto_20180404_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datafile', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='ABC',
        ),
    ]
