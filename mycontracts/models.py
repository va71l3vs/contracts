from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

DEPARTMENTS = ((1,"Департамент информационных технологий и автоматизации"),(2,"Финансово-экономический департамент"),
               (3,"Департамент труда"),(4,"Департамент занятости"))
TYPE = ((1,"Запрос котировок"),(2,"Аукцион"),(3,"Закупка у единственного поставщика"))

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Класс департамента определяет откуда пришел контракт (департамент, отдел, исполнитель,статус контракта(черновик или нет))
class Contracts(models.Model):
    object_name = models.CharField(max_length=300)
    nmck = models.FloatField()
    count_goods = models.IntegerField()
    tip_contracts = models.IntegerField(choices=TYPE)
    tz = models.TextField()
    contracts_returns = models.DateTimeField()#дата возврата контракта
    class Meta:
        ordering = ["object_name","nmck"]
        verbose_name = "Контракты"
        verbose_name_plural = "Название контракта"

    def __str__(self):
        return self.object_name


class Departments(models.Model):
    common_name = models.IntegerField(choices=DEPARTMENTS,default=1,db_index=True)
    user = models.CharField(max_length=30)
    worker = models.CharField(max_length=40)
    status = models.BooleanField(bool)

    class Meta:
        ordering = ["common_name"]
        verbose_name = "Департамент"
        verbose_name_plural = "Наименование департамента"

class Revisor(models.Model):
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Сотрудник отдела закупок"
        verbose_name_plural = "ФИО сотудника отдела закупок"


class Published_contracts(models.Model):
    date_published = models.DateTimeField(blank=True, null=True)
    status_rebuild = models.BooleanField(bool)
    contracts = models.ForeignKey(Contracts,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.contracts.object_name

    class Meta:
        ordering = ["date_published"]
        verbose_name = "Дата публикации контракта в ЕСИА"
        verbose_name_plural = "Контракт опубликован"



