from . import views
from django.urls import path, include

urlpatterns = [
    path("",views.ImageViewSet.as_view(({
        'post':'create'
    })),name='image-count'),
]
