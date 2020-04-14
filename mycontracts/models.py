from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone


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
class Departments(models.Model):
    common_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    worker = models.CharField(max_length=40)
    status = models.BooleanField(bool)
    contracts_returns = models.DateTimeField()#дата возврата контракта
    #добавить в модель возможность изменения цвета на календаре, для тех контрактов у которых истек срок рассмотрения
