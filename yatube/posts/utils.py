from django.core.paginator import Paginator
from .constants import POST_COUNT


def page_nav(request, posts):
    """"""
    paginator = Paginator(posts, POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj
