# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0019_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(default=1, verbose_name='Po\u010det kus\u016f')),
            ],
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['description'], 'verbose_name': 'Dokument', 'verbose_name_plural': 'Dokumenty'},
        ),
        migrations.AddField(
            model_name='documentproducts',
            name='document',
            field=models.ForeignKey(related_name='documentproduct_set', verbose_name='Dokument', to='leonardo_form_pegastudio.Document'),
        ),
    ]
