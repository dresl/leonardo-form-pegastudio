# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioorders',
            name='budova',
            field=models.CharField(max_length=255, verbose_name='Budova', choices=[(b'poz1', b'Zam\xc4\x9bstnanec'), (b'poz2', b'Student')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='cislo_uctu',
            field=models.CharField(default=b'37030561/0100', max_length=255, verbose_name='\u010c\xedslo \xfa\u010dtu'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='dic',
            field=models.CharField(default=b'CZ00216275', max_length=255, verbose_name='DI\u010c'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='fakturacni_udaje',
            field=models.CharField(default=b'Univerzita Pardubice, Studentsk\xc3\xa1 95, Pardubice 532 10', max_length=255, verbose_name='Faktura\u010dn\xed \xfadaje'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='fakulta',
            field=models.CharField(max_length=255, verbose_name='Fakulta', choices=[(b'poz1', b'Zam\xc4\x9bstnanec'), (b'poz2', b'Student')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='ic',
            field=models.CharField(default=b'00216275', max_length=255, verbose_name='I\u010c'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='katedra',
            field=models.CharField(max_length=255, verbose_name='Katedra', choices=[(b'poz1', b'Zam\xc4\x9bstnanec'), (b'poz2', b'Student')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='patro',
            field=models.CharField(max_length=255, verbose_name='Patro', choices=[(b'poz1', b'Zam\xc4\x9bstnanec'), (b'poz2', b'Student')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='porada_material',
            field=models.CharField(max_length=255, verbose_name='Chcete poradit s v\xfdb\u011brem materi\xe1lu?', choices=[(b'ano', b'Ano'), (b'ne', b'Ne')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='porada_poster',
            field=models.CharField(max_length=255, verbose_name='Chcete graficky zpracovat poster?', choices=[(b'ano', b'Ano'), (b'ne', b'Ne')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='pozice',
            field=models.CharField(max_length=255, verbose_name='Pozice', choices=[(b'poz1', b'Zam\xc4\x9bstnanec'), (b'poz2', b'Student')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='preprava',
            field=models.CharField(max_length=255, verbose_name='P\u0159eprava', choices=[(b'poz1', b'Zam\xc4\x9bstnanec'), (b'poz2', b'Student')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='prezentace',
            field=models.CharField(max_length=255, verbose_name='Prezentace', choices=[(b'poz1', b'Zam\xc4\x9bstnanec'), (b'poz2', b'Student')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='std',
            field=models.CharField(default=b'', max_length=255, verbose_name='st k\xf3d'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='zeme',
            field=models.CharField(max_length=255, verbose_name='Zem\u011b', choices=[(b'poz1', b'Zam\xc4\x9bstnanec'), (b'poz2', b'Student')]),
        ),
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='laminace',
            field=models.CharField(max_length=255, verbose_name='Laminace', choices=[(b'ano', b'Ano'), (b'ne', b'Ne')]),
        ),
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='material',
            field=models.CharField(max_length=255, verbose_name='Materi\xe1l', choices=[(b'ano', b'Ano'), (b'ne', b'Ne')]),
        ),
        migrations.AlterField(
            model_name='pegastudioproducts',
            name='pocet_kusu',
            field=models.PositiveIntegerField(default=1, verbose_name='Po\u010det kus\u016f'),
        ),
    ]
