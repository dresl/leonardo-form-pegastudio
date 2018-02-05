# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import leonardo.module.media.fields.multistorage_file


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0007_auto_20180204_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pegastudioproducts',
            name='document',
        ),
        migrations.AddField(
            model_name='pegastudioproducts',
            name='file',
            field=leonardo.module.media.fields.multistorage_file.MultiStorageFileField(max_length=255, upload_to=leonardo.module.media.fields.multistorage_file.generate_filename_multistorage, null=True, verbose_name='file', blank=True),
        ),
    ]
