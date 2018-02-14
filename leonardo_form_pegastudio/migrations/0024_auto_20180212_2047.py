# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0023_auto_20180212_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentproducts',
            name='document',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='DocumentProducts',
        ),
    ]
