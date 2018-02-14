# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0024_auto_20180212_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pegastudioorders',
            name='file',
        ),
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='file',
            field=models.FileField(upload_to=b'documents', verbose_name='Soubor'),
        ),
    ]
