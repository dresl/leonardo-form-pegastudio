# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0005_remove_pegastudioproducts_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegastudioproducts',
            name='document',
            field=models.FileField(default=b'', upload_to=b'documents', verbose_name='Dokument'),
        ),
    ]
