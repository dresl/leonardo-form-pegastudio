# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0008_auto_20180204_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='file',
            field=models.FileField(max_length=255, upload_to=b'', null=True, verbose_name='file', blank=True),
        ),
    ]
