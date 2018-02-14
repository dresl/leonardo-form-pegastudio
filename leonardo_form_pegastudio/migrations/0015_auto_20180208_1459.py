# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0014_auto_20180208_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='file',
            field=models.FileField(upload_to=b'documents/'),
        ),
    ]
