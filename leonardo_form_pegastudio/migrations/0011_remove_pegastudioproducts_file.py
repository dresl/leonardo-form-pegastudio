# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0010_auto_20180204_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pegastudioproducts',
            name='file',
        ),
    ]
