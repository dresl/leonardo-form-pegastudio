# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_form_pegastudio', '0028_auto_20180214_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegastudioorders',
            name='budova',
            field=models.CharField(max_length=255, verbose_name='Budova', choices=[(b'ha', b'HA'), (b'hba', b'HB - A'), (b'hbb', b'HB - B'), (b'hbc', b'HB - C'), (b'hbd', b'HB - D'), (b'hce', b'HC - E'), (b'hcf', b'HC - F'), (b'hcg', b'HC - G'), (b'ea', b'EA - Studentsk\xc3\xa1 84'), (b'eb', b'EB - Studentsk\xc3\xa1 95'), (b'da', b'DA - Studentsk\xc3\xa1 95'), (b'db', b'DB - Studentsk\xc3\xa1 95'), (b'dc', b'DC - Studentsk\xc3\xa1 95'), (b'dd', b'DD - Doubravice 41'), (b'g', b'G - Stava\xc5\x99ov 97'), (b'pavil', b'Pavilon - Doubravice 41'), (b'ca', b'CA - n\xc3\xa1m. \xc4\x8cs. legi\xc3\xad 565'), (b'cb', b'CB - n\xc3\xa1m. \xc4\x8cs. legi\xc3\xad 565'), (b'ua', b'UA - Studentsk\xc3\xa1 519'), (b'uk', b'UK - Studentsk\xc3\xa1 519'), (b'za', b'ZA - Pr\xc5\xafmyslov\xc3\xa1 395'), (b'zb', b'ZB - Pr\xc5\xafmyslov\xc3\xa1 395'), (b'zc', b'ZC - Pr\xc5\xafmyslov\xc3\xa1 395'), (b'zd', b'ZD - Pr\xc5\xafmyslov\xc3\xa1 395'), (b'ze', b'ZE - Pr\xc5\xafmyslov\xc3\xa1 395'), (b'z', b'Z - Z\xc3\xa1mek 1'), (b'r', b'R - Studentsk\xc3\xa1 95'), (b'jazcentrum', b'Jazykov\xc3\xa9 centrum - Studentsk\xc3\xa1 95'), (b'ta', b'TA - Kun\xc4\x9btick\xc3\xa1 92'), (b'jinezprav', b'Jin\xc3\xa9(napi\xc5\xa1te do zpr\xc3\xa1vy)...')]),
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
            name='email',
            field=models.EmailField(default=b'', max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='fakturacni_udaje',
            field=models.CharField(default=b'Univerzita Pardubice, Studentsk\xc3\xa1 95, 532 10 Pardubice', max_length=255, verbose_name='Faktura\u010dn\xed \xfadaje'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='fakulta',
            field=models.CharField(max_length=255, verbose_name='Fakulta', choices=[(b'fcht', b'FCHT - Fakulta chemicko-technologick\xc3\xa1'), (b'dfjp', b'DFJP - Dopravn\xc3\xad fakulta Jana Pernera'), (b'fes', b'FES - Fakulta ekonomicko-spr\xc3\xa1vn\xc3\xad'), (b'fei', b'FEI - Fakulta elektrotechniky a informatiky'), (b'ff', b'FF - Fakulta filozofick\xc3\xa1'), (b'fzs', b'FZS - Fakulta zdravotnick\xc3\xbdch studi\xc3\xad'), (b'fr', b'FR - Fakulta restaurov\xc3\xa1n\xc3\xad'), (b'rek', b'Rektor\xc3\xa1t')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='ic',
            field=models.CharField(default=b'00216275', max_length=255, verbose_name='I\u010c'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='jmeno',
            field=models.CharField(default=b'', max_length=255, verbose_name='Jm\xe9no'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='katedra',
            field=models.CharField(max_length=255, verbose_name='Katedra', choices=[(b'FCHT', ((b'fchtkatanalchem', b'FCHT - Katedra analytick\xc3\xa9 chemie'), (b'fchtkatanortech', b'FCHT - Katedra anorganick\xc3\xa9 technologie'), (b'fchtkatbioved', b'FCHT - Katedra biologick\xc3\xbdch a biochemick\xc3\xbdch v\xc4\x9bd'), (b'fchtkatfyzchem', b'FCHT - Katedra fyzik\xc3\xa1ln\xc3\xad chemie'), (b'fchtkatobecanorg', b'FCHT - Katedra obecn\xc3\xa9 a anorganick\xc3\xa9 chemie'), (b'fchtkatpolfot', b'FCHT - Katedra polygrafie a fotofyziky'), (b'fchtkatekomanchemport', b'FCHT - Katedra ekonomiky a managementu chem. a potr. pr\xc5\xafm.'), (b'fchtustenermat', b'FCHT - \xc3\x9astav energetick\xc3\xbdch materi\xc3\xa1l\xc5\xaf'), (b'fchtustenvchiing', b'FCHT - \xc3\x9astav enviroment\xc3\xa1ln\xc3\xadho a chemick\xc3\xa9ho in\xc5\xbeen\xc3\xbdrstv\xc3\xad'), (b'fchtustchemtechlat', b'FCHT - \xc3\x9astav chemie a technologie makromolekul\xc3\xa1rn\xc3\xadch l\xc3\xa1tek'), (b'fchtustorgchemtech', b'FCHT - \xc3\x9astav organick\xc3\xa9 chemie a technologie'), (b'fchtkataplfyzmat', b'FCHT - \xc3\x9astav aplikovan\xc3\xa9 fyziky a matematiky'), (b'fchtkatstudod', b'FCHT - Studijn\xc3\xad odd\xc4\x9blen\xc3\xad'), (b'fchtkatjine', b'FCHT - Jin\xc3\xa9(napi\xc5\xa1te do zpr\xc3\xa1vy)...'))), (b'DFJP', ((b'dfjpkatinfdop', b'DFJP - Katedra informatiky v doprav\xc4\x9b'), (b'dfjpkatprosdia', b'DFJP - Katedra dopravn\xc3\xadch prost\xc5\x99edk\xc5\xaf a diagnostiky'), (b'dfjpkatdoprstav', b'DFJP - Katedra dopravn\xc3\xadho stavitelstv\xc3\xad'), (b'dfjpkattechrizstav', b'DFJP - Katedra technologie a \xc5\x99\xc3\xadzen\xc3\xad dopravy'), (b'dfjpkatdoprmang', b'DFJP - Katedra dopravn\xc3\xadho managementu, marketingu a logistiky'), (b'dfjpkatelekzab', b'DFJP - Katedra elektrotechniky, elek. a zabez. tech. v doprav\xc4\x9b'), (b'dfjpkatmechmatstroj', b'DFJP - Katedra mechaniky, materi\xc3\xa1l\xc5\xaf a \xc4\x8d\xc3\xa1sti stroj\xc5\xaf'), (b'dfjpkatstudod', b'DFJP - Studijn\xc3\xad odd\xc4\x9blen\xc3\xad'), (b'dfjpkatjine', b'DFJP - Jin\xc3\xa9(napi\xc5\xa1te do zpr\xc3\xa1vy)...'))), (b'FES', ((b'fesustavekoved', b'FES - \xc3\x9astav ekonomick\xc3\xbdch v\xc4\x9bd'), (b'fesustavpodnekonmang', b'FES - \xc3\x9astav podnikov\xc3\xa9 ekonomiky a managementu'), (b'fesustavmatkvant', b'FES - \xc3\x9astav matematiky a kvantitativn\xc3\xadch metod'), (b'fesustavsystinginf', b'FES - \xc3\x9astav syst\xc3\xa9mov\xc3\xa9ho in\xc5\xbeen\xc3\xbdrstv\xc3\xad a informatiky'), (b'fesustavspravsocved', b'FES - \xc3\x9astav spr\xc3\xa1vn\xc3\xadch a soci\xc3\xa1ln\xc3\xadch v\xc4\x9bd'), (b'fesustavregbezpved', b'FES - \xc3\x9astav region\xc3\xa1ln\xc3\xadch a bezpe\xc4\x8dnostn\xc3\xadch v\xc4\x9bd'), (b'fesustavstudod', b'FES - Studijn\xc3\xad odd\xc4\x9blen\xc3\xad'), (b'fesustavjine', b'FES - Jin\xc3\xa9(napi\xc5\xa1te do zpr\xc3\xa1vy)...'))), (b'FEI', ((b'feikatlek', b'FEI - Katedra elektrotechniky'), (b'feikatinftech', b'FEI - Katedra informa\xc4\x8dn\xc3\xadch technologi\xc3\xad'), (b'feikatmatfyz', b'FEI - Katedra matematiky a fyziky'), (b'feikatrizproc', b'FEI - Katedra \xc5\x99\xc3\xadzen\xc3\xad proces\xc5\xaf'), (b'feikatsofttech', b'FEI - Katedra softwarov\xc3\xbdch technologi\xc3\xad'), (b'feikatstudod', b'FEI - Studijn\xc3\xad odd\xc4\x9blen\xc3\xad'), (b'feikatjine', b'FEI - Jin\xc3\xa9(napi\xc5\xa1te do zpr\xc3\xa1vy)...'))), (b'FF', ((b'ffkatangamer', b'FF - Katedra anglistiky a amerikanistiky'), (b'ffkatcizjaz', b'FF - Katedra ciz\xc3\xadch jazyk\xc5\xaf'), (b'ffkatfil', b'FF - Katedra filosofie'), (b'ffkatlitkultslav', b'FF - Katedra liter\xc3\xa1rn\xc3\xad kultury a slavistiky'), (b'ffkatrel', b'FF - Katedra religionistiky'), (b'ffkatsockulantro', b'FF - Katedra soci\xc3\xa1ln\xc3\xad a kulturn\xc3\xad antropologie'), (b'ffkatvych', b'FF - Katedra v\xc4\x9bd o v\xc3\xbdchov\xc4\x9b'), (b'ffkathistved', b'FF - \xc3\x9astav historick\xc3\xbdch v\xc4\x9bd'), (b'ffkatstudod', b'FF - Studijn\xc3\xad odd\xc4\x9blen\xc3\xad'), (b'ffkatjine', b'FF - Jin\xc3\xa9(napi\xc5\xa1te do zpr\xc3\xa1vy)...'))), (b'FZS', ((b'fzskatoset', b'FZS - Katedra o\xc5\xa1et\xc5\x99ovatelstv\xc3\xad'), (b'fzskatporodaszdr', b'FZS - Katedra porodn\xc3\xad asistence a zdravotn\xc4\x9b soci\xc3\xa1ln\xc3\xad pr\xc3\xa1ce'), (b'fzskatklinobr', b'FZS - Katedra klinick\xc3\xbdch obor\xc5\xaf'), (b'fzskatinfomang', b'FZS - Katedra informatiky, managementu a radiologie'), (b'fzskatstudod', b'FZS - Studijn\xc3\xad odd\xc4\x9blen\xc3\xad'), (b'fzskatjine', b'FZS - Jin\xc3\xa9(napi\xc5\xa1te do zpr\xc3\xa1vy)...'))), (b'FR', ((b'fratelierrestmalb', b'FR - Ateli\xc3\xa9r restaurov\xc3\xa1n\xc3\xad n\xc3\xa1st\xc4\x9bnn\xc3\xa9 malby a sgrafita'), (b'fratelierrestkamen', b'FR - Ateli\xc3\xa9r restaurov\xc3\xa1n\xc3\xad kamene'), (b'fratelierrestpapir', b'FR - Ateli\xc3\xa9r restaurov\xc3\xa1n\xc3\xad pap\xc3\xadru, kni\xc5\xben\xc3\xad vazby a dokument\xc5\xaf'), (b'fratelierumeldel', b'FR - Ateli\xc3\xa9r restaurov\xc3\xa1n\xc3\xad um\xc4\x9bleck\xc3\xbdch d\xc4\x9bl na pap\xc3\xadru a souv. materi\xc3\xa1lech'), (b'frateliervytvarprip', b'FR - Ateli\xc3\xa9r v\xc3\xbdtvarn\xc3\xa9 p\xc5\x99\xc3\xadpravy'), (b'fratelierhumved', b'FR - Katedra humanitn\xc3\xadch v\xc4\x9bd'), (b'fratelierchemtech', b'FR - Katedra chemick\xc3\xa9 technologie'), (b'frateliercentrum', b'FR - Centrum pro restaurov\xc3\xa1n\xc3\xad a pam\xc3\xa1tkovou p\xc3\xa9\xc4\x8di'), (b'fratelierstudod', b'FR - Studijn\xc3\xad odd\xc4\x9blen\xc3\xad'), (b'fratelierjine', b'FR - Jin\xc3\xa9(napi\xc5\xa1te do zpr\xc3\xa1vy)...'))), (b'Dal\xc5\xa1\xc3\xad', ((b'upceknih', b'Univerzitn\xc3\xad knihovna'), (b'rektor', b'Rektor\xc3\xa1t'), (b'jazykcentrum', b'Jazykov\xc3\xa9 centrum'), (b'katsport', b'Katedra t\xc4\x9blov\xc3\xbdchovy a sportu')))]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='patro',
            field=models.CharField(max_length=255, verbose_name='Patro', choices=[(b'priz', b'P\xc5\x99\xc3\xadzem\xc3\xad'), (b'p1', b'1.'), (b'p2', b'2.'), (b'p3', b'3.'), (b'p4', b'4.'), (b'p5', b'5.'), (b'p6', b'6.'), (b'p7', b'7.'), (b'p8', b'8.'), (b'p9', b'9.'), (b'p10', b'10.'), (b'p11', b'11.'), (b'p12', b'12.'), (b'p13', b'13.')]),
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
            field=models.CharField(max_length=255, verbose_name='P\u0159eprava', choices=[(b'osobni', b'Osobn\xc3\xad (auto, vlak)'), (b'letecka', b'Leteck\xc3\xa1')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='prezentace',
            field=models.CharField(max_length=255, verbose_name='Prezentace', choices=[(b'interier', b'Interi\xc3\xa9r'), (b'exterier', b'Exteri\xc3\xa9r')]),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='std',
            field=models.CharField(default=b'', max_length=255, verbose_name='st k\xf3d'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='telefon',
            field=models.PositiveIntegerField(default=None, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='pegastudioorders',
            name='zeme',
            field=models.CharField(default=b'CZ', max_length=255, verbose_name='Zem\u011b', choices=[(b'Africa', ((b'DZ', b'Algeria'), (b'AO', b'Angola'), (b'BJ', b'Benin'), (b'BW', b'Botswana'), (b'BF', b'Burkina Faso'), (b'BI', b'Burundi'), (b'CM', b'Cameroon'), (b'CV', b'Cape Verde'), (b'CF', b'Central African Republic'), (b'TD', b'Chad'), (b'KM', b'Comoros'), (b'CG', b'Congo - Brazzaville'), (b'CD', b'Congo - Kinshasa'), (b'CI', b'C\xc3\xb4te d\xe2\x80\x99Ivoire'), (b'DJ', b'Djibouti'), (b'EG', b'Egypt'), (b'GQ', b'Equatorial Guinea'), (b'ER', b'Eritrea'), (b'ET', b'Ethiopia'), (b'GA', b'Gabon'), (b'GM', b'Gambia'), (b'GH', b'Ghana'), (b'GN', b'Guinea'), (b'GW', b'Guinea-Bissau'), (b'KE', b'Kenya'), (b'LS', b'Lesotho'), (b'LR', b'Liberia'), (b'LY', b'Libya'), (b'MG', b'Madagascar'), (b'MW', b'Malawi'), (b'ML', b'Mali'), (b'MR', b'Mauritania'), (b'MU', b'Mauritius'), (b'YT', b'Mayotte'), (b'MA', b'Morocco'), (b'MZ', b'Mozambique'), (b'NA', b'Namibia'), (b'NE', b'Niger'), (b'NG', b'Nigeria'), (b'RW', b'Rwanda'), (b'RE', b'R\xc3\xa9union'), (b'SH', b'Saint Helena'), (b'SN', b'Senegal'), (b'SC', b'Seychelles'), (b'SL', b'Sierra Leone'), (b'SO', b'Somalia'), (b'ZA', b'South Africa'), (b'SD', b'Sudan'), (b'SZ', b'Swaziland'), (b'ST', b'S\xc3\xa3o Tom\xc3\xa9 and Pr\xc3\xadncipe'), (b'TZ', b'Tanzania'), (b'TG', b'Togo'), (b'TN', b'Tunisia'), (b'UG', b'Uganda'), (b'EH', b'Western Sahara'), (b'ZM', b'Zambia'), (b'ZW', b'Zimbabwe'))), (b'Americas', ((b'AI', b'Anguilla'), (b'AG', b'Antigua and Barbuda'), (b'AR', b'Argentina'), (b'AW', b'Aruba'), (b'BS', b'Bahamas'), (b'BB', b'Barbados'), (b'BZ', b'Belize'), (b'BM', b'Bermuda'), (b'BO', b'Bolivia'), (b'BR', b'Brazil'), (b'VG', b'British Virgin Islands'), (b'CA', b'Canada'), (b'KY', b'Cayman Islands'), (b'CL', b'Chile'), (b'CO', b'Colombia'), (b'CR', b'Costa Rica'), (b'CU', b'Cuba'), (b'DM', b'Dominica'), (b'DO', b'Dominican Republic'), (b'EC', b'Ecuador'), (b'SV', b'El Salvador'), (b'FK', b'Falkland Islands'), (b'GF', b'French Guiana'), (b'GL', b'Greenland'), (b'GD', b'Grenada'), (b'GP', b'Guadeloupe'), (b'GT', b'Guatemala'), (b'GY', b'Guyana'), (b'HT', b'Haiti'), (b'HN', b'Honduras'), (b'JM', b'Jamaica'), (b'MQ', b'Martinique'), (b'MX', b'Mexico'), (b'MS', b'Montserrat'), (b'AN', b'Netherlands Antilles'), (b'NI', b'Nicaragua'), (b'PA', b'Panama'), (b'PY', b'Paraguay'), (b'PE', b'Peru'), (b'PR', b'Puerto Rico'), (b'BL', b'Saint Barth\xc3\xa9lemy'), (b'KN', b'Saint Kitts and Nevis'), (b'LC', b'Saint Lucia'), (b'MF', b'Saint Martin'), (b'PM', b'Saint Pierre and Miquelon'), (b'VC', b'Saint Vincent and the Grenadines'), (b'SR', b'Suriname'), (b'TT', b'Trinidad and Tobago'), (b'TC', b'Turks and Caicos Islands'), (b'VI', b'U.S. Virgin Islands'), (b'US', b'United States'), (b'UY', b'Uruguay'), (b'VE', b'Venezuela'))), (b'Asia', ((b'AF', b'Afghanistan'), (b'AM', b'Armenia'), (b'AZ', b'Azerbaijan'), (b'BH', b'Bahrain'), (b'BD', b'Bangladesh'), (b'BT', b'Bhutan'), (b'BN', b'Brunei'), (b'KH', b'Cambodia'), (b'CN', b'China'), (b'CY', b'Cyprus'), (b'GE', b'Georgia'), (b'HK', b'Hong Kong SAR China'), (b'IN', b'India'), (b'ID', b'Indonesia'), (b'IR', b'Iran'), (b'IQ', b'Iraq'), (b'IL', b'Israel'), (b'JP', b'Japan'), (b'JO', b'Jordan'), (b'KZ', b'Kazakhstan'), (b'KW', b'Kuwait'), (b'KG', b'Kyrgyzstan'), (b'LA', b'Laos'), (b'LB', b'Lebanon'), (b'MO', b'Macau SAR China'), (b'MY', b'Malaysia'), (b'MV', b'Maldives'), (b'MN', b'Mongolia'), (b'MM', b'Myanmar [Burma]'), (b'NP', b'Nepal'), (b'NT', b'Neutral Zone'), (b'KP', b'North Korea'), (b'OM', b'Oman'), (b'PK', b'Pakistan'), (b'PS', b'Palestinian Territories'), (b'YD', b"People's Democratic Republic of Yemen"), (b'PH', b'Philippines'), (b'QA', b'Qatar'), (b'SA', b'Saudi Arabia'), (b'SG', b'Singapore'), (b'KR', b'South Korea'), (b'LK', b'Sri Lanka'), (b'SY', b'Syria'), (b'TW', b'Taiwan'), (b'TJ', b'Tajikistan'), (b'TH', b'Thailand'), (b'TL', b'Timor-Leste'), (b'TR', b'Turkey'), (b'TU', b'Turkmenistan'), (b'AE', b'United Arab Emirates'), (b'UZ', b'Uzbekistan'), (b'VN', b'Vietnam'), (b'YE', b'Yemen'))), (b'Europe', ((b'AL', b'Albania'), (b'AD', b'Andorra'), (b'AT', b'Austria'), (b'BY', b'Belarus'), (b'BE', b'Belgium'), (b'BA', b'Bosnia and Herzegovina'), (b'BG', b'Bulgaria'), (b'HR', b'Croatia'), (b'CY', b'Cyprus'), (b'CZ', b'Czech Republic'), (b'DK', b'Denmark'), (b'DD', b'East Germany'), (b'EE', b'Estonia'), (b'FO', b'Faroe Islands'), (b'FI', b'Finland'), (b'FR', b'France'), (b'DE', b'Germany'), (b'GI', b'Gibraltar'), (b'GR', b'Greece'), (b'GG', b'Guernsey'), (b'HU', b'Hungary'), (b'IS', b'Iceland'), (b'IE', b'Ireland'), (b'IM', b'Isle of Man'), (b'IT', b'Italy'), (b'JE', b'Jersey'), (b'LV', b'Latvia'), (b'LI', b'Liechtenstein'), (b'LT', b'Lithuania'), (b'LU', b'Luxembourg'), (b'MK', b'Macedonia'), (b'MT', b'Malta'), (b'FX', b'Metropolitan France'), (b'MD', b'Moldova'), (b'MC', b'Monaco'), (b'ME', b'Montenegro'), (b'NL', b'Netherlands'), (b'NO', b'Norway'), (b'PL', b'Poland'), (b'PT', b'Portugal'), (b'RO', b'Romania'), (b'RU', b'Russia'), (b'SM', b'San Marino'), (b'RS', b'Serbia'), (b'CS', b'Serbia and Montenegro'), (b'SK', b'Slovakia'), (b'SI', b'Slovenia'), (b'ES', b'Spain'), (b'SJ', b'Svalbard and Jan Mayen'), (b'SE', b'Sweden'), (b'CH', b'Switzerland'), (b'UA', b'Ukraine'), (b'SU', b'Union of Soviet Socialist Republics'), (b'GB', b'United Kingdom'), (b'VA', b'Vatican City'), (b'AX', b'\xc3\x85land Islands'))), (b'Oceania', ((b'AS', b'American Samoa'), (b'AQ', b'Antarctica'), (b'AU', b'Australia'), (b'BV', b'Bouvet Island'), (b'IO', b'British Indian Ocean Territory'), (b'CX', b'Christmas Island'), (b'CC', b'Cocos [Keeling] Islands'), (b'CK', b'Cook Islands'), (b'FJ', b'Fiji'), (b'PF', b'French Polynesia'), (b'TF', b'French Southern Territories'), (b'GU', b'Guam'), (b'HM', b'Heard Island and McDonald Islands'), (b'KI', b'Kiribati'), (b'MH', b'Marshall Islands'), (b'FM', b'Micronesia'), (b'NR', b'Nauru'), (b'NC', b'New Caledonia'), (b'NZ', b'New Zealand'), (b'NU', b'Niue'), (b'NF', b'Norfolk Island'), (b'MP', b'Northern Mariana Islands'), (b'PW', b'Palau'), (b'PG', b'Papua New Guinea'), (b'PN', b'Pitcairn Islands'), (b'WS', b'Samoa'), (b'SB', b'Solomon Islands'), (b'GS', b'South Georgia and the South Sandwich Islands'), (b'TK', b'Tokelau'), (b'TO', b'Tonga'), (b'TV', b'Tuvalu'), (b'UM', b'U.S. Minor Outlying Islands'), (b'VU', b'Vanuatu'), (b'WF', b'Wallis and Futuna')))]),
        ),
    ]
