# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0003_auto_20180204_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='document',
            field=models.FileField(upload_to=b'documents/', verbose_name='Dokument'),
        ),
    ]
