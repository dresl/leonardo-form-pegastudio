# encoding: utf-8
from leonardo.module.web.models import Widget
from leonardo.module.media.fields.image import ImageField
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime
from leonardo.module.media.fields.multistorage_file import MultiStorageFileField


CHOICES_BOOLEAN = (
    ('ano', 'Ano'),
    ('ne', 'Ne'),
)

CHOICES_TYPE_POZICE = (
    ('poz1', 'Zaměstnanec'),
    ('poz2', 'Student'),
)

CHOICES_COUNTRIES = (
    ('Africa' ,(
        ('DZ', 'Algeria'),
        ('AO', 'Angola'),
        ('BJ', 'Benin'),
        ('BW', 'Botswana'),
        ('BF', 'Burkina Faso'),
        ('BI', 'Burundi'),
        ('CM', 'Cameroon'),
        ('CV', 'Cape Verde'),
        ('CF', 'Central African Republic'),
        ('TD', 'Chad'),
        ('KM', 'Comoros'),
        ('CG', 'Congo - Brazzaville'),
        ('CD', 'Congo - Kinshasa'),
        ('CI', 'Côte d’Ivoire'),
        ('DJ', 'Djibouti'),
        ('EG', 'Egypt'),
        ('GQ', 'Equatorial Guinea'),
        ('ER', 'Eritrea'),
        ('ET', 'Ethiopia'),
        ('GA', 'Gabon'),
        ('GM', 'Gambia'),
        ('GH', 'Ghana'),
        ('GN', 'Guinea'),
        ('GW', 'Guinea-Bissau'),
        ('KE', 'Kenya'),
        ('LS', 'Lesotho'),
        ('LR', 'Liberia'),
        ('LY', 'Libya'),
        ('MG', 'Madagascar'),
        ('MW', 'Malawi'),
        ('ML', 'Mali'),
        ('MR', 'Mauritania'),
        ('MU', 'Mauritius'),
        ('YT', 'Mayotte'),
        ('MA', 'Morocco'),
        ('MZ', 'Mozambique'),
        ('NA', 'Namibia'),
        ('NE', 'Niger'),
        ('NG', 'Nigeria'),
        ('RW', 'Rwanda'),
        ('RE', 'Réunion'),
        ('SH', 'Saint Helena'),
        ('SN', 'Senegal'),
        ('SC', 'Seychelles'),
        ('SL', 'Sierra Leone'),
        ('SO', 'Somalia'),
        ('ZA', 'South Africa'),
        ('SD', 'Sudan'),
        ('SZ', 'Swaziland'),
        ('ST', 'São Tomé and Príncipe'),
        ('TZ', 'Tanzania'),
        ('TG', 'Togo'),
        ('TN', 'Tunisia'),
        ('UG', 'Uganda'),
        ('EH', 'Western Sahara'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabwe'),
     )
    ),
    ('Americas' ,(
        ('AI', 'Anguilla'),
        ('AG', 'Antigua and Barbuda'),
        ('AR', 'Argentina'),
        ('AW', 'Aruba'),
        ('BS', 'Bahamas'),
        ('BB', 'Barbados'),
        ('BZ', 'Belize'),
        ('BM', 'Bermuda'),
        ('BO', 'Bolivia'),
        ('BR', 'Brazil'),
        ('VG', 'British Virgin Islands'),
        ('CA', 'Canada'),
        ('KY', 'Cayman Islands'),
        ('CL', 'Chile'),
        ('CO', 'Colombia'),
        ('CR', 'Costa Rica'),
        ('CU', 'Cuba'),
        ('DM', 'Dominica'),
        ('DO', 'Dominican Republic'),
        ('EC', 'Ecuador'),
        ('SV', 'El Salvador'),
        ('FK', 'Falkland Islands'),
        ('GF', 'French Guiana'),
        ('GL', 'Greenland'),
        ('GD', 'Grenada'),
        ('GP', 'Guadeloupe'),
        ('GT', 'Guatemala'),
        ('GY', 'Guyana'),
        ('HT', 'Haiti'),
        ('HN', 'Honduras'),
        ('JM', 'Jamaica'),
        ('MQ', 'Martinique'),
        ('MX', 'Mexico'),
        ('MS', 'Montserrat'),
        ('AN', 'Netherlands Antilles'),
        ('NI', 'Nicaragua'),
        ('PA', 'Panama'),
        ('PY', 'Paraguay'),
        ('PE', 'Peru'),
        ('PR', 'Puerto Rico'),
        ('BL', 'Saint Barthélemy'),
        ('KN', 'Saint Kitts and Nevis'),
        ('LC', 'Saint Lucia'),
        ('MF', 'Saint Martin'),
        ('PM', 'Saint Pierre and Miquelon'),
        ('VC', 'Saint Vincent and the Grenadines'),
        ('SR', 'Suriname'),
        ('TT', 'Trinidad and Tobago'),
        ('TC', 'Turks and Caicos Islands'),
        ('VI', 'U.S. Virgin Islands'),
        ('US', 'United States'),
        ('UY', 'Uruguay'),
        ('VE', 'Venezuela'),
      )
    ),
    ('Asia' ,(
        ('AF', 'Afghanistan'),
        ('AM', 'Armenia'),
        ('AZ', 'Azerbaijan'),
        ('BH', 'Bahrain'),
        ('BD', 'Bangladesh'),
        ('BT', 'Bhutan'),
        ('BN', 'Brunei'),
        ('KH', 'Cambodia'),
        ('CN', 'China'),
        ('CY', 'Cyprus'),
        ('GE', 'Georgia'),
        ('HK', 'Hong Kong SAR China'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('IR', 'Iran'),
        ('IQ', 'Iraq'),
        ('IL', 'Israel'),
        ('JP', 'Japan'),
        ('JO', 'Jordan'),
        ('KZ', 'Kazakhstan'),
        ('KW', 'Kuwait'),
        ('KG', 'Kyrgyzstan'),
        ('LA', 'Laos'),
        ('LB', 'Lebanon'),
        ('MO', 'Macau SAR China'),
        ('MY', 'Malaysia'),
        ('MV', 'Maldives'),
        ('MN', 'Mongolia'),
        ('MM', 'Myanmar [Burma]'),
        ('NP', 'Nepal'),
        ('NT', 'Neutral Zone'),
        ('KP', 'North Korea'),
        ('OM', 'Oman'),
        ('PK', 'Pakistan'),
        ('PS', 'Palestinian Territories'),
        ('YD', 'People\'s Democratic Republic of Yemen'),
        ('PH', 'Philippines'),
        ('QA', 'Qatar'),
        ('SA', 'Saudi Arabia'),
        ('SG', 'Singapore'),
        ('KR', 'South Korea'),
        ('LK', 'Sri Lanka'),
        ('SY', 'Syria'),
        ('TW', 'Taiwan'),
        ('TJ', 'Tajikistan'),
        ('TH', 'Thailand'),
        ('TL', 'Timor-Leste'),
        ('TR', 'Turkey'),
        ('TU', 'Turkmenistan'),
        ('AE', 'United Arab Emirates'),
        ('UZ', 'Uzbekistan'),
        ('VN', 'Vietnam'),
        ('YE', 'Yemen'),
      )
    ),
    ('Europe' ,(
        ('AL', 'Albania'),
        ('AD', 'Andorra'),
        ('AT', 'Austria'),
        ('BY', 'Belarus'),
        ('BE', 'Belgium'),
        ('BA', 'Bosnia and Herzegovina'),
        ('BG', 'Bulgaria'),
        ('HR', 'Croatia'),
        ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'),
        ('DK', 'Denmark'),
        ('DD', 'East Germany'),
        ('EE', 'Estonia'),
        ('FO', 'Faroe Islands'),
        ('FI', 'Finland'),
        ('FR', 'France'),
        ('DE', 'Germany'),
        ('GI', 'Gibraltar'),
        ('GR', 'Greece'),
        ('GG', 'Guernsey'),
        ('HU', 'Hungary'),
        ('IS', 'Iceland'),
        ('IE', 'Ireland'),
        ('IM', 'Isle of Man'),
        ('IT', 'Italy'),
        ('JE', 'Jersey'),
        ('LV', 'Latvia'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lithuania'),
        ('LU', 'Luxembourg'),
        ('MK', 'Macedonia'),
        ('MT', 'Malta'),
        ('FX', 'Metropolitan France'),
        ('MD', 'Moldova'),
        ('MC', 'Monaco'),
        ('ME', 'Montenegro'),
        ('NL', 'Netherlands'),
        ('NO', 'Norway'),
        ('PL', 'Poland'),
        ('PT', 'Portugal'),
        ('RO', 'Romania'),
        ('RU', 'Russia'),
        ('SM', 'San Marino'),
        ('RS', 'Serbia'),
        ('CS', 'Serbia and Montenegro'),
        ('SK', 'Slovakia'),
        ('SI', 'Slovenia'),
        ('ES', 'Spain'),
        ('SJ', 'Svalbard and Jan Mayen'),
        ('SE', 'Sweden'),
        ('CH', 'Switzerland'),
        ('UA', 'Ukraine'),
        ('SU', 'Union of Soviet Socialist Republics'),
        ('GB', 'United Kingdom'),
        ('VA', 'Vatican City'),
        ('AX', 'Åland Islands'),
      )
    ),
    ('Oceania' ,(
        ('AS', 'American Samoa'),
        ('AQ', 'Antarctica'),
        ('AU', 'Australia'),
        ('BV', 'Bouvet Island'),
        ('IO', 'British Indian Ocean Territory'),
        ('CX', 'Christmas Island'),
        ('CC', 'Cocos [Keeling] Islands'),
        ('CK', 'Cook Islands'),
        ('FJ', 'Fiji'),
        ('PF', 'French Polynesia'),
        ('TF', 'French Southern Territories'),
        ('GU', 'Guam'),
        ('HM', 'Heard Island and McDonald Islands'),
        ('KI', 'Kiribati'),
        ('MH', 'Marshall Islands'),
        ('FM', 'Micronesia'),
        ('NR', 'Nauru'),
        ('NC', 'New Caledonia'),
        ('NZ', 'New Zealand'),
        ('NU', 'Niue'),
        ('NF', 'Norfolk Island'),
        ('MP', 'Northern Mariana Islands'),
        ('PW', 'Palau'),
        ('PG', 'Papua New Guinea'),
        ('PN', 'Pitcairn Islands'),
        ('WS', 'Samoa'),
        ('SB', 'Solomon Islands'),
        ('GS', 'South Georgia and the South Sandwich Islands'),
        ('TK', 'Tokelau'),
        ('TO', 'Tonga'),
        ('TV', 'Tuvalu'),
        ('UM', 'U.S. Minor Outlying Islands'),
        ('VU', 'Vanuatu'),
        ('WF', 'Wallis and Futuna'),
      )
    ),
)

CHOICES_TYPE_BUDOVA = (
   ('ha', 'HA'),
   ('hba', 'HB - A'),
   ('hbb', 'HB - B'),
   ('hbc', 'HB - C'),
   ('hbd', 'HB - D'),
   ('hce', 'HC - E'),
   ('hcf', 'HC - F'),
   ('hcg', 'HC - G'),
   ('ea', 'EA - Studentská 84'),
   ('eb', 'EB - Studentská 95'),
   ('da', 'DA - Studentská 95'),
   ('db', 'DB - Studentská 95'),
   ('dc', 'DC - Studentská 95'),
   ('dd', 'DD - Doubravice 41'),
   ('g', 'G - Stavařov 97'),
   ('pavil', 'Pavilon - Doubravice 41'),
   ('ca', 'CA - nám. Čs. legií 565'),
   ('cb', 'CB - nám. Čs. legií 565'),
   ('ua', 'UA - Studentská 519'),
   ('uk', 'UK - Studentská 519'),
   ('za', 'ZA - Průmyslová 395'),
   ('zb', 'ZB - Průmyslová 395'),
   ('zc', 'ZC - Průmyslová 395'),
   ('zd', 'ZD - Průmyslová 395'),
   ('ze', 'ZE - Průmyslová 395'),
   ('z', 'Z - Zámek 1'),
   ('r', 'R - Studentská 95'),
   ('jazcentrum', 'Jazykové centrum - Studentská 95'),
   ('ta', 'TA - Kunětická 92'),
   ('jinezprav', 'Jiné(napište do zprávy)...'),
)

CHOICES_TYPE_PATRA = (
   ('priz', 'Přízemí'),
   ('p1', '1.'),
   ('p2', '2.'),
   ('p3', '3.'),
   ('p4', '4.'),
   ('p5', '5.'),
   ('p6', '6.'),
   ('p7', '7.'),
   ('p8', '8.'),
   ('p9', '9.'),
   ('p10', '10.'),
   ('p11', '11.'),
   ('p12', '12.'),
   ('p13', '13.'),
)

CHOICES_TYPE_FAKULTY = (
   ('fcht', 'FCHT - Fakulta chemicko-technologická'),
   ('dfjp', 'DFJP - Dopravní fakulta Jana Pernera'),
   ('fes', 'FES - Fakulta ekonomicko-správní'),
   ('fei', 'FEI - Fakulta elektrotechniky a informatiky'),
   ('ff', 'FF - Fakulta filozofická'),
   ('fzs', 'FZS - Fakulta zdravotnických studií'),
   ('fr', 'FR - Fakulta restaurování'),
   ('rek', 'Rektorát')
)

CHOICES_TYPE_KATEDRY = (
    ('FCHT', (
        ('fchtkatanalchem', 'FCHT - Katedra analytické chemie'),
        ('fchtkatanortech', 'FCHT - Katedra anorganické technologie'),
        ('fchtkatbioved', 'FCHT - Katedra biologických a biochemických věd'),
        ('fchtkatfyzchem', 'FCHT - Katedra fyzikální chemie'),
        ('fchtkatobecanorg', 'FCHT - Katedra obecné a anorganické chemie'),
        ('fchtkatpolfot', 'FCHT - Katedra polygrafie a fotofyziky'),
        ('fchtkatekomanchemport', 'FCHT - Katedra ekonomiky a managementu chem. a potr. prům.'),
        ('fchtustenermat', 'FCHT - Ústav energetických materiálů'),
        ('fchtustenvchiing', 'FCHT - Ústav enviromentálního a chemického inženýrství'),
        ('fchtustchemtechlat', 'FCHT - Ústav chemie a technologie makromolekulárních látek'),
        ('fchtustorgchemtech', 'FCHT - Ústav organické chemie a technologie'),
        ('fchtkataplfyzmat', 'FCHT - Ústav aplikované fyziky a matematiky'),
        ('fchtkatstudod', 'FCHT - Studijní oddělení'),
        ('fchtkatjine', 'FCHT - Jiné(napište do zprávy)...'),
      )
    ),
    ('DFJP', (
        ('dfjpkatinfdop', 'DFJP - Katedra informatiky v dopravě'),
        ('dfjpkatprosdia', 'DFJP - Katedra dopravních prostředků a diagnostiky'),
        ('dfjpkatdoprstav', 'DFJP - Katedra dopravního stavitelství'),
        ('dfjpkattechrizstav', 'DFJP - Katedra technologie a řízení dopravy'),
        ('dfjpkatdoprmang', 'DFJP - Katedra dopravního managementu, marketingu a logistiky'),
        ('dfjpkatelekzab', 'DFJP - Katedra elektrotechniky, elek. a zabez. tech. v dopravě'),
        ('dfjpkatmechmatstroj', 'DFJP - Katedra mechaniky, materiálů a části strojů'),
        ('dfjpkatstudod', 'DFJP - Studijní oddělení'),
        ('dfjpkatjine', 'DFJP - Jiné(napište do zprávy)...'),
      )
    ),
    ('FES', (
        ('fesustavekoved', 'FES - Ústav ekonomických věd'),
        ('fesustavpodnekonmang', 'FES - Ústav podnikové ekonomiky a managementu'),
        ('fesustavmatkvant', 'FES - Ústav matematiky a kvantitativních metod'),
        ('fesustavsystinginf', 'FES - Ústav systémového inženýrství a informatiky'),
        ('fesustavspravsocved', 'FES - Ústav správních a sociálních věd'),
        ('fesustavregbezpved', 'FES - Ústav regionálních a bezpečnostních věd'),
        ('fesustavstudod', 'FES - Studijní oddělení'),
        ('fesustavjine', 'FES - Jiné(napište do zprávy)...'),
      )
    ),
    ('FEI', (
        ('feikatlek', 'FEI - Katedra elektrotechniky'),
        ('feikatinftech', 'FEI - Katedra informačních technologií'),
        ('feikatmatfyz', 'FEI - Katedra matematiky a fyziky'),
        ('feikatrizproc', 'FEI - Katedra řízení procesů'),
        ('feikatsofttech', 'FEI - Katedra softwarových technologií'),
        ('feikatstudod', 'FEI - Studijní oddělení'),
        ('feikatjine', 'FEI - Jiné(napište do zprávy)...'),
      )
    ),
    ('FF', (
        ('ffkatangamer', 'FF - Katedra anglistiky a amerikanistiky'),
        ('ffkatcizjaz', 'FF - Katedra cizích jazyků'),
        ('ffkatfil', 'FF - Katedra filosofie'),
        ('ffkatlitkultslav', 'FF - Katedra literární kultury a slavistiky'),
        ('ffkatrel', 'FF - Katedra religionistiky'),
        ('ffkatsockulantro', 'FF - Katedra sociální a kulturní antropologie'),
        ('ffkatvych', 'FF - Katedra věd o výchově'),
        ('ffkathistved', 'FF - Ústav historických věd'),
        ('ffkatstudod', 'FF - Studijní oddělení'),
        ('ffkatjine', 'FF - Jiné(napište do zprávy)...'),
      )
    ),
    ('FZS', (
        ('fzskatoset', 'FZS - Katedra ošetřovatelství'),
        ('fzskatporodaszdr', 'FZS - Katedra porodní asistence a zdravotně sociální práce'),
        ('fzskatklinobr', 'FZS - Katedra klinických oborů'),
        ('fzskatinfomang', 'FZS - Katedra informatiky, managementu a radiologie'),
        ('fzskatstudod', 'FZS - Studijní oddělení'),
        ('fzskatjine', 'FZS - Jiné(napište do zprávy)...'),
      )
    ),
    ('FR', (  
        ('fratelierrestmalb', 'FR - Ateliér restaurování nástěnné malby a sgrafita'),
        ('fratelierrestkamen', 'FR - Ateliér restaurování kamene'),
        ('fratelierrestpapir', 'FR - Ateliér restaurování papíru, knižní vazby a dokumentů'),
        ('fratelierumeldel', 'FR - Ateliér restaurování uměleckých děl na papíru a souv. materiálech'),
        ('frateliervytvarprip', 'FR - Ateliér výtvarné přípravy'),
        ('fratelierhumved', 'FR - Katedra humanitních věd'),
        ('fratelierchemtech', 'FR - Katedra chemické technologie'),
        ('frateliercentrum', 'FR - Centrum pro restaurování a památkovou péči'),
        ('fratelierstudod', 'FR - Studijní oddělení'),
        ('fratelierjine', 'FR - Jiné(napište do zprávy)...'),
      )
    ),
    ('Další', (
        ('upceknih', 'Univerzitní knihovna'),
        ('rektor', 'Rektorát'),
        ('jazykcentrum', 'Jazykové centrum'),
        ('katsport', 'Katedra tělovýchovy a sportu'),
      )
    ),
)

CHOICES_TYPE_MATERIALY = (
    ('Nejčastěji používané', (
        ('bbsecon', 'BBS economy 115 gsm'),
        ('bbsprem', 'BBS premium 120 gsm'),
        ('clv', ' CLV150 gsm'),
        ('ofset', 'Ofset 80 gsm'),
        ('post135', 'Poster papír polomat 135 gsm'),
        ('post200', 'Poster papír polomat 200 gsm'),
        ('fotopaplesk', 'Fotopapír lesk 200 gsm'),
        ('fotopapsatin', 'Fotopapír satin 200 gsm'),
        ('sammon', 'Samolepka monochromatická'),
        ('fluor', 'Fluorescentní papír 80 gsm'),
      )
    ),
    ('Látky', (
        ('nikos', 'NIKOS'),
        ('jitu', 'JITU'),
        ('whisper', 'WHISPER '),
        ('vlaj', 'VLAJKOVINA'),
        ('dres', 'DRESOVINA'),
        ('polysub', 'POLYSUB'),
        ('miko', 'MIKO'),
        ('disco', 'DISCOVERY'),
        ('sonic', 'SONIC'),
        ('blockout', 'BLOCKOUT'),
        ('dimout', 'DIMOUT'),
        ('viva', 'VIVA'),
        ('airtex', 'AIRTEX'),
        ('chcividet', 'CHCI VYDĚT VZORNÍK LÁTEK'),
      )
    ),
    ('Samolepící tiskové materiály', (
        ('monlesk', 'Monomerická samolepka lesklá'),
        ('monmat', 'Monomerická samolepka matná'),
        ('montrans', 'Monomerická samolepka transparentní'),
        ('monlamlesk', 'Monomerická samolepka+ laminace lesklá'),
        ('monlammat', 'Monomerická samolepka+ laminace matná'),
        ('monlamleskopos', 'Monomerická samolepka+ laminace lesklá+ OPOS'),
        ('monlammatopos', 'Monomerická samolepka+ laminace matná+ OPOS'),
        ('monstruk', 'Monomerická samolepka+ strukturovaná podl. lam.'),
        ('monstrukopos', 'Monomerická samolepka+ strukturovaná podl. lam.+ OPOS'),
        ('pollesk', 'Polyomerická samolepka lesklá'),
        ('polleskopos', 'Polyomerická samolepka lesklá+ OPOS'),
        ('polstruk', 'Polyomerická samolepka+ strukturovaná podl. lam.'),
        ('polstrukopos', 'Polyomerická samolepka+ strukturovaná podl. lam.+ OPOS'),
        ('litlesk', 'Litá samolepka lesklá'),
        ('lit', ' Litásamolepka+ laminace lesklá'),
        ('litlam', 'Litá samolepka+ laminace lesk+ OPOS'),
        ('walllesk', 'WallArt samolepka lesklá'),
        ('wallmat', 'WallArt samolepka matná '),
        ('transsam', 'Trnaslucentní polymerická samolepka'),
        ('translam', 'Trnaslucentní polymerická samolepka+ laminace leská'),
        ('piskarlon', 'Písková polymerická samolepka Arlon 5400'),
        ('piskarlonlam', 'Písková polymerická samolepka Arlon 5400+ laminace leská'),
        ('owvlesk', 'OWV samolepka krátkodobá bez atestu lesklá'),
        ('ovwlesklam', 'OWV samolepka krátkodobá bez atestu lesklá+ laminace lekslá'),
        ('owvdloulesk', 'OWV samolepka dlouhodobá bez atestu lesklá'),
        ('owvdloulam', 'OWV samolepka dlouhodobá bez atestu lesklá+ laminace lesklá'),
        ('owvatestlesk', 'OWV samolepka s atestem lesklá'),
        ('owvatestlesklam', 'OWV samolepka s atestem lesklá+ laminace lesklá'),
      )
    ),
    ('Bannery', (
        ('lamban', 'Laminátový banner 450 gsm'),
        ('lambanóka', 'Laminátový banner 450 gsm+ oka'),
        ('lambanokahran', 'Laminátový banner 450 gsm+ oka+ zpevněné hrany'),
        ('litban', 'Litý banner 510 gsm'),
        ('litbanoka', 'Litý banner 510 gsm+ oka+ zpevněné hrany'),
        ('meshban', 'Mesh banner 400gsm'),
        ('meshbanoka', 'Mesh banner 400gsm+ oka'),
        ('meskokahran', 'Mesh banner 400gsm+ oka+ zpevněné hrany'),
        ('blban', 'Blockout banner 510 gsm (jednostranný tisk)'),
        ('blbanoka', 'Blockout banner 510 gsm (jednostranný tisk)+ oka '),
        ('blbanokahr', 'Blockout banner 510 gsm (jednostr. tisk)+ oka+ zpev. hr.'),
        ('blbanoboustr', 'Blockout banner 510 gsm (oboustranný tisk)'),
        ('blban', 'Blockout banner 510 gsm (oboustranný tisk)'),
      )
    ),
    ('Prezentační_stojany', (
        ('rolv150', 'ROLLUPY výška do 150 cm'),
        ('rolv180', 'ROLLUPY výška do 180 cm'),
        ('rolv200', 'ROLLUPY výška do 200 cm'),
        ('rolp200', 'ROLLUPY výška přes 200 cm'),
        ('rols100', 'ROLLUPY šířka standart 100cm'),
        ('rols150', 'ROLLUPY šířka do 150cm'),
        ('rols200', 'ROLLUPY šířka do 200cm'),
        ('rols300', 'ROLLUPY šířka do 300cm'),
        ('rols400', 'ROLLUPY šířka do 400cm'),
        ('roln400', 'ROLLUPY šířka nad 400cm'),
        ('vlajky', 'VLAJKY, VLAJKOVÉ SYSTÉMY'),
        ('acka', 'ÁČKA'),
        ('stojl', 'STOJAN L-KO'),
        ('stojk', 'STOJAN X-KO'),
        ('prezsten', 'PREZENTAČNÍ STĚNY'),
      )
    ),
)

CHOICES_TYPE_LAMINACE = (
   ('ne', 'NE'),
   ('lesk', 'Lesklá'),
   ('mat', 'Matná'),
   ('struv', 'Strukturovaná v UV'),
   ('strbezuv', 'Strukturovaná bez UV'),
   ('oboulam', 'Oboustranná lepicí laminace'),
   ('podllam', 'Podlahová fotolaminace'),
)

CHOICES_TYPE_PREPRAVA = (
   ('osobni', 'Osobní (auto, vlak)'),
   ('letecka', 'Letecká'),
)

CHOICES_TYPE_PREZENTACE = (
   ('interier', 'Interiér'),
   ('exterier', 'Exteriér'),
)


class PegastudioOrders(models.Model):

    jmeno = models.CharField(
        max_length=255, verbose_name=u"Jméno", default='')
    pozice = models.CharField(
        verbose_name=u"Pozice", choices=CHOICES_TYPE_POZICE, max_length=255)
    prijmeni = models.CharField(
        max_length=255, verbose_name=u"Příjmení", default='')
    fakulta = models.CharField(
        verbose_name=u"Fakulta", choices=CHOICES_TYPE_FAKULTY, max_length=255)
    telefon = models.CharField(
        verbose_name=u"Telefon (ve tvaru: +420 123 456 789)", max_length=100)
    katedra = models.CharField(
        verbose_name=u"Katedra", choices=CHOICES_TYPE_KATEDRY, max_length=255)
    email = models.EmailField(
        verbose_name=u"E-mail", default='')
    budova = models.CharField(
        verbose_name=u"Budova", choices=CHOICES_TYPE_BUDOVA, max_length=255)
    std = models.CharField(
        max_length=255, verbose_name=u"st kód", default='')
    patro = models.CharField(
        verbose_name=u"Patro", choices=CHOICES_TYPE_PATRA, max_length=255)
    fakturacni_udaje = models.CharField(
        verbose_name=u"Fakturační údaje", default="Univerzita Pardubice, Studentská 95, 532 10 Pardubice", max_length=255)
    ic = models.CharField(
        verbose_name=u"IČ", default="00216275", max_length=255)
    dic = models.CharField(
        verbose_name=u"DIČ", default="CZ00216275", max_length=255)
    cislo_uctu = models.CharField(
        verbose_name=u"Číslo účtu", default="37030561/0100", max_length=255)
    zprava = models.TextField(
        verbose_name=u"Zpráva", default='', blank=True)
    porada_material = models.CharField(
        verbose_name=u"Chcete poradit s výběrem materiálu?", choices=CHOICES_BOOLEAN, max_length=255)
    porada_poster = models.CharField(
        verbose_name=u"Chcete graficky zpracovat poster?", choices=CHOICES_BOOLEAN, max_length=255)
    prezentace = models.CharField(
        verbose_name=u"Prezentace", choices=CHOICES_TYPE_PREZENTACE, max_length=255)
    zeme = models.CharField(
        verbose_name=u"Země", choices=CHOICES_COUNTRIES, default='CZ', max_length=255)
    preprava = models.CharField(
        verbose_name=u"Přeprava", choices=CHOICES_TYPE_PREPRAVA, max_length=255)
    pub_date = models.DateTimeField(u'Datum objednávky', auto_now_add=True)

    def __unicode__(self):
        return self.jmeno

    class Meta:
        ordering = ['jmeno', ]
        verbose_name = u'Položka'
        verbose_name_plural = u'Položky'


class PegastudioProducts(models.Model):

    order = models.ForeignKey(PegastudioOrders,
        verbose_name=u"Objednávka", related_name="orderproduct_set")
    pocet_kusu = models.PositiveIntegerField(
        verbose_name=u"Počet kusů", default=1)
    material = models.CharField(
        verbose_name=u"Materiál", choices=CHOICES_TYPE_MATERIALY, max_length=255)
    laminace = models.CharField(
        verbose_name=u"Laminace", choices=CHOICES_TYPE_LAMINACE, max_length=255)
    file = models.FileField(
        u'Soubor', upload_to='documents/%Y/%m/%d/')

    def __unicode__(self):
        return self.material

    class Meta:
        ordering = ['material', ]
        verbose_name = u'Produkt'
        verbose_name_plural = u'Produkty'

