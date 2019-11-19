from django.db import models
from db.base_model import BaseModel


# Create your models here.
class Tag(BaseModel):
    name = models.CharField(max_length=20, verbose_name='标签')

    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Photo(BaseModel):
    tag=models.ForeignKey('Tag',verbose_name='标签')
    name=models.CharField(max_length=100, verbose_name='名称')
    photo=models.ImageField(upload_to='photo', blank=True, verbose_name='照片')
    read=models.SmallIntegerField(default=0,verbose_name='喜欢')

    class Meta:
        db_table='photo'
        verbose_name='照片'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name