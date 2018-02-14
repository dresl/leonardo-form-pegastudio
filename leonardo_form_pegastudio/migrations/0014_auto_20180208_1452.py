# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0013_auto_20180205_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='file',
            field=models.FileField(upload_to=b'documents'),
        ),
    ]
