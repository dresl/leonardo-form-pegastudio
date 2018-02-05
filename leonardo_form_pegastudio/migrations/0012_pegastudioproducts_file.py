# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0011_remove_pegastudioproducts_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegastudioproducts',
            name='file',
            field=models.FileField(default=b'/static/bp.pdf', upload_to=b'', max_length=255, verbose_name='file'),
        ),
    ]
