from django.db import models
from django.utils import timezone

# Create your models here.
class Region(models.Model):
    title = models.CharField("Название", max_length=100)
    has_division = models.BooleanField("Есть подразделение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

class RspsDiv(models.Model):
    title = models.CharField("Название", max_length=200)
    region = models.ForeignKey(Region, verbose_name = "Регион")
    telephone = models.CharField("Телефон", max_length=50)
    email = models.EmailField()
    created_date = models.DateTimeField("Дата создания", blank=True, null=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

class RspsMember(models.Model):
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50)
    job = models.CharField("Место работы", max_length=100)
    is_a_leader = models.BooleanField("Руководитель")
    rsps_div = models.ForeignKey(RspsDiv, verbose_name="Подразделение")
    education = models.CharField("Образование", max_length=200, blank=True, null=True)
    created_date = models.DateField("Дата принятия", blank=True, null=True)

    def __str__(self):
        return u'%s %s %s' %(self.first_name, self.middle_name, self.last_name)
    class Meta:
        verbose_name = "Член РСПС"
        verbose_name_plural = "Члены РСПС"

class RspsEvents(models.Model):
    title = models.CharField("Название события", max_length=100)
    place = models.CharField("Место проведения", max_length=100)
    date = models.DateField("Дата", max_length=100)
    rsps_div = models.ForeignKey(RspsDiv, verbose_name = 'Подразделение')
    body = models.TextField("Описание", default="Описание события")
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

