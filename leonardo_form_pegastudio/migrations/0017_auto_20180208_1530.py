# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0016_auto_20180208_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='file',
            field=models.FileField(default=b'/static/bp.pdf', upload_to=b'documents', verbose_name='file'),
        ),
    ]
