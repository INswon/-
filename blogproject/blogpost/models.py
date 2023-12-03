from django.db import models

# Create your models here.

""" カテゴリーモデル """
class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name


class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
                      Category, verbose_name='カテゴリー',
                      on_delete=models.PROTECT
                      )

    def __str__(self):
        return self.title



