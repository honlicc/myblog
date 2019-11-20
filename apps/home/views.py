from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from user.models import User
from home.models import BlogTag, BlogTable, IndexBanner, Blog, Comments
from django.http import JsonResponse, HttpResponse
from utils.mixin import LoginRequiredMixin


# Create your views here.

class HomeView(View):
    def get(self, request):
        # 获取轮播图
        banners = IndexBanner.objects.all().order_by('index')


        # 获取所有文章
        blogs = Blog.objects.all().order_by('-create_time')

        blog_top = Blog.objects.filter(type=1).order_by('-create_time')[:2]

        # 推荐
        blog_recommend = Blog.objects.all().order_by('-recommend')[:4]

        # 点击，按阅读数排序
        blog_read = Blog.objects.all().order_by('-read')[:4]

        content = {
            'banners': banners,
            'blogs': blogs,
            'blog_top': blog_top,
            'blog_recommend': blog_recommend,
            'blog_read': blog_read,
        }

        return render(request, 'index.html', content)


class RecordListView(View):
    def get(self, request):
        # 获取所有文章
        blogs = Blog.objects.all().order_by('-create_time')
        # 所有日记类文章
        blog_rj = Blog.objects.filter(type=2).order_by('-create_time')

        # 推荐
        blog_recommend = Blog.objects.all().order_by('-create_time')[:4]

        # 点击，按阅读数排序
        blog_read = Blog.objects.all().order_by('-read')[:4]

        content = {
            'blog_rj': blog_rj,
            'blog_recommend': blog_recommend,
            'blog_read': blog_read,
            'blogs': blogs,
        }

        return render(request, 'recordlist.html', content)


class CourseListView(View):
    def get(self, request):
        # 所有教程类文章
        blog_document = Blog.objects.filter(type=1).order_by('-create_time')

        # 推荐
        blog_recommend = Blog.objects.all().order_by('-create_time')[:4]

        # 点击，按阅读数排序
        blog_read = Blog.objects.all().order_by('-read')[:4]

        content = {
            'blog_document': blog_document,
            'blog_recommend': blog_recommend,
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
        blog_recommend = Blog.objects.all().order_by('-create_time')[:4]

        # 点击，按阅读数排序
        blog_read = Blog.objects.all().order_by('-read')[:4]
        blog.read += 1
        blog.save()

        comments = Comments.objects.filter(blog=blog_id, status=1)
        comme_len = len(comments)

        content = {
            'blog': blog,
            'comments': comments,
            'blog_recommend': blog_recommend,
            'blog_read': blog_read,
            'comme_len': comme_len,
        }

        return render(request, 'info.html', content)


class ContentView(View):
    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return redirect(reverse('home:index'))

        tables = BlogTable.objects.filter(tag_id=blog.tag)

        for table in tables:
            blogs = Blog.objects.filter(table=table).filter(status=1)
            table.blogs = blogs



        content = {
            'tables': tables,
            'blog': blog,

        }
        return render(request, 'content.html', content)


class ReleaseView(View):
    def get(self, request):
        return redirect(reverse('home:index'))


# comment/blog_id
class CommentView(View):
    def post(self, request):
        user = request.user
        blog_id = int(request.POST.get('blog_id'))
        detail = request.POST.get('comment')
        try:
            user = User.objects.get(id=user.id)
        except User.DoesNotExist:
            return JsonResponse({"res": 0, "msg": "用户信息异常"})

        try:
            blog = Blog.objects.get(id=blog_id)
        except User.DoesNotExist:
            return JsonResponse({"res": 3, "msg": "文章信息异常"})

        if user.is_authenticated():
            comments = Comments.objects.create(user=user, blog=blog, detail=detail)

            return JsonResponse({"res": 1, "msg": "评论成功"})
        else:
            return JsonResponse({"res": 2, "msg": "请先登录"})


class TimeView(View):
    def get(self, request):
        # 获取所有文章
        blogs = Blog.objects.filter(status=1).order_by('-create_time')

        return render(request, 'time.html', {"blogs": blogs})

class GbookView(View):
    def get(self, request):

        return render(request, 'gbook.html')
