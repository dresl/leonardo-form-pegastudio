# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0029_auto_20180214_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioorders',
            name='telefon',
            field=models.CharField(max_length=100, verbose_name='Telefon (ve tvaru: +420 123 456 789'),
        ),
    ]
