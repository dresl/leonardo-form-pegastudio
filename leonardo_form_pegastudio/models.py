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


class PegastudioOrders(models.Model):

    jmeno = models.CharField(
        max_length=255, verbose_name=u"Jméno", blank=True, default='')
    pozice = models.CharField(
        verbose_name=u"Pozice", choices=CHOICES_TYPE_POZICE, max_length=255, blank=True)
    prijmeni = models.CharField(
        max_length=255, verbose_name=u"Příjmení", default='')
    fakulta = models.CharField(
        verbose_name=u"Fakulta", choices=CHOICES_TYPE_POZICE, max_length=255, blank=True)
    telefon = models.PositiveIntegerField(
        verbose_name=u"Telefon", blank=True, default=None)
    katedra = models.CharField(
        verbose_name=u"Katedra", choices=CHOICES_TYPE_POZICE, max_length=255, blank=True)
    email = models.EmailField(
        verbose_name=u"E-mail", blank=True, default='')
    budova = models.CharField(
        verbose_name=u"Budova", choices=CHOICES_TYPE_POZICE, max_length=255, blank=True)
    std = models.CharField(
        max_length=255, blank=True, verbose_name=u"st kód", default='')
    patro = models.CharField(
        verbose_name=u"Patro", choices=CHOICES_TYPE_POZICE, max_length=255, blank=True)
    fakturacni_udaje = models.CharField(
        verbose_name=u"Fakturační údaje", default="Univerzita Pardubice, Studentská 95, Pardubice 532 10", max_length=255, blank=True)
    ic = models.CharField(
        verbose_name=u"IČ", default="00216275", max_length=255, blank=True)
    dic = models.CharField(
        verbose_name=u"DIČ", default="CZ00216275", max_length=255, blank=True)
    cislo_uctu = models.CharField(
        verbose_name=u"Číslo účtu", default="37030561/0100", max_length=255, blank=True)
    zprava = models.TextField(
        verbose_name=u"Zpráva", default='', blank=True)
    porada_material = models.CharField(
        verbose_name=u"Chcete poradit s výběrem materiálu?", choices=CHOICES_BOOLEAN, max_length=255, blank=True)
    porada_poster = models.CharField(
        verbose_name=u"Chcete graficky zpracovat poster?", choices=CHOICES_BOOLEAN, max_length=255, blank=True)
    prezentace = models.CharField(
        verbose_name=u"Prezentace", choices=CHOICES_TYPE_POZICE, max_length=255, blank=True)
    zeme = models.CharField(
        verbose_name=u"Země", choices=CHOICES_TYPE_POZICE, max_length=255, blank=True)
    preprava = models.CharField(
        verbose_name=u"Přeprava", choices=CHOICES_TYPE_POZICE, max_length=255, blank=True)
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
        verbose_name=u"Materiál", choices=CHOICES_BOOLEAN, max_length=255)
    laminace = models.CharField(
        verbose_name=u"Laminace", choices=CHOICES_BOOLEAN, max_length=255)
    file = models.FileField(
        u'file', upload_to='documents', default="/static/bp.pdf", max_length=255)

    def __unicode__(self):
        return self.material

    class Meta:
        ordering = ['material', ]
        verbose_name = u'Produkt'
        verbose_name_plural = u'Produkty'

