from .models import category

def all_links(request):
    links=category.objects.all()
    return dict(links=links)