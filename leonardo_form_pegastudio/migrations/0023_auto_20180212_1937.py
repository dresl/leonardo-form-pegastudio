# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0022_documentproducts_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentproducts',
            name='document_file',
            field=models.FileField(upload_to=b'documents/'),
        ),
    ]
