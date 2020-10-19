from django.urls import path
# from .api_views import WordList
# from . import generic_views
from . import mixins

from rest_framework import routers
# from . import viewsets

router = routers.DefaultRouter()
# router.register('english_api', viewsets.WordViewSet)
router.register('english_api', mixins.WordViewSet)

urlpatterns = [
    # path('words/', WordList.as_view(), name='word_list')
    # path('', generic_views.ListCreateWord.as_view(), name='word_list'),
    # path('<int:pk>', generic_views.RetrieveUpdateDestroyWord.as_view(), name='word_detail'),
]

urlpatterns += router.urls
