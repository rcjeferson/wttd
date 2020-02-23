from django.db import models
from django.shortcuts import resolve_url as r
from eventex.core.managers import KindQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KIND = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone'),
    )

    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE,
                                verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KIND)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value


class Activity(models.Model):
    title = models.CharField('titulo', max_length=255)
    start = models.TimeField('início', null=True, blank=True)
    description = models.TextField('descrição', blank=True)

    speakers = models.ManyToManyField('Speaker', blank=True,
                                      verbose_name='palestrantes')

    objects = PeriodManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Talk(Activity):
    class Meta:
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title
