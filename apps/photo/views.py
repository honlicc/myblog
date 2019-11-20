from django.shortcuts import render
from django.views.generic import View
from photo.models import Photo
from django.core.paginator import Paginator


# Create your views here.

class PhotoView(View):
    def get(self, request, page):
        photos = Photo.objects.all()

        # 分页
        paginator = Paginator(photos, 3)

        # 获取第几页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        # 获取第page页的Page实例对象
        photo_page = paginator.page(page)

        # 进行页码控制
        num_pages = paginator.num_pages


        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)




        content = {
            'pages': pages,
            'photo_page': photo_page,
        }

        return render(request, 'photo.html', content)
