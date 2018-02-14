# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0020_auto_20180212_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='document',
        ),
    ]
