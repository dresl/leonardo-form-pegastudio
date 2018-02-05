# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0012_pegastudioproducts_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioorders',
            name='email',
            field=models.EmailField(default=b'', max_length=254, verbose_name='E-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='jmeno',
            field=models.CharField(default=b'', max_length=255, verbose_name='Jm\xe9no', blank=True),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='prijmeni',
            field=models.CharField(default=b'', max_length=255, verbose_name='P\u0159\xedjmen\xed'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='telefon',
            field=models.PositiveIntegerField(default=None, verbose_name='Telefon', blank=True),
        ),
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='file',
            field=models.FileField(default=b'/static/bp.pdf', upload_to=b'documents', max_length=255, verbose_name='file'),
        ),
    ]
