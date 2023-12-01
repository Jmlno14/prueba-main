from django.db import models

class countrylanguage(models.Model):
    nombrecountrylanguage = models.CharField('nombrecountrylanguage', max_length=35)
    id_country = models.CharField('nombreCountry', max_length=3, unique=True, null=False)
    countrylanguage = models.CharField('countrylanguage', max_length=30, null=False)
    isOfficial = models.BooleanField('officialanguage', null=False)
    percentage = models.DecimalField('languagePercentaje', max_digits=4, decimal_places=1, null=False)  # Corregidos max_digits y decimal_places
    siglacountrylanguage = models.CharField('siglacountrylanguage', max_length=2, unique=True)
    activocountrylanguage = models.BooleanField('active', default=False)
    search_fields = ('nombrecountrylanguage', 'siglacountrylanguage',)
    list_filter = ('nombrecountrylanguage',)

    class Meta:
        verbose_name = 'Nombre countrylanguage'
        verbose_name_plural = 'Nombres countrylanguages'
        ordering = ['nombrecountrylanguage']
        unique_together = ('nombrecountrylanguage', 'siglacountrylanguage')

    def __str__(self):
        return self.nombrecountrylanguage + ' - ' + self.siglacountrylanguage + str(self.id)
