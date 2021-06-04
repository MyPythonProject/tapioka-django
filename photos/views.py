from django.views import generic
from photos.models import Item, Photo


class IndexView(generic.ListView):
    template_name = 'photos/index.html'

    def get_queryset(self):
        return Item.objects.all()[:5]


class ListView(generic.ListView):
    model = Item
    template_name = 'photos/items_list.html'

    def get_queryset(self):
        return Item.objects.all()[:10]


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'photos/items_detail.html'


class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'photos/photos_detail.html'
