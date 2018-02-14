# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0017_auto_20180208_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegastudioorders',
            name='file',
            field=models.FileField(default=b'/static/bp.pdf', upload_to=b'documents', verbose_name='file'),
        ),
    ]
