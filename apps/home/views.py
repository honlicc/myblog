from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from user.models import User
from home.models import BlogTag, BlogTable, IndexBanner, Blog, Comments
from django.http import JsonResponse, HttpResponse
from django.db.models import Q


# Create your views here.

class HomeView(View):
    def get(self, request):
        # 获取轮播图
        banners = IndexBanner.objects.all().order_by('index')

        # 获取所有文章
        blogs = Blog.objects.all().order_by('-create_time')
        blog_top = Blog.objects.all().filter(~Q(table=None)).order_by('-create_time')[:2]


        # 推荐
        blog_tj = Blog.objects.all().order_by('-create_time')[:4]

        # 点击，按阅读数排序
        blog_read = Blog.objects.all().order_by('-read')[:4]

        content = {
            'banners': banners,
            'blogs': blogs,
            'blog_top': blog_top,
            'blog_tj': blog_tj,
            'blog_read': blog_read,
        }

        return render(request, 'index.html', content)


class RecordListView(View):
    def get(self, request):
        # 获取所有文章
        blogs = Blog.objects.all()

        # 所有日记类文章
        blog_rj = []
        for blog in blogs:
            if blog.tag.type.id == 1:
                blog.detail = blog.detail[:400]
                blog_rj.append(blog)

        # 推荐
        blog_tj = Blog.objects.all().order_by('-create_time')[:4]

        # 点击，按阅读数排序
        blog_read = Blog.objects.all().order_by('-read')[:4]

        content = {
            'blog_rj': blog_rj,
            'blog_tj': blog_tj,
            'blog_read': blog_read,
        }

        return render(request, 'recordlist.html', content)


class CourseListView(View):
    def get(self, request):
        # 获取所有文章
        blogs = Blog.objects.all()

        # 所有教程类文章
        blog_rj = []
        for blog in blogs:
            if blog.tag.type.id == 2:
                blog.detail = blog.detail[:400]
                blog_rj.append(blog)

        # 推荐
        blog_tj = Blog.objects.all().order_by('-create_time')[:4]

        # 点击，按阅读数排序
        blog_read = Blog.objects.all().order_by('-read')[:4]

        content = {
            'blog_rj': blog_rj,
            'blog_tj': blog_tj,
            'blog_read': blog_read,
        }
        return render(request, 'courselist.html', content)


# /info/blog_id
class InfoView(View):
    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return redirect(reverse('home:index'))

        # 推荐
        blog_tj = Blog.objects.all().order_by('-create_time')[:4]

        # 点击，按阅读数排序
        blog_read = Blog.objects.all().order_by('-read')[:4]

        blog.read += 1
        blog.save()

        comment = Comments.objects.filter(blog=blog_id)

        content = {
            'blog': blog,
            'comment': comment,
            'blog_tj': blog_tj,
            'blog_read': blog_read,
        }

        return render(request, 'info.html', content)


class ContentView(View):
    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return redirect(reverse('home:index'))

        tables = BlogTable.objects.filter(tag_id=blog.table.tag.id)

        for table in tables:
            blogs = Blog.objects.filter(table=table).filter(status=1)
            table.blogs=blogs


        content = {
            'tables': tables,
            'blog': blog,

        }
        return render(request, 'content.html', content)


class ReleaseView(View):
    def get(self, request):
        return redirect(reverse('home:index'))
