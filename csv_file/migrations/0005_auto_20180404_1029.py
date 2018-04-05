# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_file', '0004_auto_20180404_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('task_name', models.CharField(max_length=20)),
                ('task_desc', models.TextField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/')),
                ('doc', models.FileField(default='Doc/None/No-doc.pdf', upload_to='Doc/')),
            ],
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]
