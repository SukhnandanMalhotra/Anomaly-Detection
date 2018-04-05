# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_file', '0007_auto_20180404_1150'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]
