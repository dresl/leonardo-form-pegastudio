# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0021_remove_document_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentproducts',
            name='document_file',
            field=models.FileField(default=b'a', upload_to=b'documents/'),
        ),
    ]
