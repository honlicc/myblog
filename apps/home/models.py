from django.db import models
from db.base_model import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class IndexBanner(BaseModel):
    type = models.ForeignKey('Blog', verbose_name='文章')
    image = models.ImageField(upload_to='banner', blank=True, verbose_name='图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'index_banner'
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name



class BlogType(BaseModel):
    '''blog类型模型类'''
    name = models.CharField(max_length=20, verbose_name='类型名称')

    class Meta:
        db_table = 'blog_type'
        verbose_name = '博客类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogTag(BaseModel):
    '''标签模型类'''

    type = models.ForeignKey('BlogType', verbose_name='博客类型')
    name = models.CharField(max_length=20, verbose_name='名称')
    image= models.ImageField(upload_to='tag', blank=True, verbose_name='图片')

    class Meta:
        db_table = 'blog_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogTable(BaseModel):
    '''目录列表'''
    tag = models.ForeignKey('BlogTag', verbose_name='目录')
    name = models.CharField(max_length=20, verbose_name='名称')

    class Meta:
        db_table = 'blog_table'
        verbose_name = '目录列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(BaseModel):
    '''blog模型类'''
    status_choices = (
        (0, '下线'),
        (1, '上线'),
        (2, '草稿'),
    )
    user = models.ForeignKey('user.UserInfo', verbose_name='作者')
    type = models.ForeignKey('BlogType', verbose_name='类型')
    tag = models.ForeignKey('BlogTag', null=True,blank=True,verbose_name='标签')
    table = models.ForeignKey('BlogTable', null=True,blank=True, verbose_name='目录')
    title = models.CharField(max_length=20, verbose_name='标题')
    image = models.ImageField(upload_to='banner',  blank=True, verbose_name='图片')
    read=models.IntegerField(default=0,verbose_name='阅读数')
    # 富文本类型:带有格式的文本
    detail = RichTextUploadingField(default='', verbose_name='详情')
    recommend = models.IntegerField(default=0,verbose_name='推荐')
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='状态')

    class Meta:
        db_table = 'blog'
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comments(BaseModel):
    status_choices = (
        (0, '删除'),
        (1, '展示'),
    )
    user = models.ForeignKey('user.User', verbose_name='评论人')
    blog = models.ForeignKey('Blog', verbose_name='文章')
    detail = RichTextUploadingField(default='', verbose_name='详情')
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='状态')

    class Meta:
        db_table = 'Comments'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.blog.title
