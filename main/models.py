from django.db import models

class zakazi(models.Model):
    zazchik = models.CharField('Как к вам можно обращаться',max_length= 100 )
    zakaz =models.TextField('Опишите вид работ которую вам необходимо сделать')
    def __str__(self):
        return self.zazchik
    class Meta:
        verbose_name ='Отзыв'
        verbose_name_plural = 'Отзывы'
class articles(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
